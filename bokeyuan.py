import requests


class BK:
    def __init__(self):
        self.url = 'https://www.cnblogs.com/#p{}'

    def get_pages(self, url):
        return requests.get(url).content.decode()

    def save_pages(self, content, page):
        file_name = "第{}页.txt".format(page)
        with open('./data/{}'.format(file_name), 'w', encoding='utf-8') as f:
            # 写入数据
            f.write(content)

    def run(self):
        for page_index in range(5):
            url = self.url.format(page_index + 1)
            content = self.get_pages(url)
            self.save_pages(content,page_index + 1)


if __name__ == '__main__':
    BK().run()
