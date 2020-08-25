import asyncio
import pyppeteer
import pandas as pd


def save(info_list):
    name = ['名称', '地址', '等级', '评分', '价格', '简介']
    res = pd.DataFrame(info_list, columns=name)
    print(res)
    # res.to_csv('北京部分景点信息.csv', encoding='utf-8')
    res.to_excel('北京部分景点信息.xlsx', encoding='utf-8')


async def main():
    browser = await pyppeteer.launch(
        headless=False,
        # defaultViewport={'width': 1366, 'height': 768},
        args=['--window-size=1366,768']
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 688})
    await page.goto('http://show.ybccode.com/travel/')
    await asyncio.sleep(2)
    await page.screenshot(path='成功访问页面.jpg', fullPage=True)

    await page.click('.signIn')
    await asyncio.sleep(2)

    await page.type('#uName', 'admin')
    await asyncio.sleep(0.5)

    await page.type('#uPass', '123456')
    await asyncio.sleep(0.5)

    await page.hover('.handler')
    await page.mouse.down()
    await page.mouse.move(513 + 340 - 50 + 25, 0)
    await page.mouse.up()
    await asyncio.sleep(1)

    await page.click('#loginBtn')
    await asyncio.sleep(5)

    await page.screenshot(path='成功登录.jpg', fullPage=True)

    # document = await page.content()
    info_list = []
    description = await page.querySelectorAll('.description')
    for scene in description:
        h5 = await scene.querySelector('h5')
        name = await (await h5.getProperty('textContent')).jsonValue()

        h4 = await scene.querySelector('h4')
        score = await (await h4.getProperty('textContent')).jsonValue()
        score = score.split('：')[1]

        h3 = await scene.querySelector('h3')
        intro = await (await h3.getProperty('textContent')).jsonValue()

        span = await scene.querySelectorAll('span')
        address = await (await span[0].getProperty('textContent')).jsonValue()
        level = await (await span[1].getProperty('textContent')).jsonValue()
        price = await (await span[2].getProperty('textContent')).jsonValue()

        info = [name, address, level, score, price, intro]
        # print(info)
        info_list.append(info)

    print(info_list)

    await page.close()
    await browser.close()

    save(info_list)


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()
asyncio.run(main())