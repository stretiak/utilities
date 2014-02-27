def  increase(sentence, number_of_items):
    for i in range(0, number_of_items, 1):
            t = sentence[0:-1] + str(i) + sentence[-1]
            print(t)
    return t



#this is onle the test line for commit
#HE-heeeeeee

#increase("The best picture I've ever seen (copy)", 5)
#HHHHHHHHHH

def find_increase(sentence):
    first_copy = sentence.find("copy",1,len(sentence))
    number = int(sentence[(first_copy + len('copy')): -1])
    if number != 0:
        number += 1
        sentence = sentence[0:(first_copy + len('copy'))]+ str(number)+ sentence[-1]
    print(sentence)
    return sentence

find_increase("The best picture I've ever seen (copy14)")
