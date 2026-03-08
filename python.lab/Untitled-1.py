#5/12/25

def integers():
    i = 1
    while True:
        yield i
        i += 1

integers()

def squres():
    for i in integers():
        yield i**2

def take(n, sequence):
    seq = iter(sequence)
    result = []

    for _ in range(n):
        result.append(next(seq))

    return result

take(3, squres())

lst_1 = list(range(6))
print(lst_1)
iter_1 = iter(lst_1)
print(iter_1)
print(next(iter_1))

class Cities:
    def __init__(self):
        self._cities_list = []
        self.__index = 0

    def __iter__(self):
        print("Caling cities")
        return self
    
    def __next__(self):
        print("next method")
        if self.__index >= len(self.cities_list):
            raise StopIteration
        else:
            item = self._cities_list[self.__index]
            self.__index += 1
            return item
        

    def add_city(self, city_name):
        self._cities_list.append = []

    def get_cities(self):
        return self._cities_list
    
c2 = Cities()

c2.add_city("Lviv")
c2.add_city("Lemberg")

for city in c2:
    print(city)


class Cities2:
    def __init__(self):
        self._cities_list = []
        self.__index = 0

    def __iter__(self):
        print("Caling cities")
        return self
    
    def __next__(self):
        print("next method")
        if self.__index >= len(self.cities_list):
            self.index = 0
            raise StopIteration
        else:
            item = self._cities_list[self.__index]
            self.__index += 1
            return item
        
    def __getitem__(self, ind): 
        return self._cities_list[ind]
    
    def __eq__(self, value):
        pass

    def add_city(self, city_name):
        self._cities_list.append = []

    def get_cities(self):
        return self._cities_list
    
c3 = Cities()

c3.add_city("Lviv")
c3.add_city("Lemberg")
c3[0]



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    pass

dict_1 = {c3: "value"}
dict_1.keys() 