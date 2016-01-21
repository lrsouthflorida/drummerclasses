
bikes = {"black_bike:4", "gold_bike:3", "red_bike:2", "silver_bike:5", "purple_bike:1"}
bikeshop = Bike_Shop("Bikeshop",bikes,20/100)

customerone = Customers("Customerone",200) # added info to included customers budgets.py
customertwo = Customers("Customertwo",500)
customerthree = Customers("Customerthree",1000)

allcustomers = []
afforablebikes = {}


class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
    

class Bike_Shop(object):
    def __init__(self, name, bikes, cost_margin): 
        self.name = name
        self.cost_margin = cost_margin
        self.inventory = {}
        self.profit = 0
        
        for bike in bikes:
            price = self.inventory[bike]*self.cost_margin
        
    def sell(self, bike, customer): #Formula for proift that 
            self.profit += int(self.inventory[bike]["price"]-(self.inventory[bike]["price"]/self.margin))
            customer.bikesowned.append(bike)
            customer.fund -= self.inventory[bike]["price"]
            self.inventory[bike]["amount"] -=1
        
   
class Customers(object):
    bikesowned = []
    def __init__(self, name, customer_funds):
        self.name = name
        self.customer_funds = customer_funds
       
def find_customers_bikes(): # get customers and bikes they can afford.
    for obj in gc.get_objects():
        if isinstance(obj, Customers):
                allcustomers.append(obj)

    for customer in allcustomers #helps find the customer afforable bikes
        afforablebikes[customer.name] = []
        for bike in bikeshop.inventory:
                if customer.customer_funds >= bikeshop.inventory[bike]["price"]:
                    afforablebikes[customer.name].append(bike)
    
    print ("The afforable bikes are %s") % afforablebikes
    
find_customers_bikes()    
    
def print_inventory(): #prints out the inventory 
    print bike.shop.inventory
    
print_inventory()    

    
def inventory_profit(): # function for inventory profit
    inventory_clean = {}
    for key in bikeshop.inventory:
            inventory_clean[key.name]=bikeshop.inventory[key]
    print inventory_clean
    
inventory_profit()    
    
    
    
    
        
        
        
        
        