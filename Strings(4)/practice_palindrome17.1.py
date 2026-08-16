# Take a user input string and check if it is a palindrome (same forwards and backwards).
# palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. Spaces, punctuation marks, and capital letters are typically ignored when checking a phrase.

string = "abccba"

if(string == string[::-1]):
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")
    
    
    
string1 = "harry is a good educator"

if(string1 == string1[::-1]):
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")
    
