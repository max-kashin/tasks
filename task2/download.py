import requests
import random
import re
import os

MAX_COMICS_ID = 2400
BASE_XKCD_URL = "https://xkcd.com/{}/"
COMICS_DIR = 'comics'


def get_random_comics_id() -> int:
    comics_id = None
    while not comics_id:
        file_id = random.randint(0, MAX_COMICS_ID)
        is_comics_downloaded = os.path.isfile(f"./{COMICS_DIR}/{file_id}.png")
        if not is_comics_downloaded:
            comics_id = file_id
    return comics_id


def get_image_url(comics_is: int) -> str:
    url = BASE_XKCD_URL.format(comics_is)
    response = requests.get(url, allow_redirects=True)
    content = response.text
    result = re.search(r'https://imgs.xkcd.com/comics/\w+\.png', content)
    return result.group(0)


def download_comics():
    comics_is = get_random_comics_id()
    image_url = get_image_url(comics_is)
    if image_url:
        response = requests.get(image_url, allow_redirects=True)
        image = response.content
        image_name = f"{comics_is}.png"
        if not os.path.exists(COMICS_DIR):
            os.makedirs(COMICS_DIR)
        downloaded_comics = os.listdir(COMICS_DIR)
        if len(downloaded_comics) >= 2:
            os.remove(f"./{COMICS_DIR}/{downloaded_comics[1]}")
        open(f'./comics/{image_name}', 'wb').write(image)
    else:
        print('Unknown comics URL')
