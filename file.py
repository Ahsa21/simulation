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
        if numb + self.vitality >= 100: # this makes sure that the vitality does not increase more than 100
            self.vitality = 100
        else:
            self.vitality += numb

    def shrink(self, float): # this method shrink the vitality of a worker
        if self.vitality - float >0:
            self.vitality -= float
        else:
            self.vitality = 0


    def check_die(self, point): # checks if the worker has vitality == 0
        life = False
        if point == 0:
            life = True
        else:
            life = False
        return life
    def get_livskraft(self):
        return self.vitality



class Dining_room: # here eats the workers
    def __init__(self, from_barack, to_barack, from_warehouse):
        self._from_barack = from_barack #from which barack the worker will be recieved from
        self._from_warehouse = from_warehouse #from which warehouse the food should be brought from
        self._to_barack = to_barack # to which barack should the worker be send to?

    def get_warehouse(self): # returns how much food we have
        return self._from_warehouse.get_count()

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
        if not (self._check_address() and self._check_worker() and self.check_food()):
            print('something does not exisit in dining_room, either addresses, workers or food')

        else:

            quality = self._from_warehouse.send_food().get_quality() # gives the quality of the food
            worker = self._from_barack.send_worker() # bring the worker

            if  quality > 0: # if the quality is positive
                worker.increase(quality)
                self._to_barack.add_worker(worker)
                print("someone is got stronger by the food")

            else: #if the quality is negative
                worker.shrink(-quality)
                if worker.check_die(worker.get_livskraft()):
                    print("a worker died")
                else:
                    self._to_barack.add_worker(worker)
                    print("someone is sick by the food")


class Food:
    def __init__(self):
        self.quality = None
        self.random_quality()

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
        if not (self._check_address() and self._check_worker()):
            print('something does not exist in the field, workers or adderesses')
            
        else:

            worker = self._from_barack.send_worker()
            accident = rd.choice([True, False, False, False, False]) # an accident may occur

            if not accident:
                self._to_barack.add_worker(worker)
                self._to_warehouse.recieve_food(Food())
                print("a worker produced food from the field")
                
            else:
                print('worker accident in the field')


class Home: # a place where workers get some rest or even marry
    def __init__(self, from_barack, to_barack, from_inventory):
        self._from_barack = from_barack #from which barack the worker will be recieved from
        self._to_barack = to_barack # to which barack should the worker be sent to?
        self._from_inventory = from_inventory #from which inventory we will take/ recieve a product
        self._house_type = None

    def get_inventory(self):
        return self._from_inventory.get_count()

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
        self.set_house_type() # give a random choice for workers, either to marry of to get some rest
        house_type = self._house_type

        if not (self._check_worker(house_type) and self.check_produkt() and self._check_adress()):
            print('something does not exist in home, either workers, products or addresses')

        else:
            self._from_inventory.send_product() # remove a product from the inventory

            if house_type == 'sleep':
                worker3 = self._from_barack.send_worker()
                worker3.increase(rd.randrange(25))
                self._to_barack.add_worker(worker3)
                print("someone has slept")

            elif house_type == 'marry':
                worker1 = self._from_barack.send_worker()
                worker2 = self._from_barack.send_worker()
                self._to_barack.add_worker(worker1)
                self._to_barack.add_worker(worker2)
                self._to_barack.add_worker(Worker())
                print("a couple got married")



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
            new_address = self._from_barack
            self._from_barack = self._to_barack
            self._to_barack = new_address

        return self._from_barack.workers_count() >= 1
    def _check_address(self):
        return (self._from_barack and self._to_barack and self._to_inventory) != None

    def create_product(self):
        if not (self._check_address() and self._check_worker()):
            print('something does not exist in factory, either addresses or workers')

        else:

            worker1 =self._from_barack.send_worker() # bring a worker 
            accident = rd.choice([True, False,False,True,False]) # a chance that an accident occur

            if accident:
                worker1.shrink(100) # the worker dies
            else:
                worker1.shrink(rd.randrange(25)) # shrink the vitality of the worker 
                if worker1.check_die(worker1.get_livskraft()):
                    print("a worker has died")

                else:
                    self._to_inventory.recieve_product(Product())
                    self._to_barack.add_worker(worker1)
                    print("a worker has made a product")




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
        start = True
        for x in self._barack:
            if x.workers_count() == 0:
                start = False
            else:
                return True
        if start:
            self.simulation = True
            return self.simulation
        
        self.simulation = False

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
        for worker1 in self._barack:
            for worker2 in range(numb_workers):
                worker1.add_worker(Worker())

    def create_world(self):
        while self.simulation:
            if self.simulation:
                for x in self._factory:
                    x.create_product() # start the production
                    self.simulation_is_over() # checks if there are at least one worker to work

            if self._home[0].get_inventory() != 0 and self.simulation:
                for x in self._home:
                    x.start_home() # make sure that either a worker get some rest or get married
                    self.simulation_is_over()

            if self.simulation:
                for x in self._field:
                    x.produce() # plant the field and make some food for the workers
                    self.simulation_is_over()

            if self._dining_room[0].get_warehouse() !=0 and self.simulation:
                for x in self._dining_room:
                    x.start_eating() # a place where workers eat
                    self.simulation_is_over()
        print("simulation is over")



x = Simulation()
barack1 = Barack()
barack2 = Barack()
inventory1 = Inventory()
warehouse1 = Warehouse()

x.add_barack(barack1)
x.add_barack(barack2)
x.add_factory(Factory(barack1, barack2, inventory1))
x.add_home(Home(barack2, barack1, inventory1))
x.add_field(Field(barack1, barack2, warehouse1))
x.add__dining_room(Dining_room(barack2, barack1, warehouse1))
x.add_worker(5)
x.run_world()
x.create_world()



