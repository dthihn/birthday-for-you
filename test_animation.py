from playwright.sync_api import sync_playwright
import time
import os

def test_scene():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Make sure we give permissions so camera code doesn't crash
        # (or at least we mock it)
        context = browser.new_context(permissions=['camera'])
        page = context.new_page()

        print("Navigating to index.html...")
        page.goto("http://localhost:8000/index.html", wait_until="networkidle")

        # Wait for loading to finish and Start button to appear
        print("Waiting for #start-btn...")
        page.wait_for_selector("#start-btn", state="visible", timeout=15000)

        print("Clicking start button...")
        page.click("#start-btn")

        # Wait a bit for animation to run to verify no immediate crash
        time.sleep(3)

        # Take a screenshot to verify rendering is still working
        os.makedirs("artifacts", exist_ok=True)
        page.screenshot(path="artifacts/scene.png")
        print("Screenshot saved to artifacts/scene.png")

        browser.close()

if __name__ == "__main__":
    test_scene()
