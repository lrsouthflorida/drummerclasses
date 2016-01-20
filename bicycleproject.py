
bikes = {black_bike:4, gold_bike:3, red_bike:2, silver_bike:5, purple_bike:1}
bikeshop = Bikeshops("Bikeshop",bikes,20/100)

customerone = Customers("Customerone",200)
customertwo = Customers("Customertwo",500)
customerthree = Customers("Customerthree",1000)




class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
    

class Bike_Shop(object):
    def __init__(self, name, bikes, cost_margin): 
        self.name = name
        self.cost_margin = cost_margin
        self.inventory = {}inventory
        self.profit = 0
        
        for bike in bikes:
            price = self.inventory[bike]*self.cost_margin
        
        
   
class Customers(object):
    bikesowned = []
    def __init__(self, name, customer_funds):
        self.name = name
        self.customer_funds = customer_funds
        
        


    
    
    
    
    
    
    
    
        
        
        
        
        