#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from random import randint
from time import sleep

with open('config.json', "r") as f:
    file_content = f.read()
    config = json.loads(file_content)

def slaves(slave_method, id, get = ""):
    sleep(config['timing'])
    if get:
        req = requests.get(
            f'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/{slave_method}?id={id}',
            headers={
                "authorization": config["auth"],
                "content-type": "application/json",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
            }
        ).json()
        
        return req
    else:
        req = requests.post(
            f'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/{slave_method}',
            headers={
                "authorization": config["auth"],
                "content-type": "application/json",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
            },
            data=json.dumps({
                "slave_id": id,
                "name": "vk.com/trard"
            })
        )

    if req.ok:
        print(f"{slave_method} {id}")
    else:
        print(f"Ошибка {req.status_code} в {slave_method}. Повторяю")
        slaves(slave_method, id)

def main():
    balance = slaves("start", 1, "get")['me']['balance']
    while balance > config['minBalance']:
        if config['InvisibleSlaves']:
            id = randint(-600000000,-1)
        else:
            id = randint(1,600000000)

        slave = slaves("user", id, "get")
        if slave['price'] <= config['maxSlavePrice']:
            slaves("buySlave", id)
            slaves("jobSlave", id)
            if config["buyFetters"]:
                slaves("buyFetter", id)

        if config['checkBalance']:
            balance = slaves("start", 1, "get")['me']['balance']


if __name__ == "__main__":
    main()
