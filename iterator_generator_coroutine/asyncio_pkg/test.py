import aiohttp
import asyncio


async def test():
    async with aiohttp.ClientSession() as session:
        resp = await session.get("http://baidu.com")
        print(resp.status)


if __name__ == '__main__':
    asyncio.run(test())
