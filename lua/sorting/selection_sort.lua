function table.print(nums)
    for k, v in ipairs(nums) do
        print(k, v)
    end
end

function table.copy(nums)
    new_table = {}
    for k, v in ipairs(nums) do
        new_table[k] = v
    end
    return new_table
end

function get_smallest_idx(nums)
    smallest_idx, smallest_num = 1, nums[1]
    for idx = 2, #nums do
        if nums[idx] < smallest_num then
            smallest_idx = idx
            smallest_num = nums[idx]
        end
    end
    return smallest_idx
end

-- selection sort is an inplace algorithm.
-- todo: Adjust the code accordingly once you learn how to!
function selection_sort(nums)
    sorted_nums = {}
    copied_nums = table.copy(nums)
    for i = 1, #copied_nums do
        smallest_idx = get_smallest_idx(copied_nums)
        smallest_num = table.remove(copied_nums, smallest_idx)
        table.insert(sorted_nums, smallest_num)
    end
    return sorted_nums
end


nums = {5,3,6,2,10}
table.print(nums)
sorted_nums = selection_sort(nums)
print()
table.print(sorted_nums)
