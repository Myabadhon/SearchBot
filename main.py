from playwright.sync_api import sync_playwright

search_term = input("Enter the Word: ")

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()

    page = context.new_page()

    try:
        page.goto("https://www.bing.com")

        search_bar = page.wait_for_selector("input[name='q']")

        search_bar.fill(search_term)
        page.keyboard.press("Enter")

        page.wait_for_timeout(5000)
        result_titles = page.query_selector_all(".b_paractl")   #Getting Wiki Content

        for title in result_titles:
            print(title.inner_text())

    except Exception as e:
        print(f"An error occurred: {e}")

    context.close()
    browser.close()
