def emailslicer():
    ''' Email slicer
'''

    username=email_id[:email_id.index('@')]
    domainname=email_id[email_id.index('@')+1:]
    print("Your username is:" ,username ,"\nAnd your domain name is:",domainname.upper())
   

print(emailslicer.__doc__)

while True:
    email_id=input("Enter your email id: ")
    if '@' in email_id:
        emailslicer()
    elif '@' not in email_id:
        print("Please enter valid email adress")
    

    exit=input("Do you want to enter another Email address: YES or NO")
    if exit=="no":
        print("Thank you")
        break
   
        

