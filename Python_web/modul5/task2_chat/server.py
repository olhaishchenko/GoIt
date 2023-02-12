import asyncio
import json
import logging
from datetime import datetime, timedelta

import aiohttp
import websockets
import names
from websockets import WebSocketServerProtocol, WebSocketProtocolError
from websockets.exceptions import ConnectionClosedOK

logging.basicConfig(level=logging.INFO)


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


async def get_exchange(date):
    # today = datetime.today().date()
    # date = today.strftime("%d.%m.%Y")
    r = await request('https://api.privatbank.ua/p24api/exchange_rates?json&date=' + date)
    exchange_rate = {r['date']: {'EUR': {}, 'USD': {}}}
    for rate in r['exchangeRate']:
        if rate.get('currency') in ['EUR', 'USD']:
            exchange_rate[r['date']][rate['currency']]['sale'] = rate['saleRate']
            exchange_rate[r['date']][rate['currency']]['purchase'] = rate['purchaseRate']

    return f"{exchange_rate}"


class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} disconnects')

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

    async def send_to_client(self, message: str, ws: WebSocketServerProtocol):
        await ws.send(message)

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distrubute(ws)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    def list_days(self, count: int) -> list:
        if count >= 10:
            raise ValueError("Among days can't be more 10")
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

    async def distrubute(self, ws: WebSocketServerProtocol):

        async for message in ws:

            if message.startswith('exchange') or message.startswith('exch'):
                list_message = message.split(' ')
                if len(list_message) == 1:
                    count_day = 1
                else:
                    count_day = int(list_message[1])
                date = self.list_days(count_day)

                answer = []
                for day in date:
                    r = await get_exchange(day)
                    answer.append(r)
                await self.send_to_client(answer, ws)
            else:
                await self.send_to_clients(f"{ws.name}: {message}")


async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 8080):
        await asyncio.Future()  # run forever


if __name__ == '__main__':

    asyncio.run(main())
