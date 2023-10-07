from collections import deque as de
import random as rd

class Barack:
    def __init__(self):
        self.workers = de([])

    def workers_count(self):
        return len(self.workers)
    
    def add_worker(self, worker):
        self.workers.append(worker)


    def send_worker(self): # remove a worker and return it. it removes from the left with index 0
        return self.workers.popleft()



class Worker: # this class contains information about the worker
    def __init__(self):
        self.vitality = 100

    def increase(self, numb): # here increase the vitality of the worker
        pass

    def shrink(self, float): # this method shrink the vitality of a worker
        pass


    def check_die(self, point): # checks if the worker has vitality == 0
        pass

    def get_livskraft(self):
        return self.vitality



class Dining_room: # here eats the workers
    def __init__(self, from_barack, to_barack, from_warehouse):
        self._from_barack = from_barack #from which barack the worker will be recieved from
        self._from_warehouse = from_warehouse #from which warehouse the food should be brought from
        self._to_barack = to_barack # to which barack should the worker be send to?

    def set_to_barack(self, to_barack):
        self._to_barack = to_barack

    def set_from_barack(self,from_barack):
        self._from_barack = from_barack

    def set_from_warehouse(self, from_warehouse):
        self._from_warehouse = from_warehouse

    def check_food(self): # checks if there are food in warehouse
        return self._from_warehouse.get_count() >= 1

    def _check_worker(self): #checks if there are workers in barack
        return self._from_barack.workers_count() >= 1
    
    def _check_address(self):
        return (self._from_barack and self._from_warehouse and self._to_barack) != None
    
    def start_eating(self):
        pass


class Food:
    def __init__(self):
        self.quality = None

    def random_quality(self): # gives a random quality 
        self.quality = rd.randrange(-40, 50)

    def get_quality(self):
        return self.quality


class Warehouse:
    def __init__(self):
        self.food = de([])

    def recieve_food(self, food):
        self.food.append(food)

    def send_food(self):
        return self.food.popleft() # removes food from left and return that specific food

    def get_count(self):
        return len(self.food)



class Field: # a place where workers work to make some food
    def __init__(self, from_barack, to_barack, to_warehouse):
        self._from_barack = from_barack #from which barack the worker will be recieved from
        self._to_warehouse = to_warehouse #to which warehouse the food should be sent to
        self._to_barack = to_barack # to which barack should the worker be sent to?

    def set_to_barack(self, barack):
        self._to_warehouse = barack

    def set_to_warehouse(self, warehouse):
        self._to_warehouse = warehouse

    def set_from_barack(self, barack):
        self._from_barack = barack

    def _check_worker(self): #check if there are workers in barack
        return self._from_barack.workers_count() >= 1

    def _check_address(self):
        value = None
        if (self._from_barack and self._to_warehouse and self._to_barack) != None:
            value = True

        else:
            value = False

        return value

    def produce(self): # here starts the production of the food
        pass


class Home: # a place where workers get some rest or even marry
    def __init__(self, from_barack, to_barack, from_inventory):
        self._from_barack = from_barack #from which barack the worker will be recieved from
        self._to_barack = to_barack # to which barack should the worker be sent to?
        self._from_inventory = from_inventory #from which inventory we will take/ recieve a product
        self._house_type = None

    def set_to_barack(self, barack):
        self._to_barack = barack

    def set_from_barack(self, barack):
        self._from_barack = barack

    def set_from_inventory(self, inventory):
        self._from_inventory = inventory

    def set_house_type(self): # determine if this house is for marrage or for usual sleeping
        self._house_type = rd.choice(['sleep', 'marry'])

    def check_produkt(self):
        return self._from_inventory.get_count() >= 1

    def _check_worker(self,house_type):
        if house_type =='sleep':
            return self._from_barack.workers_count() >= 1 # if it is for sleeping so only one worker is needed in the home/room 
        
        else:
            return self._from_barack.workers_count() >= 2 # if it is for marrage it needs two workers to get married home

    def _check_adress(self): #checks if all addresses exist
        value = None
        if (self._from_barack and self._from_inventory and self._to_barack) != None:
            value = True

        else:
            value = False

        return value
    
    def start_home(self):
        pass 



class Inventory:
    def __init__(self):
        self._products = []

    def get_count(self):
        return len(self._products)
    
    def recieve_product(self, product):
        self._products.append(product)
        
    def send_product(self):
        return self._products.pop()



class Factory:
    def __init__(self, from_barack, to_barack, to_inventory):
        self._from_barack = from_barack #from which barack the worker will be recieved from.
        self._to_barack = to_barack # to which barack should the worker be sent to?.
        self._to_inventory = to_inventory # to which inventory we should send the product.
    

    def set_to_barack(self, barack):
        self._to_barack = barack

    def set_from_barack(self, barack):
        self._from_barack = barack

    def set__to_inventory(self, inventory):
        self._to_inventory= inventory

    def _check_worker(self):
        if not self._from_barack.workers_count() >= 1 and self._to_barack.workers_count() >= 1:
            pass

    def _check_address(self):
        return (self._from_barack and self._to_barack and self._to_inventory) != None

    def create_product(self):
        pass



class Product:
   def __init__(self):
       pass
   


class Simulation: # here starts the simulation
    def __init__(self):
            self._home = []
            self._factory = []
            self._field = []
            self._dining_room = []
            self._barack = []
            self._warehouse = []
            self._inventory = []
            self.simulation = False

    def simulation_is_over(self): # checks if there are at least one worker for the simulation to work
        pass

    def add_factory(self, factory):
        self._factory.append(factory)

    def add_home(self, home):
        self._home.append(home)

    def add_field(self, field):
        self._field.append(field)

    def add__dining_room(self, dining_room):
        self._dining_room.append(dining_room)

    def add_barack(self, barack):
        self._barack.append(barack)
    
    def add_warehouse(self, warehouse):
        self._warehouse.append(warehouse)

    def add_inventory(self, inventory):
        self._inventory.append(inventory)

    def run_world(self):
        self.simulation = True

    def add_worker(self, numb_workers):
        pass

    def create_world(self):
        pass