from collections import deque
from time import time


customer_count = int(10e7)
l = [_ for _ in range(1, customer_count+1)]
sll = deque(l)


def get_next_customer(queue: list | deque) -> int:
    if isinstance(queue, list):
        customer = l[0]
        l.remove(customer)
    elif isinstance(queue, deque):
        customer = queue.popleft()
    return customer


start = time()
get_next_customer(l)
elapsed = format(time() - start, "f")

print(f"get_next_customer(l) with {customer_count=} -> {elapsed}s")

start = time()
get_next_customer(sll)
elapsed = format(time() - start, "f")

print(f"get_next_customer(sll) with {customer_count=} -> {elapsed}s")
