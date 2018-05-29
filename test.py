import asyncio


async def coro1():
    print("C1: Start")
    await asyncio.sleep(1)
    print("C1: Stop")


async def coro2():
    print("C2: Start")
    print("C2: a")
    await asyncio.sleep(1)
    print("C2: b")
    await asyncio.sleep(1)
    print("C2: c")
    await asyncio.sleep(1)
    print("C2: Stop")

def main():
    loop = asyncio.get_event_loop()
    tasks = [coro1(), coro2()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == "__main__":
    main()