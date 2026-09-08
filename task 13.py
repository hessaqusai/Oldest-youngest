print("Welcome to the Library Membership Eligibility Checker!")
print("To be eligible, you must meet at least one of the following:")
print("- Be between 7 and 18 years old")
print("- Have read more than 5 books last year")
name=input("Enter your name:")
year=int(input("Enter your birth year:"))
books=int(input("Enter the number of books you read last year:"))
age=year-2026
if age>=7 and age<=18:
    print(name, "your age is", age," the number of books you read is", books,"books, you are eligible for the membership")
if books>5:
    print(name, "your age is", age," the number of books you read is", books,"books, you are eligible for the membership")
else:
    print(name, "your age is", age," the number of books you read is", books,"books, you are not eligible for the membership")
