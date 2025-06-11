"""
If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
if __name__ == "__main__":
    my_range = range(1, 1000)
    results = []
    for i in my_range:
        if i % 3 == 0:
            results.append(i)
        elif i % 5 == 0:
            results.append(i)
        
    sum = 0
    for x in results:
        sum = sum + x
    print (str(sum))
