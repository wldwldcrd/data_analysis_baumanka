def check_nums(nums, result):
    pos = []
    if (result == 0):
        return []
    for num in nums:
        if num[2]:
            if num[0] < result:
                sub_pos = check_nums(nums[num[1]+1:], result-num[0])
                if sub_pos:
                    pos.append(num[1])
                    pos.append(sub_pos)
            elif num[0] == result:
                pos.append(num[1])
    return pos


nums = [2, 3, 4, 11, 15]
result = 9

nums = [nums, [x for x in range(len(nums))], [1]*len(nums)]
nums = list(map(list, zip(*nums)))

pos = check_nums(nums, result)
print(pos)

# if result > sum(nums):
#     print("Error: Result > sum(nums)")
