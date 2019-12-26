import asyncio
import itertools


async def spin(msg):
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        print(status, flush=True, end='\r')
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    print(' ' * len(status), end='\r')


async def slow_function():
    await asyncio.sleep(5)
    return 42


async def supervisor():
    spinner = asyncio.ensure_future(spin('thinking!'))
    print('spinner object: ', spinner)
    result = await slow_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer: ', result)


if __name__ == "__main__":
    main()
