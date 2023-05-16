import requests
import time

API_URL: str = 'https://api.telegram.org/bot'
API_DOGS_URL: str = 'https://random.dog/woof.json'
API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
API_FOX_URL: str = 'https://randomfox.ca/floof/'
BOT_TOKEN: str = '6277553592:AAGJCdQI7TtN3iNBB45kSPMPARlFuOXKd8U'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
cat_response: requests.Response
cat_link: str

while counter < MAX_COUNTER:
    print('attempt = ', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
              #  cat_link = cat_response.json()[0]['url']
              # dog_link = cat_response.json()['url']
                fox_link = cat_response.json()[0]['url']
                # print(fox_link)
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={fox_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
    time.sleep(1)
    counter += 1
