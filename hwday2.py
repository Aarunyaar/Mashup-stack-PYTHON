Receipt_Header="""RECEIPT"""

price = 450
book = "\n\tPython basics:  {}."
print(book.format(price))

price1 = 600
book1 = "\n\tData Science Intro: {}."
print(book1.format(price1))

total_price=price+price1
print("\n\tTotal Amount= {}".format(total_price))

message="\n\tTHANK YOU FOR SHOPPING!"
print(format(message))

receipt= Receipt_Header+book.format(price)+book1.format(price1)+"\n\tTotal Amount = {}".format(total_price)+message
print("\n\tFULL RECEIPT")
print(receipt)