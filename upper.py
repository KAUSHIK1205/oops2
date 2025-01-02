class upper:
    def __int__(self):
        self.str1=""

    def enter(self):
        self.str1= input("please enter a word:")

    def printf(self):
        print(  "result is :", self.str1.upper())
       
str1= upper()
str1.enter()
str1.printf()

