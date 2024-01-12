import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as pw:
        browser = await pw.webkit.launch(
            headless=False
        )

        page = await browser.new_page()

        # Maximize the screen (set a large viewport size)
        await page.goto('https://twitter.com/JustShills')
        await page.evaluate('() => { window.innerWidth = screen.width; window.innerHeight = screen.height; }')

        # Wait for 5 seconds (as in your original code)
        await page.wait_for_timeout(5000)

        datas = []
        x = 0
        while x < 1000:  # Scroll down 10 times

            # Scroll down by the viewport height
            await page.evaluate(f'window.scrollBy(0, {str(x)})')

            # Wait for scrolling to take effect (adjust time as needed)
            await page.wait_for_timeout(50)

            # Grab data after each scroll
            article_element = await page.query_selector_all('article')
            for article in article_element:
                result = dict()
                result['Text : '] = await article.inner_text()
                datas.append(result)
            x += 100
        for data in datas:
            print(data)
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
