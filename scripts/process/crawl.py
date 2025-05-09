from seleniumbase import SB
import bs4


def get_navigation_urls():
    for i in range(1, 100):
        yield i, f"https://stackoverflow.com/questions/tagged/python?tab=votes&page={i}&pagesize=50"

def crawl_index():
    with SB(uc=True, test=True, locale="en") as sb:
        for i, url in get_navigation_urls():
            sb.activate_cdp_mode()
            sb.open(url)
            sb.uc_gui_click_captcha()
            sb.sleep(2)
            sb.save_page_source(f"./data/raw/page-{i}.html", folder=None)

def crawl_posts():
    with SB(uc=True, test=True, locale="en") as sb:
        with open("./data/raw/pages/urls.txt", "w") as export:
            i = 671
            for line in open("./data/raw/index/urls.txt"):
                line = line.strip()
                if not line: continue

                with open(f"./data/raw/index/{line}") as file:
                    content = file.read()
                soup = bs4.BeautifulSoup(content)
                for link in soup.select("#questions .s-link"):
                    href = "https://stackoverflow.com" + link.attrs.get("href")
                    sb.activate_cdp_mode()
                    sb.open(href)
                    sb.uc_gui_click_captcha()
                    sb.sleep(1)
                    sb.save_page_source(f"./data/raw/pages/page-{i}.html", folder=None)
                    i += 1



crawl_posts()
