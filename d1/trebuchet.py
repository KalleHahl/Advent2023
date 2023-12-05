from collections import deque
import re

strings = []



with open('trebuchet.txt', 'r') as file:
    for line in file:
        strings.append(line.strip())

def trebuchets(strings):
    number_strings = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    pattern = r"(zero|one|two|three|four|five|six|seven|eight|nine)"
    num_list = []
    strings = ['eightwo']
    for element in strings:
        right = False
        left = False
        word_right = ''
        word_left = ''
        num = deque([])
        for i in range(len(element)):
            if not left:
                if element[i].isdigit():
                    left = True
                    num.appendleft(element[i])
                else:
                    word_left += element[i]

                    reg = re.search(pattern, word_left)
                    if reg:
                        num.appendleft(number_strings[reg.group(1)])
                        left = True

            if not right:
                if element[-1-i].isdigit():
                    right = True
                    num.append(element[-1-i])
                else:
                    word_right += element[-1-i]
                    reg = re.search(pattern, word_right[::-1])
                    if reg:
                        num.append(number_strings[reg.group(1)])
                        right = True
            if right and left:
                break
        num_list.append(int(''.join(num)))
    print(num_list)
    return num_list



if __name__ == '__main__':
    print(sum(trebuchets(strings)))