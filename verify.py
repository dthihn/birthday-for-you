from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("http://localhost:8000/noelnoem-main/index.html")
    page.wait_for_timeout(3000) # wait for page load / assets

    # Click start button if it exists
    start_btn = page.locator("#start-btn")
    if start_btn.is_visible():
        start_btn.click()
        page.wait_for_timeout(500)

    page.wait_for_timeout(3000)

    # Take screenshot at the key moment
    page.screenshot(path="/home/jules/verification/screenshots/verification2.png")
    page.wait_for_timeout(1000)  # Hold final state for the video

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()  # MUST close context to save the video
            browser.close()