import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': 'Insert your number here',       #your cell number goes here, you only get 1 free message.
        'message': 'Im sending you this message from Python!',
        'key': 'textbelt',
    })
    print(resp.json())

#schedule.every().day.at('18:00').do(send_message)

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)