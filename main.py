import re

from playwright.sync_api import sync_playwright


class GoogleSearch:

    def __init__(self, keyword):
        self.keyword = keyword
        self.url = f"https://www.google.com/search?q={keyword}"

    def get_hit_count(self) -> int:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(self.url)
            # id: result-stats
            result = page.eval_on_selector("#result-stats", "el => el.textContent")
            browser.close()

            if result is None:
                return 0

            pattern = r"(\d+)\s*件"
            match = re.search(pattern, result.replace(",", ""))

            if match:
                number_str = match.group(1)
                number = int(number_str)
                return number
            else:
                return 0


if __name__ == "__main__":
    keyword = "Python"
    hit_count = GoogleSearch(keyword).get_hit_count()
    print(f"Hit count for {keyword}: {hit_count}")
