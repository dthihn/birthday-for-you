from playwright.sync_api import sync_playwright
import time
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(f"file://{os.path.abspath('noelnoem-main/index_giang_cute.html')}")
    page.screenshot(path="tulip_cute.png")

    # Wait for auto-loader to finish (2s + 1s + some buffer)
    print("Waiting 6 seconds for auto-transition...")
    time.sleep(6)

    # Take screenshot of the 3D scene
    page.screenshot(path="tulip_cute_scene.png")

    browser.close()
