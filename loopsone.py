my_list=["anish", "shushant", "rajib", "rupon", "polash"]
letter_to_check= input("what letter should we check")
for item in my_list:
     if item[0]== letter_to_check:
          print(item)
     else:
           print("nothing with that letter")
           
