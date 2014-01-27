def fibonacci_recursion(n, num=0):
    if n >= 2:
        num = fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2);
    else:
        num = n
    return num;

print("Element under the number N in the Fibonacci series: ", fibonacci_recursion(8));

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
    sentence_new = ' '.join(sentence.split())
    index_gaps = []
    n = sentence.strip().split(" ")
    for j in range(0,len(sentence_new),1):
        n = sentence_new.find(" ", j, len(sentence_new))
        if n == j:
            index_gaps.append(n)
    return len(index_gaps) + 1

print(word_count("      The best   bbb             "))
print(word_count("          The          best picture          I've ever seen"))




