from collections import deque as de
import random as rd
import sqlite3



class Places:

    '''
    a super class to the following classes Barack, Warehouse and Inventory
    '''

    def __init__(self):
        '''constructor'''
        self._objects = de([])

    def get_count(self):
        '''# it returns the number of the objects '''
        raise NotImplementedError()

    def add_object(self, object):
        '''# it adds un opject'''
        raise NotImplementedError()

    def send_object(self):
        '''# it sends an item to somewhere else'''
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()


class Barack(Places):
    ''' a place where Workers wait'''
    def __init__(self):
        super().__init__()
        self._objects = de([])

    def __str__(self):
        return f"the number of Workers is {len(self._objects)}"

    def get_count(self):
        return len(self._objects)
    
    def add_object(self, worker):
        self._objects.append(worker)

    def send_object(self): # remove a worker and return it. it removes from the left with index 0
        return self._objects.popleft()

class Inventory(Places):
    '''# a place to put the Products in'''
    def __init__(self):
        super().__init__()
        self._objects = []

    def __str__(self):
        return f"the number of Workers is {len(self._objects)}"

    def get_count(self):
        return len(self._objects)
    
    def add_object(self, product):
        self._objects.append(product)
        
    def send_object(self):
        return self._objects.pop()


class Warehouse(Places):
    '''# a place to save the Food in'''

    def __init__(self):
        super().__init__()
        self._objects = de([])

    def __str__(self):
        return f"the number of Workers is {len(self._objects)}"

    def add_object(self, food):
        self._objects.append(food)

    def send_object(self):
        return self._objects.popleft() # removes food from left and return that specific food

    def get_count(self):
        return len(self._objects)

class Resources:
    '''# a super class to the following classes Worker,Food and Product'''
    def __init__(self):
        pass
    def qualitylife(self):
        raise NotImplementedError()


class Worker(Resources):
    '''# this class contains Information about the Worker'''
    def __init__(self):
        super().__init__()
        self._vitality = 100

    def increase(self, numb): # here increase the vitality of the worker
        if numb + self._vitality >= 100: # this makes sure that the vitality does not increase more than 100
            self._vitality = 100
        else:
            self._vitality += numb

    def shrink(self, float): # this method shrink the vitality of a worker
        if self._vitality - float >0:
            self._vitality -= float
        else:
            self._vitality = 0


    def check_die(self, point): # checks if the worker has vitality == 0
        life = False
        if point == 0:
            life = True
        else:
            life = False
        return life
    
    def qualitylife(self):
        return self._vitality


class Food(Resources):
    '''# a resourse prodused by the Field'''
    def __init__(self):
        super().__init__()
        self._quality = None
        self.random_quality()

    def random_quality(self): # gives a random quality 
        self._quality = rd.randrange(-40, 50)

    def qualitylife(self):
        return self._quality

class Product:
   '''#a resourse prodused by the factories'''
   def __init__(self):
       pass

class Information:
    ''' a super class to the following classes Home, Dining_room, Field and Factory '''
    def __init__(self, from_barack, to_barack):
        self._from_barack = from_barack #from which barack the worker will be recieved from
        self._to_barack = to_barack # to which barack should the worker be send to?

    def set_to_barack(self, to_barack):
        raise NotImplementedError()

    def set_from_barack(self,from_barack):
        raise NotImplementedError()

    def _check_worker(self): #checks if there are Workers in Barack
        raise NotImplementedError()

    def _check_address(self):
        raise NotImplementedError()

    def start(self):
        raise NotImplementedError()


class Dining_room(Information): 
    '''here eats the workers'''
    def __init__(self, from_barack, to_barack, from_warehouse):
        super().__init__(from_barack, to_barack)
        self._from_warehouse = from_warehouse #from which warehouse the food should be brought from

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
        return self._from_barack.get_count() >= 1
    
    def _check_address(self):
        return (self._from_barack and self._from_warehouse and self._to_barack) != None
    
    def start(self):
        if not (self._check_address() and self._check_worker() and self.check_food()):
            print('something does not exisit in dining_room, either addresses, workers or food')

        else:

            quality = self._from_warehouse.send_object().qualitylife() # gives the quality of the food
            worker = self._from_barack.send_object() # bring the worker

            if  quality > 0: # if the quality is positive
                worker.increase(quality)
                self._to_barack.add_object(worker)
                print("someone is got stronger by the food")

            else: #if the quality is negative
                worker.shrink(-quality)
                if worker.check_die(worker.qualitylife()):
                    print("a worker died")
                else:
                    self._to_barack.add_object(worker)
                    print("someone is sick by the food")



class Field(Information):
    '''# a place where workers work to make some food'''
    def __init__(self, from_barack, to_barack, to_warehouse):
        super().__init__(from_barack, to_barack)
        self._to_warehouse = to_warehouse #to which warehouse the food should be sent to

    def set_to_barack(self, barack):
        self._to_warehouse = barack

    def set_to_warehouse(self, warehouse):
        self._to_warehouse = warehouse

    def set_from_barack(self, barack):
        self._from_barack = barack

    def _check_worker(self): #check if there are workers in barack
        return self._from_barack.get_count() >= 1

    def _check_address(self):
        value = None
        if (self._from_barack and self._to_warehouse and self._to_barack) != None:
            value = True

        else:
            value = False

        return value

    def start(self): # here starts the production of the food
        if not (self._check_address() and self._check_worker()):
            print('something does not exist in the field, workers or adderesses')
            
        else:

            worker = self._from_barack.send_object()
            accident = rd.choice([True, False, False, False, False]) # an accident may occur

            if not accident:
                self._to_barack.add_object(worker)
                self._to_warehouse.add_object(Food())
                print("a worker produced food from the field")
                
            else:
                print('worker accident in the field')


class Home(Information):
    '''# a place where workers get some rest or even marry'''
    def __init__(self, from_barack, to_barack, from_inventory):
        super().__init__(from_barack, to_barack)
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

        if not self._from_barack.get_count() >= 1 and self._to_barack.get_count() >= 1 and house_type =='sleep':
            new_address = self._from_barack
            self._from_barack = self._to_barack
            self._to_barack = new_address

        elif not self._from_barack.get_count() >= 2 and self._to_barack.get_count() >= 2 and house_type =='marry':
            new_address = self._from_barack
            self._from_barack = self._to_barack
            self._to_barack = new_address

        if house_type =='sleep':
            return self._from_barack.get_count() >= 1 # if it is for sleeping so only one worker is needed in the home/room 
        
        else:
            return self._from_barack.get_count() >= 2 # if it is for marrage it needs two workers to get married home

    def _check_address(self): #checks if all addresses exist
        value = None
        if (self._from_barack and self._from_inventory and self._to_barack) != None:
            value = True

        else:
            value = False

        return value
    
    def start(self):
        self.set_house_type() # give a random choice for workers, either to marry of to get some rest
        house_type = self._house_type

        if not (self._check_worker(house_type) and self.check_produkt() and self._check_address()):
            print('something does not exist in home, either workers, products or addresses')

        else:
            self._from_inventory.send_object() # remove a product from the inventory

            if house_type == 'sleep':
                worker3 = self._from_barack.send_object()
                worker3.increase(rd.randrange(25))
                self._to_barack.add_object(worker3)
                print("someone has slept")

            elif house_type == 'marry':
                worker1 = self._from_barack.send_object()
                worker2 = self._from_barack.send_object()
                self._to_barack.add_object(worker1)
                self._to_barack.add_object(worker2)
                self._to_barack.add_object(Worker())
                print("a couple got married")



class Factory(Information):
    def __init__(self, from_barack, to_barack, to_inventory):
        super().__init__(from_barack, to_barack)
        self._to_inventory = to_inventory # to which inventory we should send the product.
    

    def set_to_barack(self, barack):
        self._to_barack = barack

    def set_from_barack(self, barack):
        self._from_barack = barack

    def set_to_inventory(self, inventory):
        self._to_inventory= inventory

    def _check_worker(self):
        if not self._from_barack.get_count() >= 1 and self._to_barack.get_count() >= 1:
            new_address = self._from_barack
            self._from_barack = self._to_barack
            self._to_barack = new_address

        return self._from_barack.get_count() >= 1
    def _check_address(self):
        return (self._from_barack and self._to_barack and self._to_inventory) != None

    def start(self):
        if not (self._check_address() and self._check_worker()):
            print('something does not exist in factory, either addresses or workers')

        else:

            worker1 =self._from_barack.send_object() # bring a worker 
            accident = rd.choice([True, False,False,True,False]) # a chance that an accident occur

            if accident:
                worker1.shrink(100) # the worker dies
            else:
                worker1.shrink(rd.randrange(25)) # shrink the vitality of the worker 
                if worker1.check_die(worker1.qualitylife()):
                    print("a worker has died")

                else:
                    self._to_inventory.add_object(Product())
                    self._to_barack.add_object(worker1)
                    print("a worker has made a product")

class SimSimsAnalytics:
    '''#"analyses"'''
    def __init__(self, file):
        self._conn = self._create_connection(file)
        self._sim_id = None

        c = self._conn.cursor()
        c.execute("INSERT INTO simulations(date) VALUES (datetime('now'))")
        self._conn.commit()
        c.execute ("SELECT last_insert_rowid();")
        self._sim_id = c.fetchall()[0][0]

    def show_result(self): # here we can see the data of the database
        c = self._conn.cursor()
        c.execute("SELECT * FROM iterations")
        rows = c.fetchall()
        for row in rows:
            print(row)

    def add_step(self,step, Workers, Products, Food): # adds the data to the data base
        c = self._conn.cursor()
        c.execute(f"INSERT INTO iterations VALUES ({self._sim_id}, {step}, {Workers}, {Products}, {Food})")
        self._conn.commit()

    def to_excel(self, filename): # move to excel
        pass

    def to_figure(self, filename): # here we can draw the diagram
        pass

    def _create_connection(self, db_file): # connect to the database
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)

        return conn

class Simulation:
    '''# here starts the simulation'''
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
            if x.get_count() == 0:
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
                worker1.add_object(Worker())

    def create_world(self):
        while self.simulation:
            if self.simulation:
                for x in self._factory:
                    x.start() # start the production
                    self.simulation_is_over() # checks if there are at least one worker to work

            if self._home[0].get_inventory() != 0 and self.simulation:
                for x in self._home:
                    x.start() # make sure that either a worker get some rest or get married
                    self.simulation_is_over()

            if self.simulation:
                for x in self._field:
                    x.start() # plant the field and make some food for the workers
                    self.simulation_is_over()

            if self._dining_room[0].get_warehouse() !=0 and self.simulation:
                for x in self._dining_room:
                    x.start() # a place where workers eat
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



