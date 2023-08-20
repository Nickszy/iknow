import json
# from functools import cached_property
import requests

class weread:

    def __init__(self) -> None:
        pass

    @property
    def skey(self):

        url = "https://i.weread.qq.com/login"

        payload = json.dumps({
            "random": 1592359318,
            "deviceId": "1c6c299cce6d43377b37433196fa4fec",
            "refCgi": "",
            "deviceName": "zheyu’s iPhone",
            "signature": "e52b3383ea471824e124a61a4a5eb6b139db0c965746ce27d38824085130edb2",
            "refreshToken": "onb3MjkEPYy4Y5EUAgMcNk07cQmU@jjMGNOwWTV0c6dZ7VwH6mQAA",
            "wxToken": 1,
            "timestamp": 1686589376,
            "inBackground": 0,
            "deviceToken": "4b854408531a4445d5515ae84bb4186fce6a2dd139d17de278b29d831690c63b"
        })
        headers = {
            'Cache-Control': 'no-cache',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Host': 'i.weread.qq.com',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()["accessToken"]

    def _request(self, method: str, url: str, headers: dict = None, payload: dict = None, data: dict = None):
        '''
        # TODO 内部封装一个请求方法
        '''
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code != '200':
            pass
        return response

    def search(self, key: str, scope: str = '2') -> list:
        '''
        查询通过 scope区分
        'scope': 0, 'name': '全部'},
        'scope': 10, 'name': '电子书'},
        'scope': 6, 'name': '作者'},
        'scope': 12, 'name': '全文'},
        'scope': 14, 'name': '微信听书'},
        'scope': 13, 'name': '书单'},
        'scope': 2, 'name': '公众号'},
        'scope': 4, 'name': '文章'}
        '''

        url = f"https://i.weread.qq.com/store/search?count=15&keyword={key}&scope={scope}&v=2"

        payload = {}
        headers = {
            'Cache-Control': 'no-cache',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate,br',
            'Connection': 'keep-alive',
            'vid': '18878438',
            'v': '7.3.4.18',
            'skey': self.skey,
            'Host': 'i.weread.qq.com',
            'Cookie': 'wr_logined=1',
            'User-Agent': 'WeRead/7.3.4 (iPhone; iOS 16.1; Scale/3.00)'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()['books']

    def get_booklist(self, booilistid: str):
        '''
        ## 书单
        18878438_7HKRjUBo5
        '''

        url = f"https://i.weread.qq.com/booklist/single?booklistId={booilistid}"

        payload = {}
        headers = {
            'Cache-Control': 'no-cache',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate,br',
            'Connection': 'keep-alive',
            'vid': '18878438',
            'v': '7.3.4.18',
            'skey': self.skey,
            'Host': 'i.weread.qq.com',
            'Cookie': 'wr_logined=1',
            "Content-Type": "application/json",
            'User-Agent': 'WeRead/7.3.4 (iPhone; iOS 16.1; Scale/3.00)'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()["booklist"]

    def get_articles(self, bookid):
        # bookid = "MP_WXS_2390204840"

        url = f"https://i.weread.qq.com/book/articles?bookId={bookid}&count=20&offset=0&synkey=0"

        payload = {}
        headers = {
            'Cache-Control': 'no-cache',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate,br',
            'Connection': 'keep-alive',
            'vid': '18878438',
            'v': '7.3.4.18',
            'skey': self.skey,
            'Host': 'i.weread.qq.com',
            "Content-Type": "application/json",
            'Cookie': 'wr_logined=1',
            'User-Agent': 'WeRead/7.3.4 (iPhone; iOS 16.1; Scale/3.00)'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()["reviews"]


if __name__ == "__main__":
    wr = weread()
    print(wr.get_articles("MP_WXS_2390204840"))
    print(wr.get_booklist("18878438_7HKRjUBo5"))
