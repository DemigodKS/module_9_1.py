
def min_function(args):
    res = min(args)
    return res

def max_function(args):
    res = max(args)
    return res

def len_function(args):
    res = len(args)
    return res

def sum_function(args):
    res = 0
    for i in args:
        res += i
    return res

def sort_function(args):
    res = sorted(args)
    return res

def apply_all_func(int_list, *functions):
    results = {}
    for i in functions:
        results[i.__name__]= i(int_list)
    return results

print(apply_all_func([2, 4, 5, 6], max, min))
print(apply_all_func([6, 8, 3, 2, 5], len, sum, sorted))










