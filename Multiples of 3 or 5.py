"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

"""
Solution1 - Brute Force
Check all numbers below 1000 - if divisible by 3 or 5, add to sum
"""
# sum_res = 0
# for i in range (1,1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sum_res += i
# print(sum_res)

"""
Solution2 - Mathematical
Sum of multiples of 3 + sum of multiples of 5 - sum of multiples of 15
"""
tar = 1000

def sum_div_by(div):
    n = int((tar - 1)/div)
    return div * n * (n+1) / 2

print(sum_div_by(3) + sum_div_by(5) - sum_div_by(15))
