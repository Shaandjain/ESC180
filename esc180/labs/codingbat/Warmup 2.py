def string_times(str, n):
    return str * n

def front_times(str, n):
    return str[:3] * n

def string_bits(str):
    return str[::2]

def string_splosion(str):
    return ''.join([str[:i] for i in range(1, len(str) + 1)])

def last2(str):
    return sum([str[i:i+2] == str[-2:] for i in range(len(str) - 2)])

def array_count9(nums):
    return nums.count(9)

def array_front9(nums):
    return 9 in nums[:4]

def array123(nums):
    return 1 in nums and 2 in nums and 3 in nums

def string_match(a, b):
    return sum([a[i:i+2] == b[i:i+2] for i in range(len(a) - 1)])


