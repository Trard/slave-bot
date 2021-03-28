#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from json import loads
from random import randint
from time import sleep

with open('config.json', "r") as f:
    file_content = f.read()
    config = loads(file_content)

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": config['auth'],
    "origin": "https://prod-app7794757-6f6bf9481ca4.pages-ac.vk-apps.com",
    "referer": "https://prod-app7794757-6f6bf9481ca4.pages-ac.vk-apps.com/",
    "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}


def slaves(slave_method, id, get = ""):
    sleep(config['timing'])

    if get:
        req = requests.get(
            f'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/{slave_method}',
            headers=headers,
            params = {
                "id": id
            }
        )
    else:
        req = requests.post(
            f'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/{slave_method}',
            headers=headers,
            json={
                "slave_id": id,
                "name": "vk.com/trard"
            }
        )

    if req.ok:
        print(f"{slave_method} {id}")
        return req.json()
    else:
        print(f"Ошибка {req.status_code} в {slave_method}. Повторяю")
        slaves(slave_method, id, get)

def main():
    balance = slaves("start", 1, "get")['me']['balance']
    while balance >= config['minBalance']:
        try:
            id = randint(1, 600000000)
            if config['InvisibleSlaves']:
                id = -id

            slaveprice = slaves("user", id, "get")['price'] if config['checkSlavePrice'] else 0

            if slaveprice <= config['maxSlavePrice']:
                slaves("buySlave", id)
                slaves("jobSlave", id)
                if config["buyFetters"]:
                    slaves("buyFetter", id)

            if config['checkBalance']:
                balance = slaves("start", 1, "get")['me']['balance']

        except Exception as e:
            print(e)
            sleep(config['timing']*2)


if __name__ == "__main__":
    main()
