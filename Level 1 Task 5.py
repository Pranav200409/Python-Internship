def palindrome_checker(str):
    return str == str[::-1]

user_input = input("Enter your string:")
if palindrome_checker(user_input):
    print(f"{user_input} is a palindrome .")
else :
    print(f"{user_input} is not a palindrome.")