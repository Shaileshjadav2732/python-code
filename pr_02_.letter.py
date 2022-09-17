letter='''Dear <|NAME|>,
greeting from ABC coding house.Iam happy to tell you about your selection
you are selected!
have a great day
Date: <|DATE|>
'''
name=input("enter Your name\n")
date=input("enter date:\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
