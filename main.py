import vk_api
import time
import requests
import urllib.request
from random import randint, choice
import os

while True:
    nomer = os.environ.get('USER_NOMER')
    passwd = os.environ.get('USER_PASSWD')
    token = os.environ.get('USER_TOKEN')
    vk_session = vk_api.VkApi(str(nomer), str(passwd))
    vk_session.auth()
    vk = vk_session.get_api()

    name = 1
    def automeme(random_mem):
        try:
            r = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                     'access_token': str(token),
                                     'v': 5.103,
                                     'domain': 'bugzhacks',
                                     'count': 1,
                                     'offset': random_mem
                               }
                               )
            all_post = []
            data = r.json()['response']['items']
            all_post.extend(data)
            for post in all_post:
                url = post['attachments'][0]['photo']['sizes'][7]['url']
                img = urllib.request.urlopen(url).read()
                out = open("meme.jpg", "wb")
                out.write(img)
            upload = vk_api.VkUpload(vk_session)
            photo = upload.photo(
                'meme.jpg',
                album_id=271566877,
                group_id=193571079
            )
            photo_url = 'photo{}_{}'.format(
                photo[0]['owner_id'], photo[0]['id']
            )
            vk.wall.post(owner_id="-193571079", from_group=1, attachments=photo_url)
        except:
            print("Ошибка")
            automeme(random_mem=randint(1,500))

    timer = 2700

    while name < 5:
        automeme(random_mem=randint(1,500))
        name = name + 1
        time.sleep(timer)