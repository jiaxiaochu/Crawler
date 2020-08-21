import asyncio
import time
import pyppeteer


async def main():
    # launch()新建浏览器进程,headless参数设置浏览器是否为“无头模式”
    browser = await pyppeteer.launch(headless=False)
    await asyncio.sleep(5)
    await browser.close()


# 创建异步事件循环
loop = asyncio.get_event_loop()
# 执行异步事件循环
# loop.run_until_complete()
asyncio.run(main())
loop.close()
