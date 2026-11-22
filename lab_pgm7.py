
import sys

string = sys.argv[1]

print("\nPalindrome Checking")
print("Given String:", string)

if string == string[::-1]:
    print("The given string is a Palindrome")
else:
    print("The given string is not a Palindrome")
