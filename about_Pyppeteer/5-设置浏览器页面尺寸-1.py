import asyncio
import pyppeteer
from screeninfo import get_monitors


# 获取电脑屏幕尺寸
# print(get_monitors())
# for data in get_monitors():
#     print(data)   # Monitor(x=0, y=0, width=1440, height=900, width_mm=None, height_mm=None, name=None)

async def main():
    # launch()新建浏览器进程,headless参数设置浏览器是否为“无头模式”
    browser = await pyppeteer.launch(
        headless=False,
        defaultViewport={'width': 1366, 'height': 788}
    )
    # 在浏览器中新建页面
    page = await browser.newPage()
    # 访问指定页面
    await page.goto('http://show.ybccode.com/travel/')
    # 延迟给定的时间
    await asyncio.sleep(5)
    # 获取页面截图
    # await page.screenshot(path='./成功打开页面截图2.jpg', fullPage=True)
    # 关闭页面
    await page.close()
    # 关闭浏览器
    await browser.close()


# 创建异步事件循环
loop = asyncio.get_event_loop()
# 执行异步事件循环
# loop.run_until_complete()
asyncio.run(main())  # Python3.7版本写法
loop.close()
