import re
def valid_email(email):
    email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    if re.search(email_condition,email):
        return True
    else :
        return False

print("\t\t\tEmail Validator")

while True:
    email = input("Enter an email address to check:").strip()
    if valid_email (email):
        print(f"{email} is a valid email address.")
    else :
        print(f"{email} is unvalid email address")

    choice = input("Do you want to continue ? (Yes to CONTINUE , no to EXIT):").strip().lower()
    if choice != 'yes':
        print("EXITING .... thankyou!!!")
        break