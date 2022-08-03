"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""
def main_problem1():
    total = 0
    number_to_sum = 1000
    for i in range(number_to_sum):
        if i%3 == 0 or i %5 ==0:
            total +=1
            print(total)
main_problem1()