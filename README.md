# Bing Search and Wiki Content Retrieval

This Python script utilizes the Playwright library to perform a Bing search and retrieve Wikipedia content from the search results.

## Requirements

- Python 3.x
- Playwright library (install via pip: `pip install playwright`)

## Usage

1. Run the script.
2. Enter the search term when prompted.
3. The script will open a Chromium browser, navigate to Bing, and perform a search with the provided term.
4. It will then wait for the search results to load and retrieve the Wikipedia content from each result.
5. The retrieved content will be printed to the console.

## Code Overview

- The script uses the Playwright library to automate browser interactions.
- It launches a Chromium browser and creates a new browsing context.
- It then opens a new page within the context and navigates to Bing.
- After waiting for the search bar to load, it fills in the provided search term and presses Enter.
- It waits for the search results to load and retrieves the Wikipedia content from each result.
- Finally, it prints the retrieved content to the console.

## Disclaimer

- This script is for educational purposes only.
- Use responsibly and ensure compliance with Bing's terms of service.