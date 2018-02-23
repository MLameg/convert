#Problem 1

#Part i: Reads a sentence from standard input
x = input("Please enter a sentence: ").lower()

#Part ii: Writes sentence in lower case
print(x)

#Part iii: Writes sentences with vowels in uppercase and consonants in lower case
case = x.replace("a", "A")
case = case.replace("e", "E")
case = case.replace("i", "I")
case = case.replace("o", "O")
case = case.replace("u", "U")
print(case)

#Part iv: Writes sentence in reverse
print(x[::-1])
