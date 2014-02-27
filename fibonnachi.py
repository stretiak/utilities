"""
Please enter a short description here. It could be useful:
 - for getting "a good habit"
 - english training
 - it is useful for studding too

"""


#just a note
# ';' are extra un Python
def fibonacci_recursion(n, num=0):
    if n >= 2:
        num = fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2);
    else:
        num = n
    return num;

print("Element under the number N in the Fibonacci series: ", fibonacci_recursion(8));

def fb(n, val=[1, 1]):
    """
    fibonacci_recursion 2
    val=[1, 1]  - warning is OK here
    """
    if n <= 0:
        return val
    val.append(val[-1] + val[-2])
    return fb(n - 1, val)

print fb(15)


def fib(n):

    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b
fib(200)

def fib_list(n):
    result = []
    a, b = 0, 1
    while b < n:
            result.append(b)
            a, b = b, a + b
    return result

print('\n')
print(fib_list(200))


def word_count(sentence):
    """
    Works correct.
    But very much complicated in implementation
    """
    sentence_new = ' '.join(sentence.split())
    index_gaps = []
    n = sentence.strip().split(" ")
    for j in range(0,len(sentence_new),1):
        n = sentence_new.find(" ", j, len(sentence_new))
        if n == j:
            index_gaps.append(n)
    return len(index_gaps) + 1

print(word_count("      The best   bbb       yy      1"))
print(word_count("          The          best picture          I've ever seen"))


def geometric_progression(a , q , n, series = []):
    """
    geometric_progression - sequence of numbers "a" ,
    in which each successive number, starting with the second,
    obtained from the previous by multiplying it by a certain number "q".
    a - members of the progression
    q - ratio of the progression
    n - number of members of the progression

    """
    if n == 1:
        series.append(a)
        return series
    series.append(a * pow(q, n - 1) )
    return geometric_progression(a, q, n - 1, series)

print(geometric_progression(1, 2, 10))

def GSD(x, y):
    """
    GSD - greatest common divisor of two integers
    x, y - natural numbers
    """
    if x == y:
        return x
    else:
        if x > y:
            return GSD(x - y, y)
        else:
            return GSD(x ,y - x)

print(GSD(25, 6))
print(GSD(30, 10))
print(GSD(99, 66))

