import platform
import sys

import aiohttp
import asyncio

from datetime import timedelta, datetime

if len(sys.argv) > 1:
    count_date = sys.argv[1]
today = datetime.today().date()
date = today.strftime("%d.%m.%Y")
data = []
data.append(date)
while count_date > 1:
    day = timedelta(days=1)
    begin_interval = today - day
    data.append(begin_interval.strftime("%d.%m.%Y"))
async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.privatbank.ua/p24api/exchange_rates?json&date=' + date) as response:
            # print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])
            # print('Cookies: ', response.cookies)
            # print(response.ok)
            result = await response.json()
            return result


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    exchange_rate = {r['date']: {'EUR': {}, 'USD': {}}}
    for rate in r['exchangeRate']:
        if rate.get('currency') in ['EUR', 'USD']:
            exchange_rate[r['date']][rate['currency']]['sale']=rate['saleRate']
            exchange_rate[r['date']][rate['currency']]['purchase'] = rate['purchaseRate']
    print(exchange_rate)