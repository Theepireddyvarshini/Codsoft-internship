####                                  TO DO LIST             
l=[]
def options():
    print("\n------welcome to do list--------")
    print("1.check list")
    print("2.add to list")
    print("3.mark list")
    print("4.delete list")
    print("5.exit")
def checklist():
    if l:
        for i,task in enumerate(l,1):
            print(i,task,sep=".")
    else:
        print("list is empty")
def addtolist():
    b=input("add your task : ")
    l.append(b)
    print("task is added !")
def marklist():
    checklist()
    b=int(input("choose an option : "))
    if 0 <= b <= len(l):
        l[b-1] = l[b-1] + " ☑️ "
        print(f"You marked '{l[b-1]}' as done.")
    else:
        print("Invalid choice.")  
def deletetask():
    checklist()
    a=int(input("select a number: "))
    l.pop(a-1)
    print(" here is a updated list ")
    checklist()
def exit():
    print(" thank you !!! ")



while True:
    options()
    a=int(input("choose an option : "))
    if a==1:
        checklist()
    elif a==2:
        addtolist()
    elif a==3:
        marklist()
    elif a==4:
        deletetask()
    elif a==5:
        exit()
        break

        





