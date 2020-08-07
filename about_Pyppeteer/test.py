import asyncio
from pyppeteer import launch


async def main():
    brower = await launch()
    page = await brower.newPage()
    await page.goto('https://www.bilibili.com/')
    await page.screenshot({'path': 'bilibili.png'})
    await brower.close()


asyncio.get_event_loop().run_until_complete(main())
