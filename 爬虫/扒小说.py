import json

import requests
import asyncio
import aiohttp

url = "http://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}"


async def download(info: dict):
    chapter_name = info['title'] + '.txt'
    chapter_cid = info['cid']
    data_text = {
        "book_id": "4306063500",
        "cid": "4306063500|10364019",
        "need_bookinfo": 1
    }
    data_text['cid'] = "4306063500|" + chapter_cid
    url_text = f"http://dushu.baidu.com/api/pc/getChapterContent?data={json.dumps(data_text)}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url_text) as resp:
            res = await resp.json()
            # print(res['data']['novel']['content'])
            with open("files/" + chapter_name, mode="w", encoding='utf-8') as f:
                f.write(res['data']['novel']['content'])


async def main():
    tasks = []
    resp = requests.get(url)
    try:
        all_data = resp.json()['data']['novel']['items']
    except Exception as e:
        print(resp.json())
        return
    resp.close()
    for data in all_data:
        tasks.append(asyncio.create_task(download(data)))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
