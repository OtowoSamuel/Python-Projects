import requests
import schedule
import time

mobile_number = +2347083247105

def send_messages():
    resp =requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Hey. Good morning beautiful',
        'key': 'textbelt'
    })
    print(resp.json())

#schedule.every().day.at('6:00').do(send_messages)

schedule.every(10).seconds.do(send_messages)

while True:
    schedule.run_pending()
    time.sleep(1)