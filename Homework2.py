#Exercise 2 - Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and 
# print_String print the string in upper case

class Str:
    def __init__(self):
        self.str1=""
        
    def get_str(self):
        self.str1=input("String: ")
    
    def print_str(self):
        p=self.str1.upper()
        print(p)
        
str=Str()
str.get_str()
str.print_str()
        
