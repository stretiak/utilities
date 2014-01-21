# -*- coding: utf-8 -*-

# read_file - считывает из заданного файла строку с заданным номеро
def read_file(name_file, number_rows):
    file = open(name_file)
    for i in range(0, number_rows, 1):
        all_text = file.readline()
    return all_text

#read_file("some_name.txt", 8)

# read_file_all - считывает файл целиком
def read_file_all(name_file):
    file = open(name_file)
    all_text = []
    all_text.append(file.read())
    #print(all_text)
    return all_text

# read_file_all("some_name.txt")


#just an example
def read_file_as_list(name_file):
    """
    @param: name_file - input file name.
    @raise: Exception - in case file doesn't exist
    @return: (list) of strings - File content
    """
    file = open(name_file)
    if not file:
        raise Exception("Cannot open file '{}'".format(name_file))
    return file.readlines()


#counter_spaces - подсчитывает колличество пробелов в заданной строке
def counter_spaces(case):
    index_gaps = []
    sentence = case[0]
    n = sentence.find(" ", 0, len(sentence))
    while n >= 0:
        j = n + 1
        index_gaps.append(n)
        n = sentence.find(" ", j, len(sentence))
    #print(index_gaps)
    return index_gaps

#counter_spaces(read_file_all("some_name.txt"))

#counter_spaces_for - подсчитывает колличество пробелов в заданной строке
def counter_spaces_for(sentence):
    index_gaps = []
    for j in range(0, len(sentence), 1):
        n = sentence.find(" ", j, len(sentence))
        if n == j:
            index_gaps.append(n)
    #print(index_gaps)
    return len(index_gaps)

#counter_spaces_for("The best picture I've ever seen")

#counter_spaces_while - подсчитывает колличество пробелов в заданной строке
def counter_spaces_while(sentence):
    index_gaps = []
    n = 1
    while True:
        n = sentence.find(" ", n, len(sentence))
        if n == -1:
            break
        if n != 0:
            index_gaps.append(n)
        n += 1
    #print(index_gaps)
    return len(index_gaps)

#counter_spaces_while("The best picture I've ever seen")

#counter_spaces_split - подсчитывает колличество пробелов в заданной строке
def counter_spaces_split(sentence):
    n = sentence.split(" ")
    #print(len(n)-1)
    return len(n)-1

#counter_spaces_split - подсчитывает колличество пробелов в заданной строке
def counter_spaces_split_print(sentence):
    n = sentence.strip().split(" ")
    for v in n:
        print( "{}".format(v))

    n = filter(lambda x: x != '', n)
    return len(n)-1


def counter_words_in_string(sentence):
    #проверка что входной параметр задан и имет правильный тип (str)
    #иначе подставляется такое значение входного параметра которое в итоге вернет 0
    sentence = sentence if sentence and isinstance(sentence, str) else ''

    return len(                         #нас интересует только количество элементов
        filter(                         #выполнить проверку функцией (первый аргумент - тут lambda) для каждого элемента после разбития
            lambda x: x != '',          #проверить не пустой ли элемент получается при разбитии
            sentence.strip().           #удалить начельные и конечные пробелы (здесь - не обязательно)
                split(" ")))            #разбить по пробелам





#counter_spaces_split("The best picture I've ever seen")

#counter_spaces_recursion - подсчитывает колличество пробелов в заданной строке
def _counter_spaces_recursion(sentence, count):
    n = sentence.find(" ", 1, len(sentence))
    if n == -1:
        exit()  #ERRRRORRR!!!!!!!  return (count)

    new_sentence = sentence[n:]
    count += 1
    #print("COUNT = ", count)
    return counter_spaces_recursion(new_sentence,count)


def counter_spaces_recursion(sentence, count=0):
    n = sentence.find(" ", 1, len(sentence))
    if n == -1:
        print "return %s" % count
        return count
    return counter_spaces_recursion(sentence[n:], count + 1)

counter_spaces_recursion("The best picture I've ever seen", count=0)


#file_gaps - подсчитывает колличество пробелов в заданном файле
def file_gaps(name_file):
    gaps_list = counter_spaces(read_file_all(name_file))
    print("Колличество пробелов в файле: ", len(gaps_list))
    return len(gaps_list)

file_gaps("some_name.txt")


if __name__ == '__main__':
    print counter_spaces_split("hehe haha mumu fufuf")
    print counter_spaces_split("hehe haha      mumu fufuf   ")
    print counter_spaces_split_print("hehe haha    mumu fufuf   ")
    print counter_words_in_string("   hehe haha    mumu fufuf   ")
    print counter_words_in_string(None)
    print counter_words_in_string({'a': 200})

    print counter_spaces_recursion("The best picture I've ever seen")