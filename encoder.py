import random
import string

text = open("plaintext.txt").read()

#chars = "abcdefghijklmnopqrstuvwxyz*.,?!()- \n"
chars = "(stephn)a*dowjzr.b\nm,uvklc ?qig!fyx-"

def base_10_to_base_6(n):
    s = ""
    while n:
        s = str(n % 6) + s
        n //= 6

    if len(s) == 1:
        s = "0" + s

    if not s:
        return "00"

    return s


def base_10_to_base_26(n):
    s = ""
    while n:
        s = string.ascii_lowercase[n % 26] + s
        n //= 26

    if len(s) == 1:
        s = "a" + s

    if not s:
        return "aa"

    return s

print(text)

result = ""

for letter in text:
    letter = letter.lower()

    if letter not in chars:
        letter = "*"

    coded_char = base_10_to_base_6(chars.index(letter.lower()))

    print(letter + ": " + coded_char + " : " + chars[int(coded_char, 6)])

    result += coded_char

len_diff = len(result) % 3

if len_diff != 0:
    result += (3 - len_diff) * str(random.randint(0, 5))

print(str(len(result)) + " " + result)

sets_of_3 = []

index = 3

while index <= len(result):
    sets_of_3.append(result[index - 3:index])
    index += 3

print(sets_of_3)

sets_of_letters = []

for set_of_3 in sets_of_3:
    sets_of_letters.append(base_10_to_base_26(int(set_of_3)))

print(sets_of_letters)

with open("code.txt", "w") as text_file:
    print(" ".join(sets_of_letters), file=text_file, end="")
