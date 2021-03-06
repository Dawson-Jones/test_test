import asyncio
import itertools


async def spin(msg):  # <1>
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        print(status, flush=True, end='\r')
        try:
            await asyncio.sleep(.1)  # <2>
        except asyncio.CancelledError:  # <3>
            break
    print(' ' * len(status), end='\r')


async def slow_function():  # <4>
    # pretend waiting a long time for I/O
    await asyncio.sleep(3)  # <5>
    return 42


# async def supervisor():  # <6>
#     # spinner = asyncio.ensure_future(spin('thinking!'))
#     spinner = asyncio.create_task(spin('thinking!'))  # <7>
#     print('spinner object:', spinner)  # <8>
#     result = await slow_function()  # <9>
#     spinner.cancel()  # <10>
#     return result


async def main1():
    task = asyncio.create_task(spin('thinking!'))
    print('spinner object:', task)  # <8>
    return await main2(task)


async def main2(future):
    result = await slow_function()
    future.cancel()
    return result


def main():
    # result = asyncio.run(supervisor())  # <11>
    result = asyncio.run(main1())  # <11>
    print('Answer:', result)


if __name__ == '__main__':
    main()
