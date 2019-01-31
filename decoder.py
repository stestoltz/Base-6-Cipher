import random
import string

text = open("code.txt").read()

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


def base_26_to_base_10(n):
    result = string.ascii_lowercase.index(n[0]) * 26 + string.ascii_lowercase.index(n[1])

    result = str(result)

    if len(result) == 2:
        result = "0" + result
    elif len(result) == 1:
        result = "00" + result
    elif not result:
        result = "000"

    return result


def base_6_to_base_10(n):
    return int(n[0]) * 6 + int(n[1])

sets_of_chars = text.split(" ")

print(sets_of_chars)

triplets = []

for each in sets_of_chars:
    triplets.append(base_26_to_base_10(each))

code = "".join(triplets)

print(code)

index = 2

output = ""

while index <= len(code):
    output += chars[base_6_to_base_10(code[index - 2:index])]
    index += 2

with open("decoded.txt", "w") as text_file:
    print(output, file=text_file, end="")