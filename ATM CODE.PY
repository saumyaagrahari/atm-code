print ("Welcome To SBI Bank")
Bankname= input("enter the bank name:")
if Bankname=="SBI":
    print("correct name")
    card=input("enter the card name:")
    if card=="ATM card":
         print("correct code")
         language=input("enter the language:")
         if language==("Hindi" and "English"):
            print ("correct language")
            PIN=int(input("enter the pin:"))
            if PIN>=1 or PIN<=9:
                print("correct pin number")
                password=int(input("enter the password:"))
                if password>=1 or password<=9:
                    print("correct password")
                    tran=input("enter the tran of transaction:")
                    if tran==("cash withdrawal"):
                        print("select type of account")
                        type=(input("enter type of account:"))
                        if type==("current amount") or ("saving amount"):
                            print("enter the withdrawal amount")
                            balance=int(input("enter the balance:"))
                            if balance>=10000:
                                print("correct balance")
                                num=input("Did you colleced your cash:")
                                if num==("yes"):
                                    print("Take a printed receipt,if needed")
                                else:
                                    print("no,i dident collected my cash")
                            else:
                                print("not sufficient balance")
                        else:
                            print("this type is not detected")                
                    else:
                        print("this transaction was not detected")
                else:
                    print("wrong password")
            else:
                print("wrong pin")       
         else:
            print("sorry,this language is not available")         
    else:
            print("sorry,your card was not detected")
else:
    print("error")
     
print("Thanks")