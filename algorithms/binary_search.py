def binary_search(nums: list, num: int) -> tuple[int | None, int]:
    min_idx, max_idx = 0, len(nums) - 1
    count = 0
    while min_idx <= max_idx:
        count += 1
        mid_idx = (min_idx + max_idx) // 2
        guess = nums[mid_idx]
        if guess == num:
            return mid_idx, count
        elif guess > num:
            max_idx = mid_idx - 1
        else:
            min_idx = mid_idx + 1
    return None, count

def simple_search(nums: list, num: int) -> tuple[int | None, int]:
    count = 0
    for idx, guess in enumerate(nums):
        count += 1
        if guess == num:
            return idx, count
    return None, count


if __name__ == "__main__":
    nums = [_ for _ in range(1, 129)]
    num = nums[-1]
    bs_idx, bs_tries = binary_search(nums, num)
    ss_idx, ss_tries = simple_search(nums, num)
    if bs_idx is not None:
        print(f"Found {num} in {ss_idx=} in {ss_tries} guesses")
        print(f"Found {num} in {bs_idx=} in {bs_tries} guesses")
    else:
        print(f"Unable to find {num}, even after {ss_tries} attempts")
        print(f"Unable to find {num}, even after {bs_tries} attempts")
