import itchat
from itchat.content import *
import requests

#回复普通聊天
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def single_reply(msg):
    if msg['Type'] == TEXT:
        defaultReply = '抱歉，我正在忙。' + msg['Text']
        print(msg['Text']) #打印接收到的消息
        if msg['Text'] in ["你好","您好","hello","Hollo","Hi","hi","晚上好" ]: #收到特定的消息时特定的回复
            reply = "you too"
        elif msg['Text'] in ["墨痕","小彭"]:
            reply = "我不在线，请打我电话"
        else:
            reply = get_reply(msg['Text']) #调用图灵机器人
        return reply or defaultReply
    return

KEY = '9b4f1b38b0ce4c17a74092345112b03f'
UID = '148947'

def get_reply(msg):
    api_tuling = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': UID
    }
    try:
        ret = requests.post(api_tuling,data=data).json()
        return ret.get('text')
    except:
        return
#rs = get_reply('讲个笑话')
#print(rs)

#登录微信
if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    #myUserName = itchat.get_friends(update=True)[0]['UserName']
    itchat.run() #运行监控进程，检查消息