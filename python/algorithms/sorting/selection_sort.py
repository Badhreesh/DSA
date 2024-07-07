from random import sample
def get_smallest_num_idx(nums: list) -> int:
    smallest_num_idx = 0
    smallest_num = nums[0]
    for idx in range(1, len(nums)):
        if nums[idx] < smallest_num:
            smallest_num_idx = idx
            smallest_num = nums[idx]
    return smallest_num_idx

# selection sort is an inplace algorithm.
# todo: Adjust the code accordingly once you learn how to!
def selection_sort(nums: list) -> list:
    sorted_nums = []
    copied_nums = list(nums)
    for _ in range(len(copied_nums)):
        smallest_num_idx: int = get_smallest_num_idx(copied_nums)
        sorted_nums.append(copied_nums.pop(smallest_num_idx))
    return sorted_nums


if __name__ == "__main__":
    nums = [5, 3, 6, 2, 10]
    # nums = sample(range(1, 101), 20)
    sorted_nums = selection_sort(nums)
    print(nums)
    print(sorted_nums)
