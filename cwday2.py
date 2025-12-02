header = """\n\t*** BOOKSTORE RECEIPT ***
\t---------------------------"""

book1 = "Python Basics"
price1 = 450

book2 = "Data Science Intro"
price2 = 600

line1 = "\n\tBook: {}  -  ₹{}".format(book1, price1)
line2 = "\n\tBook: {}  -  ₹{}".format(book2, price2)

total = price1 + price2
total_line = "\n\tTOTAL: ₹{}".format(total)

thank_you = "\n\n\tThank you for shopping with us!"

receipt = header + line1 + line2 + total_line + thank_you

print(receipt.upper())
