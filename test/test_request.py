import requests
import time

API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6277553592:AAGJCdQI7TtN3iNBB45kSPMPARlFuOXKd8U'
TEXT: str = 'YRA YRA YRA'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
char_id: int

while counter < MAX_COUNTER:
    print('attempt = ', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
    time.sleep(1)
    counter += 1
