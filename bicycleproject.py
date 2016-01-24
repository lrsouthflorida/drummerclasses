# bikes = {"black_bike":"4", "gold_bike":"3", "red_bike":"2", "silver_bike":"5", "purple_bike":"1"}
# bikeshop = Bike_Shop("Bikeshop",bikes,20/100)

# customerone = Customers("Customerone",200) # added info to included customers budgets.py
# customertwo = Customers("Customertwo",500)
# customerthree = Customers("Customerthree",1000)

# allcustomers = []
# afforablebikes = {}


class Bicycle(object):
    def __init__(self, name, weight, cost_of_produce, selling_price = 0):
        self.name = name
        self.weight = weight
        self.cost_of_produce = cost_of_produce
        self.selling_price = selling_price 
        
    

class BikeShop(object):
    def __init__(self, name, cost_margin, inventory = []): 
        self.name = name
        self.cost_margin = cost_margin
        self.inventory = inventory
        self.profit = 0
        
            
        
    def sell(self, bicycle, customer):
            selling_price = (self.cost_margin * bicycle.cost_of_produce/100) + bicycle.cost_of_produce
            self.profit = selling_price - bicycle.cost_of_produce 
            customer.bikesowned.append(bicycle)
            bicycle.selling_price = selling_price
            customer.customer_funds -= bicycle.selling_price
            self.inventory.remove(bicycle)
   
class Customer(object):
    def __init__(self, name, customer_funds, bikesowned = []):
        self.name = name
        self.customer_funds = customer_funds
        self.bikesowned = bikesowned
       
    def buy_bike(self, bicycle):
        if self.customer_funds > bicycle.selling_price:
            self.bikesowned.append(bicycle)
            self.customer_funds -= bicycle.selling_price 
        elif bicycle.selling_price <= self.customer_funds:
            print(bicycle.name)
        else:
            print("Sorry that you cannot afford the bikes.")
            
if __name__ == '__main__':       
   Cyclone = Bicycle(15,80,100,'Cyclone')   

   Warhawk = Bicycle(25,120,140,'Warhawk')

   Flash = Bicycle(12,100,130,'Flash')

   Starfire = Bicycle(22,110,135,'Starfire')

   Bulleteer = Bicycle(14,90,110,'Bulleteer')
   
   Supernova = Supernova(20,130,150,'Supernova')
   
   Donald  = Customer(1000,'Warhawk','Donald')
   
   Hilliary = Customer(500, 'Supernova', 'Hilliary')
   
   Bernie = Customer(200, 'Cyclone', 'Bernie')
   
   

    
   
  
    
    

    
    
   
    
    
    
    
        
        
        
        
        