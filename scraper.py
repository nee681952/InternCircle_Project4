
import requests
import time
import json
from bs4 import BeautifulSoup
from collections import Counter

BASE_URL = "https://quotes.toscrape.com"

HEADERS = {
    "User-Agent": "InternCircle-learning-project (student scraper)"
}


def fetch_website():

    try:
        response = requests.get(
            BASE_URL,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        print("Status Code:", response.status_code)
        print("Website connected successfully!")

        return response.text

    except requests.exceptions.RequestException as error:
        print("Website connection failed!")
        print("Error:", error)

        return None

def extract_quotes(html):

    soup = BeautifulSoup(html, "html.parser")

    quotes = soup.select("div.quote")

    extracted_data = []

    for quote in quotes:

        text_element = quote.select_one("span.text")
        author_element = quote.select_one("small.author")

        if text_element and author_element:

            quote_text = text_element.get_text(strip=True)
            author = author_element.get_text(strip=True)

            tags = [
                tag.get_text(strip=True)
                for tag in quote.select("a.tag")
            ]

            quote_data = {
                "text": quote_text,
                "author": author,
                "tags": tags
            }

            extracted_data.append(quote_data)

    return extracted_data

def scrape_all_pages():

    url = BASE_URL + "/"
    all_quotes = []

    while url:

        print("Scraping:", url)

        try:
            response = requests.get(
                url,
                headers=HEADERS,
                timeout=10
            )

            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            page_quotes = extract_quotes(response.text)

            all_quotes.extend(page_quotes)

            next_page = soup.select_one("li.next a")

            if next_page:
                url = BASE_URL + next_page["href"]
            else:
                url = None

            time.sleep(1)

        except requests.exceptions.RequestException as error:
            print("Error:", error)
            break

    return all_quotes

def save_json(quotes):

    with open("quotes.json", "w", encoding="utf-8") as file:

        json.dump(
            quotes,
            file,
            indent=2,
            ensure_ascii=False
        )

    print("Quotes saved to quotes.json")

def save_text(quotes):

    with open("quotes.txt", "w", encoding="utf-8") as file:

        for number, quote in enumerate(quotes, start=1):

            file.write(f"Quote {number}\n")
            file.write(f"Text: {quote['text']}\n")
            file.write(f"Author: {quote['author']}\n")
            file.write(f"Tags: {', '.join(quote['tags'])}\n")
            file.write("-" * 50 + "\n")

    print("Quotes saved to quotes.txt")

def show_summary(quotes):

    print("\n========== SCRAPING SUMMARY ==========")

    total_quotes = len(quotes)

    print("Total quotes collected:", total_quotes)

    if not quotes:
        print("No quotes available for summary.")
        return

    # Count authors
    authors = Counter(
        quote["author"] for quote in quotes
    )

    # Count tags
    all_tags = []

    for quote in quotes:
        all_tags.extend(quote["tags"])

    tags = Counter(all_tags)

    # Display most common author
    print("\nMost quoted author:")

    author, count = authors.most_common(1)[0]

    print(author, "-", count, "quotes")

    # Display most common tag
    print("\nMost common tag:")

    if tags:
        tag, count = tags.most_common(1)[0]
        print(tag, "-", count, "times")
    else:
        print("No tags found.")

    print("\n======================================")


if __name__ == "__main__":

    all_quotes = scrape_all_pages()

    save_json(all_quotes)

    save_text(all_quotes)

    show_summary(all_quotes)