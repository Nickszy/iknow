import json,requests,base64,datetime
import logging

class QunRobot(object):
    '''
    构建企业微信实例，主要
    https://developer.work.weixin.qq.com/document/path/90240
    
    TODO 开源方案：https://github.com/GentleCP/corpwechatbot
    '''
    
    def __init__(self,cid,aid,secret,touid):
        self.cid = cid
        self.aid = aid
        self.secret = secret
        self.touid = touid
        self.access_token = ''
        self.access_token_valid_time= datetime.datetime.now()

    
    @property
    def get_access_token(self):
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.cid}&corpsecret={self.secret}"
        if self.access_token_valid_time <= datetime.datetime.now():
            # 验证码失效，重新获取
            response = json.loads(requests.get(get_token_url).content)
            expires_in = response.get('expires_in')
            self.access_token_valid_time = datetime.datetime.now()+datetime.timedelta(seconds=expires_in-5)  # 考虑网络损耗，人为减少5s有效时间
            self.access_token = response.get('access_token')
            logging.info("获取验证码成功")
            return self.access_token
        else:
            # 验证码有效
            return self.access_token

    def send_text(self,text):
        if self.get_access_token and len(self.get_access_token) > 0:
            send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={self.get_access_token}'
            data = {
                "touser":self.touid,
                "agentid":self.aid,
                "msgtype":"text",
                "text":{
                    "content":text
                },
                "duplicate_check_interval":600
            }
            response = requests.post(send_msg_url,data=json.dumps(data)).content
            return response
        else:
            return False

    def send_image(self,base64_content):
        access_token = self.get_access_token
        if access_token and len(access_token) > 0:
            upload_url = f'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={access_token}&type=image'
            upload_response = requests.post(upload_url, files={
                "picture": base64.b64decode(base64_content)
            }).json()
            if "media_id" in upload_response:
                media_id = upload_response['media_id']
            else:
                return False

            send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
            data = {
                "touser":self.touid,
                "agentid":self.aid,
                "msgtype":"image",
                "image":{
                    "media_id": media_id
                },
                "duplicate_check_interval":600
            }
            response = requests.post(send_msg_url,data=json.dumps(data)).content
            return response
        else:
            return False

    def send_markdown(self,text):
        access_token = self.get_access_token
        if access_token and len(access_token) > 0:
            send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
            data = {
                "touser":self.touid,
                "agentid":self.aid,
                "msgtype":"markdown",
                "markdown":{
                    "content":text
                },
                "duplicate_check_interval":600
            }
            response = requests.post(send_msg_url,data=json.dumps(data)).content
            return response
        else:
            return False

if __name__ == '__main__':
    cid = 'wwb8324e99c6d7e4b9'                                # 企业
    aid = '1000009'                                           # 应用
    secret = 'xttfW4pEeXn7AnzfwhqObEI3ll5guXCjK8u55nQiaHE'    # 应用密钥
    touid = 'shenzheyu'                                       # 默认范围

    we = QunRobot(cid,aid,secret,touid)
    we.send_text('hello world')
    we.send_markdown('# hello world \n ##你好  \n**空尼齐瓦**')