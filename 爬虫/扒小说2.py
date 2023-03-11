import requests
import os
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.192.400 QQBrowser/11.5.5250.400"
}
book_info = {
    'name': "全职高手",
    "id": "766",
    "ivk_sa": "",
    "max_page": 88
}


def download_one_chapter(html: str, cur: int) -> str:
    tmp_html = html
    if cur != 1:
        tmp_html = html[:-5] + '_' + str(cur) + html[-5:]
    url = f"https://m.xxbooktxt.com/{tmp_html}"
    resp = requests.get(url, headers=header)
    resp.encoding = 'gbk'
    page_html = BeautifulSoup(resp.text, "html.parser")
    txt = page_html.find('div', id="nr1").getText()
    resp.close()
    if txt.count("本章未完,请翻页"):
        txt = txt.replace("(本章未完,请翻页)记住手机版网址：m.xxbooktxt.com", "") + download_one_chapter(html, cur + 1)
    else:
        txt = txt.replace("记住手机版网址：m.xxbooktxt.com", "")
    return txt


def download_one_chapter_1(title: str, html: str):
    all_text = download_one_chapter(html, 1)
    all_text = all_text.replace(title, '')
    all_text = all_text.replace(" 一秒记住，精彩小说无弹窗免费阅读！", '')
    all_text = all_text.replace("第(1/3)页", '')
    all_text = all_text.replace("第(2/3)页", '')
    all_text = all_text.replace("第(3/3)页", '')
    f = open(f"files//{book_info['name']}//" + title + '.txt', 'w', encoding='utf-8')
    f.write(all_text)
    f.flush()
    print(f"{title}下载完毕")
    f.close()


def download_one_group_chapter(url: str):
    # url = "https://m.xxbooktxt.com/wapbook/21032/index_2.html?ivk_sa=1023337"
    # print(f'正在请求{url}')
    resp = requests.get(url, headers=header)
    resp.encoding = 'gbk'
    page_html = BeautifulSoup(resp.text, "html.parser")
    ul_chapter = page_html.findAll('ul', class_="chapter")
    a_list = ul_chapter[1].findAll('a')
    resp.close()
    with ThreadPoolExecutor(5) as t:
        for a in a_list:
            href = a.get('href')
            title = a.getText()
            t.submit(download_one_chapter_1, title=title, html=href)


if __name__ == "__main__":
    if not os.path.exists(f"files//{book_info['name']}"):
        os.mkdir(f"files//{book_info['name']}")
    s_add = ""
    if len(book_info['ivk_sa']):
        s_add = f"?ivk_sa={book_info['ivk_sa']}"
    with ThreadPoolExecutor(10) as t:
        for i in range(1, book_info['max_page']):
            url = f"https://m.xxbooktxt.com/wapbook/{book_info['id']}/index_{i}.html" + s_add
            t.submit(download_one_group_chapter, url=url)
