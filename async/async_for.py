import asyncio
import time

async def my_gen(u: int = 10):
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(1)


async def main():
    g = [i async for i in my_gen()]
    f = [j async for j in my_gen() if not (j // 3 % 5)]
    return g, f


if __name__ == "__main__":
    s = time.perf_counter()

    g, f = asyncio.run(main())

    print(g)
    print(f)
    print(f"Program finished in: {time.perf_counter() - s}")