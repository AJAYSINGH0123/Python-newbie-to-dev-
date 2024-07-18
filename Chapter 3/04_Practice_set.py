# problem statement 1
a = input("enter the name of the user: ")
print(f"Good afternoon {a} ")

# Problem Statement 2

""" b = input("Enter the name of the applicant: ")
    date = int(input("enter date on letter: "))
    print("Letter Template\n Dear", b, "\n You are selected\nDate: ", date)   """

# Problem statement 2:-

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Ajay").replace("<|Date|>", "18 July 2024"))


