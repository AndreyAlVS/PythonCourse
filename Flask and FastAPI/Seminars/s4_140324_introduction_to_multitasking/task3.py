# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте async.
import asyncio
import os
import time
import aiofiles

MY_PATH = '.'


async def worker(file_):
    async with aiofiles.open(file_, 'r', encoding='utf-8') as f:
        content = await f.read()
        print(f'words in {file_} : {len(content.split())} in {time.time() - start_time:.2f} seconds"')


start_time = time.time()


async def main():
    for root, dirs, file_name in os.walk(MY_PATH):
        for f in file_name:
            task = asyncio.create_task(worker(f))
            await task


if __name__ == '__main__':
    asyncio.run(main())
