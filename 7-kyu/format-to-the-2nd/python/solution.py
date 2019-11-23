def print_nums(*nums):
    if len(nums) == 0: return ""

    nums = map(str, nums)
    longest = max(map(len, nums))
    return "\n".join(map(lambda s: s.zfill(longest), nums))