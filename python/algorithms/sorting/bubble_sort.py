from random import randint
from time import time

def bubble_sort(nums: list) -> list:
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                # print(nums)
    return nums


if __name__ == "__main__":
    nums = [37, 29, 47, 8]
    nums = [randint(1, 10000) for _ in range(10000)]
    # print(nums)
    start = time()
    sorted_nums = bubble_sort(nums)
    print(time() - start)

    start = time()
    sorted_nums = sorted(nums)
    print(time() - start)
    # print(sorted_nums)