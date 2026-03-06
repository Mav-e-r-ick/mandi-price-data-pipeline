import asyncio
from playwright.async_api import async_playwright

async def run():

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(accept_downloads=True)
        page = await context.new_page()

        await page.goto("https://agmarknet.gov.in/marketarrivalsweekanalysis")

        await page.wait_for_timeout(6000)

        # Select Commodity
        await page.click("text=Select Commodity")
        await page.click("text=Tomato")

        # Select State
        await page.click("text=State")
        await page.click("text=Maharashtra")

        # Select District
        await page.click("text=District")
        await page.click("text=Pune")

        # Select Year
        await page.click("text=Year")
        await page.click("text=2021")

        # Select Month
        await page.click("text=Month")
        await page.click("text=January")

        # Select Week
        await page.click("text=Week")
        await page.click("text=Week 1")

        await page.wait_for_timeout(2000)

        # Submit
        await page.locator("button:has-text('Submit')").click()

        await page.wait_for_selector("text=Export")

        # Download CSV
        async with page.expect_download() as download_info:
            await page.click("text=Export")

        download = await download_info.value
        await download.save_as("agmarknet_data.csv")

        await browser.close()

asyncio.run(run())