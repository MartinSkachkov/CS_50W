class Point():
    # automatically called when we try to create an object of type Point
    # self - the current object we are dealing with
    def __init__(self, x , y):
        # initialize the current object
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x, p.y)

class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__passengers = []

    def add_passenger(self, name):
        if self.open_seats() == 0:
            return False
        
        self.__passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.__passengers)
    
    def get_passengers(self):
        # When you return a list (or any mutable object) from a function in Python,
        # you are indeed returning a reference to the original object, not a copy of it.
        # This means that if the caller of the function modifies the list, it will affect the original list.
        # To prevent this, you should return a copy of the list. 
        return self.__passengers.copy() # keep in mind it's shallow copy

flight = Flight(3)

#| Flight |
#|--------|
#|capct= 3|
#|psngr=[]|

people = [["A"], "B", "C", "D"]

for p in people:
    res = flight.add_passenger(p)

    if res == True:
        print(f'Added {p} to flight')
    else:
        print(f'No available seats for {p}')

# private ?
# flight.passengers.append(3)
# print(flight.passengers) ["A", "B", "C", 3]

# to make passengers private use __
# then we need to write a getter so that we can see the contents
# of the value

# print(flight.__passengers) error

print(flight.get_passengers())
passengers = flight.get_passengers()

passengers.append(3)
print(passengers)
print(flight.get_passengers())
# [['A'], 'B', 'C', 3]
# [['A'], 'B', 'C']

passengers[0].append(3)
print(passengers)
print(flight.get_passengers())
# [['A', 3], 'B', 'C', 3]
# [['A', 3], 'B', 'C']
