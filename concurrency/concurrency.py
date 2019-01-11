import time
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)


def complex_calculation():
    start = time.time()
    print("Started calculating...")
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - start}')


start = time.time()

with ThreadPoolExecutor(max_workers = 2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f'Two thread total time: {time.time() - start}')
