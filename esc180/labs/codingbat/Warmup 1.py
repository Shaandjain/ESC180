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

