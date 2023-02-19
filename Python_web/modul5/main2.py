import json
import logging
import platform
import sys

import aiohttp
import asyncio

from datetime import timedelta, datetime


def list_days(count: int) -> list:
    if count >= 10:
        raise ValueError("Among days can't be more 10")
        count = 10
    today = datetime.today().date()
    date = today.strftime("%d.%m.%Y")
    data = [date]
    while count > 1:
        day = timedelta(days=1)
        new_day = today - day
        data.append(new_day.strftime("%d.%m.%Y"))
        today = new_day
        count -= 1
    return data


async def request(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    r = await response.json()
                    return r
                logging.error(f"Error status {response.status} for {url}")
        except aiohttp.ClientConnectorError as e:
            logging.error(f"Connection error {url}: {e}")
        return None


async def p24call(date) -> dict:

    async with request('https://api.privatbank.ua/p24api/exchange_rates?json&date=' + date) as response:
        result = await response.json()
        return result


def get_exchange_rates(days) -> list[dict]:

    answer = []
    for day in days:
        r = asyncio.run(p24call(day))
        exchange_rate = {r['date']: {'EUR': {}, 'USD': {}}}
        for rate in r['exchangeRate']:
            if rate.get('currency') in ['EUR', 'USD']:
                exchange_rate[r['date']][rate['currency']]['sale']=rate['saleRate']
                exchange_rate[r['date']][rate['currency']]['purchase'] = rate['purchaseRate']
        print (exchange_rate)
        answer.append(exchange_rate)
    return answer


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    count_date = 1
    if len(sys.argv) > 1:
        count_date = int(sys.argv[1])
    result = get_exchange_rates(list_days(count_date))
    print(json.dumps(result, indent=2, ensure_ascii=False))

