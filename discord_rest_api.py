import aiohttp, asyncio

BASE_URL = "https://discordapp.com/api/v6"
loop = asyncio.get_event_loop()

class HTTPClient:
    def __init__(self, token, bot=True):
        self.session = aiohttp.ClientSession()
        if bot:
            token = "Bot {}".format(token)
        self.token = token

    def get_headers(self):
        headers = {}
        headers['Authorization'] = self.token
        headers['User-Agent'] = "Python"
        return headers

    async def get(self, endpoint):
        resp = await self.session.get(BASE_URL + endpoint, headers=self.get_headers())
        return await resp.json()

    async def post(self, endpoint, json=None):
        headers = self.get_headers()
        if json != None:
            headers['Content-Type'] = "application/json"
        resp = await self.session.post(BASE_URL + endpoint, headers=headers, data=json)
        return await resp.json()

    async def delete(self, endpoint):
        resp = await self.session.delete(BASE_URL + endpoint, headers=self.get_headers())
        return await resp.json()

    async def head(self, endpoint):
        resp = await self.session.head(BASE_URL + endpoint, headers=self.get_headers())
        return await resp.json()

    async def options(self, endpoint):
        resp = await self.session.options(BASE_URL + endpoint, headers=self.get_headers())
        return await resp.json()

    async def patch(self, endpoint, json=None):
        headers = self.get_headers()
        if json != None:
            headers['Content-Type'] = "application/json"
        resp = await self.session.patch(BASE_URL + endpoint, headers=headers, data=json)
        return await resp.json()

    async def put(self, endpoint, json=None):
        headers = self.get_headers()
        if json != None:
            headers['Content-Type'] = "application/json"
        resp = await self.session.put(BASE_URL + endpoint, headers=headers, data=json)
        return await resp.json()


class Interface(object):
    def __init__(self, token):
        self.http = HTTPClient(token)
    def get(self, uri):
        return loop.run_until_complete(self.http.get(uri))
    def post(self, uri, json=None):
        return loop.run_until_complete(self.http.post(uri, json))
    def delete(self, uri):
        return loop.run_until_complete(self.http.delete(uri))
    def head(self, uri):
        return loop.run_until_complete(self.http.head(uri))
    def options(self, uri):
        return loop.run_until_complete(self.http.options(uri))
    def patch(self, uri, json=None):
        return loop.run_until_complete(self.http.patch(uri, json))
    def put(self, uri, json=None):
        return loop.run_until_complete(self.http.put(uri, json))
