# Source - https://stackoverflow.com/a/43612128
# Posted by Pozeidon, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-22, License - CC BY-SA 3.0

import math


def initial_data(number):
    count = 0
    goree = number - 1
    floor = number // 2
    while goree % 2 == 0:
        goree //= 2
        count += 1
    results = [goree, count]
    return results


def test_values(num):
  test_vals = []
  if num < 2047:
    test_vals = [2]
  elif num < 1373653:
    test_vals = [2, 3]
  elif num < 9080191:
    test_vals = [31, 73]
  elif num < 25326001:
    test_vals = [2, 3, 5]
  elif num < 3215031751:
    test_vals = [2, 3, 5, 7]
  elif num < 4759123141:
    test_vals = [2, 7, 61]
  elif num < 1122004669633:
    test_vals = [2, 13, 23, 1662803]
  elif num < 2152302898747:
    test_vals = [2, 3, 5, 7, 11]
  elif num < 3474749660383:
    test_vals = [2, 3, 5, 7, 11, 13]
  elif num < 341550071728321:
    test_vals = [2, 3, 5, 7, 11, 13, 17]
  elif num < 3825123056546413051:
    test_vals = [2, 3, 5, 7, 11, 13, 17, 19, 23]
  elif num < 2**64:
    test_vals = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
  elif num < 318665857834031151167461:
    test_vals = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
  elif num < 3317044064679887385961981:
    test_vals = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
  return test_vals


def rabin_miller(num):
    base_primes= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                   101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                   199, 211, 223, 227, 229, 233, 239,241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                   317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
                   457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521,523, 541, 547, 557, 563, 569, 571, 577, 587,
                   593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,673, 677, 683, 691, 701, 709,
                   719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853,
                   857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
                   997]
  
    if num <= 1:
        return False
    elif num in base_primes:
        return True
    else:
        for value in base_primes:
            if num % value == 0:
                return False
        data = initial_data(num)
        s = data[1]
        d = data[0]
        testing_values = test_values(num)
        if not testing_values:
            testing_values = [2, min(num - 1, int(2 * (math.log1p(num - 1)) ** 2))]
        for a in testing_values:
            if a % num == 0:
                continue
            x = pow(a, d, num)
            if x == 1 or x == num - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, num)
                if x == num - 1:
                    break
            else:
                return False
        return True