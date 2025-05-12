"""Module implementing crawling process"""

from seleniumbase import SB


def get_navigation_urls():
    """
    Generates navigation URLs for paginated Stack Overflow questions sorted by votes.

    Yields:
        tuple: A tuple containing the page number (int) and the corresponding URL (str).
    """
    for i in range(1, 100):
        yield i, f"https://stackoverflow.com/questions?tab=votes&page={i}"


def crawl_index():
    """
    Crawls a series of web pages and saves their HTML source locally.

    This function uses a SeleniumBase (SB) context to navigate through a list of URLs,
    interact with CAPTCHA challenges, and save the page source of each URL to a specified
    directory. The function assumes that the URLs are provided by the `get_navigation_urls`
    generator function.

    Steps performed:
    1. Activates Chrome DevTools Protocol (CDP) mode for enhanced browser automation.
    2. Opens each URL from the navigation list.
    3. Handles CAPTCHA challenges using the `uc_gui_click_captcha` method.
    4. Waits for 2 seconds after CAPTCHA handling to ensure the page is fully loaded.
    5. Saves the HTML source of the page to a file named `page-{i}.html` in the `./data/raw/` directory.

    Note:
        - The `SB` context is initialized with `uc=True` (undetected Chrome mode),
          `test=True` (test mode), and `locale="en"` (English locale).
        - The `get_navigation_urls` function must yield tuples of index and URL.

    Raises:
        Any exceptions raised by SeleniumBase or the underlying browser automation
        library during navigation or CAPTCHA handling.

    Returns:
        None
    """
    with SB(uc=True, test=True, locale="en") as sb:
        for i, url in get_navigation_urls():
            sb.activate_cdp_mode()
            sb.open(url)
            sb.uc_gui_click_captcha()
            sb.sleep(2)
            sb.save_page_source(f"./data/raw/page-{i}.html", folder=None)


crawl_index()
