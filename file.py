from collections import deque as de
import random as rd

class barack:
    def __init__(self):
        self.workers = de([])

    def workers_count(self):
        return len(self.workers)
    
    def add_worker(self, worker):
        self.workers.append(worker)


    def send_worker(self): # remove a worker and return it. it removes from the left with index 0
        return self.workers.popleft()



class worker: # this class contains information about the worker
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



class dining_room: # here eats the workers
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


class food:
    def __init__(self):
        self.quality = None

    def random_quality(self): # gives a random quality 
        self.quality = rd.randrange(-40, 50)

    def get_quality(self):
        return self.quality


class warehouse:
    def __init__(self):
        self.food = de([])

    def recieve_food(self, food):
        self.food.append(food)

    def send_food(self):
        return self.food.popleft() # removes food from left and return that specific food

    def get_count(self):
        return len(self.food)


