import schedule
import time
import requests
def start():
    def docheck():
        print('定时任务已经启动')
        r = requests.get('http://127.0.0.1:8000/wechat/check')
        print(r.content)
    schedule.every(2).minutes.do(docheck)


    while True:
        schedule.run_pending()
        time.sleep(10)
