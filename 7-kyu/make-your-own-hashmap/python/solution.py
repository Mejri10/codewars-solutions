from collections import defaultdict

def my_hash_map(list_of_strings):
    ans = defaultdict(list)
    for string in list_of_strings:
        ans[custom_hash(string)].append(string)
    return ans
    
def custom_hash(string):
    return sum(map(ord, string))