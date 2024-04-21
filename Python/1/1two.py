#Day 1: Trebuchet?!
#--Part Two--
def tokenize(string):
    word_to_digit = {"one": 1,
                 "two": 2,
                 "three": 3,
                 "four": 4,
                 "five": 5,
                 "six": 6,
                 "seven": 7,
                 "eight": 8,
                 "nine": 9,
                 "zero": 0}
    
    answer_list = []
    word = ""
# SAMPLE INPUT: sevenoneqbfzntsix55
    for character in string:
        if word.lower() in word_to_digit:
            answer_list.append(word_to_digit[word.lower()])
            word = ""
        if character.isdigit(): 
            answer_list.append(character)
            # print("The answer list:", answer_list)
            # print("The word value:", word)
        if character.isalpha():
            word += character

    for i in range(len(answer_list)):
        answer_list[i] = int(answer_list[i])
        #print("The answer list is:", answer_list)
    return answer_list

# test_sum = 0
# test_string = ["fIvE72"]
# for index in test_string:
#     list_of_digits = tokenize(index)
#     print(list_of_digits)
#     print(list_of_digits[0],"and", list_of_digits[-1])
#     test_sum += list_of_digits[0]*10 + list_of_digits[-1]
# print("test sum is:", test_sum)

sum = 0;
with open("test1two.txt", "r") as f:
#with open("input.txt", "r") as f:
    for line in f:
        list_of_digits = tokenize(line)
        print(list_of_digits[0],"and", list_of_digits[-1])
        sum += list_of_digits[0]*10 + list_of_digits[-1]

print("The sum is:", sum)


