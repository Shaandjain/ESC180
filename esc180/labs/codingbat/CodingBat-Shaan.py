def cigar_party(cigars, is_weekend):
  success = False
  if not is_weekend:
    if 40 <= cigars <= 60:
      success = True
  elif is_weekend:
    if 40 <= cigars:
      success = True
  return success

def date_fashion(you, date):
  
  result = 0

  if 2>= you or 2>= date:
    result = 0
  elif 8<= you or 8<= date:
    result = 2
  elif 2<you<8 or 2<date<8:
    result = 1
  return result

def squirrel_play(temp, is_summer):
    if is_summer:
        upper_limit = 100
    else:
        upper_limit = 90     
    return 60 <= temp <= upper_limit

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5 
    if speed <= 60:
        return 0 
    elif 61 <= speed <= 80:
        return 1  
    else:
        return 2 
    
def sorta_sum(a, b):
    total_sum = a + b
    if 10 <= total_sum <= 19:
        return 20
    else:
        return total_sum

def alarm_clock(day, vacation):
    is_weekend = day == 0 or day == 6
    
    if vacation:
        return "off" if is_weekend else "10:00"
    else:
        return "10:00" if is_weekend else "7:00"
    
def love6(a, b):
    return a == 6 or b == 6 or (a + b) == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10
    
def near_ten(num):
  remainder  = num % 10
  return remainder <= 2 or remainder >= 8
  
def count_evens(nums):
    return sum([not i % 2 for i in nums])

def big_diff(nums):
    return max(nums) - min(nums)

def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)

def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total


def sum67(nums):
  sum = 0 
  in67 = False
  for i in nums:
    if i ==6:
      in67 = True
    elif not in67:
      sum += i
    elif i == 7 and in67:
      in67 = False
  return sum

def has22(nums):
  has = False
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      has = True
  return has

def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):  
    return len(nums) >= 1 and nums[0] == nums[-1]

def make_pi():
    return [3, 1, 4]

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
    return sum(nums)

def rotate_left3(nums):
    return nums[1:] + nums[:1]

def reverse3(nums):
    return nums[::-1]

def max_end3(nums):
    return [max(nums[0], nums[-1])] * 3

def sum2(nums):
    return sum(nums[:2])

def middle_way(a, b):
    return [a[1], b[1]]

def make_ends(nums):
    return [nums[0], nums[-1]]

def has23(nums):
    return 2 in nums or 3 in nums

def sleep_in(weekday, vacation):
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

def sum_double(a, b):
    return a + b if a != b else 2 * (a + b)

def diff21(n):
    return 21 - n if n <= 21 else 2 * (n - 21)

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

def pos_neg(a, b, negative):
    return (a < 0 and b < 0) if negative else (a < 0 and b > 0) or (a > 0 and b < 0)

def not_string(str):
    return str if str[:3] == 'not' else 'not ' + str

def missing_char(str, n):
    return str[:n] + str[n+1:]

def front_back(str):
    return str[-1] + str[1:-1] + str[0] if len(str) > 1 else str

def front3(str):
    return str[:3] * 3

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