import time
from collections import namedtuple

IndexWithAttempts = namedtuple("IndexWithAttempts", ["index", "attemptss"])


def tictoc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.6f}s to finish.")
        return result

    return wrapper


@tictoc
def binary_search(nums: list, num: int) -> IndexWithAttempts:
    start, end = 0, len(nums) - 1
    attempts = 0
    while start <= end:
        mid = (start + end) // 2
        guess = nums[mid]
        if guess == num:
            return IndexWithAttempts(mid, attempts)
        elif guess > num:
            attempts += 1
            end = mid - 1
        else:
            attempts += 1
            start = mid + 1
    return IndexWithAttempts(None, attempts)


@tictoc
def simple_search(nums: list, num: int) -> IndexWithAttempts:
    attempts = 0
    for idx, guess in enumerate(nums):
        attempts += 1
        if guess == num:
            return IndexWithAttempts(idx, attempts)
    return IndexWithAttempts(None, attempts)


if __name__ == "__main__":
    nums = [_ for _ in range(1, 15000001)]
    num = nums[-1]  # Testing for the worst case scenario here.
    bs_idx, bs_tries = binary_search(nums, num)
    ss_idx, ss_tries = simple_search(nums, num)
    if bs_idx is not None:
        print(f"Found {num:,} in {ss_idx=:,} in {ss_tries:,} attempts.")
        print(f"Found {num:,} in {bs_idx=:,} in {bs_tries:,} attempts.")
    else:
        print(f"Unable to find {num:,}, even after {ss_tries:,} attempts.")
        print(f"Unable to find {num:,}, even after {bs_tries:,} attempts.")
