import asyncio
import pyppeteer


async def main():
    browser = await pyppeteer.launch(
        headless=False,
        defaultViewport={'width': 1366, 'height': 668},
        args=['--windows-size=1366,768']
    )
    page = await browser.newPage()
    url = 'http://show.ybccode.com/travel/'
    await page.goto(url)
    await asyncio.sleep(1)
    await page.click('.signIn')
    await asyncio.sleep(1)

    await page.type('#uName', 'admin')
    await asyncio.sleep(1)
    await page.type('#uPass', '123456')
    await asyncio.sleep(1)
    await page.hover('.handler')
    await page.mouse.down()
    await page.mouse.move(828, 0)
    await page.mouse.up()
    await asyncio.sleep(1)
    await page.click('#loginBtn')

    await asyncio.sleep(5)
    # 获取页面截图
    # await page.screenshot(path='./成功打开页面截图2.jpg', fullPage=True)

    await page.close()
    await browser.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# asyncio.run(main())
loop.close()
