function table.print(table)
    for k, v in ipairs(table) do
        print(k, v)
    end
end

function bubble_sort(table)
    for i = 1, #table do
        for j = 1, #table - i do
            if table[j] > table[j+1] then
                table[j], table[j+1] = table[j+1], table[j]
            end
        end
    end
    return table
end


nums = {5,3,6,2,10}
table.print(nums)
sorted_nums = bubble_sort(nums)
table.print(sorted_nums)