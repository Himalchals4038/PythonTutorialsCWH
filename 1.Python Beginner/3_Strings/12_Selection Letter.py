letter = '''Dear <|Name|>
Greetings from IIT Bombay, 
You are selected in JEE Advanced 2022 !
Thanks And Regards
Head-In-Charge
Date: <|Date|>'''

Name = input("Enter you Name: ")
Date = input("Enter the Date: ")
letter = letter.replace("<|Name|>", Name)
letter = letter.replace("<|Date|>", Date)

print(letter)