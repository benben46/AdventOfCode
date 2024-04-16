#Day 1: Trebuchet?!
#--Part Two--
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

def tokenize(string):
    answer_list = []
    word = ""

    for character in string:
        if character.isdigit(): 
            answer_list.append(character)
            if word.lower() in word_to_digit:
                answer_list.append(word_to_digit[word])
                word = ""
        if character.isalpha():
            word += character

    for i in range(len(answer_list)):
        answer_list[i] = int(answer_list[i])
    print(answer_list)
    return answer_list


sum = 0;
with open("test1two.txt", "r") as f:
#with open("input.txt", "r") as f:
    for line in f:
        list_of_digits = tokenize(line)
        sum += list_of_digits[0]*10 + list_of_digits[-1]

print("The sum is:", sum)


