class emp:

    def __init__(self):
        print("empoyeee created")

    def __del__(self):
        print("destructor")

    def cobj():
        print("obj started")
        obj=emp()
        print("functon end")
        return obj
    
print("calling cobj func")
obj=emp.cobj()
print("program ended")


