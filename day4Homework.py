#Turn the shopping cart program from yesterday into an object-oriented program
class ShoppingList():
    
    def __init__(self):
        self.items={"sugar":4,
                    "apple":2}
        
    
    def add_item(self,item,quantity):
      
        if item in self.items:
            self.items[item]+=quantity 
        else:
            self.items[item]=quantity
            
        print(f" {quantity} {item} added ")
        
    
    def remove_item(self,item):
        if item in self.items:
            del self.items[item]
            print(f" {item} removed")
        else:
            print(f" {item} is not in the list")
            
        print(f" Remain {item} ")
           
    def view_list(self):
        print("shopping list")
        for item in self.items:
           # print(f" self.items {item} ")
            print(f"{self.items[item]} {item}")
            
   
            
class list1:
    def __init__(self):
        
        self.shoppingList=ShoppingList()
        
    def run(self):
        while True:
            print("1- Add item to shopping list")
            print("2- remove item from the list")
            print("3- view shopping list")
            print("4- quit")
            
            choice=input("enter your choice : ")
            
            if choice=="1":
                item=input("enter item to add : ")
                quantity=int(input("enter quantity : "))
                self.shoppingList.add_item(item,quantity)
                
            elif choice=="2":
                item=input("enter item to remove : ")
                self.shoppingList.remove_item(item)
                
            elif choice=="3":
                self.shoppingList.view_list()
                
            elif choice=="4":
                print(" quit ")
                
            else:
                print(" invalid choice ")
                
                self.shoppingList.view_list()
        
call=list1()
call.run()
   
            
        
        
        
        