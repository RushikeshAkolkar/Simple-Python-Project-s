import re
email = input("Enter Your Mail Id : ")
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}"
if re.search(email_condition, email):
    print("Right Email.")
else:
    print("Wrong Email.")