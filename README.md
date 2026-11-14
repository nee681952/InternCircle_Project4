
# Web Scraper for Quotes

## Project Overview
This project is a Python web scraper that collects quotes, author names, and tags from a public practice website using Requests and BeautifulSoup.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- JSON
- HTML

## Data Source
https://quotes.toscrape.com/

This website is designed for practising web scraping.

## Features
- Fetches website HTML using Requests.
- Extracts quote text, author names, and tags.
- Collects quotes from multiple pages.
- Handles request errors.
- Saves collected data in JSON format.
- Creates a readable text file.
- Displays a summary of collected quotes.

## Project Files
- `scraper.py` – Main Python program.
- `quotes.json` – Extracted quote data in JSON format.
- `quotes.txt` – Readable quote records.

## Installation

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

## How to Run

```bash
python scraper.py
```

## Scraping Rules
- Uses a public practice website.
- Sends a descriptive User-Agent header.
- Uses a request timeout.
- Waits one second between page requests.
- Does not scrape personal information or login-protected pages.

## Learning Outcome
Learned how to send HTTP requests, inspect HTML, extract information using BeautifulSoup, handle multiple pages, and save data using Python.
