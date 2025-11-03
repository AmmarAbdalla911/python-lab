# class Vehicle:
#     total_vehicles= 0
#     def __init__(self, id, brand, model, rent_price):
#         self.id = id
#         self.brand = brand
#         self.model = model
#         self.rent_price = rent_price
#         self.is_rented = False
#         Vehicle.total_vehicles += 1
#     def rent(self):
#         if self.is_rented:
#             print("not avilable")
#         else:
#             self.is_rented = True
#             print(f"vehicle {self.id} rent sucsses")
#     def return_vehicle(self):
#         self.is_rented = False
#         print(f"vehicle {self.id} is now anvalabe")
#     def calculate_rental_cost(self, days):
#         return self.rent_price * days
#     def get_details(self):
#         print(f"{self.brand} - {self.model} - {self.id} - {self.rent_price} - {'Available' if not self.is_rented else 'Not available'}")
# class Car(Vehicle):
#     def __init__(self, id, brand, model, rent_price, num_doors):
#         super().__init__(id, brand, model, rent_price)
#         self.num_doors = num_doors
#         self.rental_price_multiplier = 1.0

#     def calculate_rental_cost(self, days):
#         return super().calculate_rental_cost(days) * self.rental_price_multiplier
#     def get_details(self):
#         print(f"car - {self.id} - {self.brand} - {self.model} - ({self.num_doors} doors) - ({self.rent_price}/day) - {'Available' if not self.is_rented else 'Not available'}")
# class Motorcycle(Vehicle):
#     def __init__(self, id, brand, model, rent_price, engine_cc):
#         super().__init__(id, brand, model, rent_price)
#         self.engine_cc =engine_cc
#         self.rental_price_multiplier = 0.7
        
#     def calculate_rental_cost(self, days):
#         return super().calculate_rental_cost(days) * self.rental_price_multiplier
#     def get_details(self):
#         print(f"motorcycle - {self.id} - {self.brand} - {self.model} - ({self.engine_cc} CC) - ({self.rent_price}/day) - {'Available' if not self.is_rented else 'Not available'}") 
# class Truck(Vehicle):
#     def __init__(self, id, brand, model, rent_price, cargo_cacpacity_tons):
#         super().__init__(id, brand, model, rent_price)
#         self.cargo_cacpacity_tons = cargo_cacpacity_tons   
#         self.rental_price_multiplier = 1.5
        
#     def calculate_rental_cost(self, days):
#         return super().calculate_rental_cost(days) * self.rental_price_multiplier
#     def get_details(self):
#         print(f"truck - {self.id} - {self.brand} - {self.model} - ({self.cargo_cacpacity_tons} TONS) - ({self.rent_price}/day) - {'Available' if not self.is_rented else 'Not available'}") 
#         #===================================================================
# class CustomRange:
#     def __init__(self, start, stop = None,step = 1 ):
#         if stop is None:
#                 stop = start
#                 start = 0
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.current = start
#     def __iter__(self):
        
#             return self 
#     def __next__(self):
#         if (self.step> 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
#             raise StopIteration
#         value = self.current
#         self.current += self.step
#         return value
#     def reset(self):
#         self.current =  self.start
# #=====================================================================================
#     def red_file_lines(filename):
#         with open(filename, "r" ,encoding='utf-8' ) as f :
#             for line in f :
#                 yield line
#     def filter_lines(lines, keyword):
#         for line in lines :
#             if keyword in line:
#                 yield line
#     def  strip_lines(lines):
#         for line in lines:
#             yield line.strip()
#     def number_lines(lines):
#         for i , line in enumerate(lines, start=1):
#             yield f"{i}.{line}"
#     def chunk_lines(lines, chunk_size):
#         chunk = []
#         for line in lines:
#             chunk.append(line)
#             if len(chunk) == chunk_size:
#                 yield chunk
#                 chunk = []
#         if chunk:
#             yield chunk
        
 #==========================================================================================
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*n):
        start = time.time()
        result = func(*n)
        end = time.time()
        print(f"[TIMER] Function '{func.__name__}' executed in {end - start} seconds")
        return result
    return wrapper


# @timer    
# def slow_function(n): 
#     time.sleep(n)
#     return f"Slept for {n} seconds"


# result = slow_function(2)
# print(result)
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Calling function '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOGGER] Function '{func.__name__}' returned: {result}")
        return result
    return wrapper
def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling '{func.__name__}'")
        print(f"[DEBUG]   args: {args}")
        print(f"[DEBUG]   kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] '{func.__name__}' returned: {result}")
        return result
    return wrapper
#+==================================================================================
class Product:
    def __init__(self, product_id, name, price, stock, category)
        self.product_id = product_id
        self.name = name
        self.price = price
        self. stock = stock
        self.category = category
        self.is_available = True
    def add_stock(self, number):
        self.stock += number
    def reduce_stock(self, number):
        if self.stock >= number :           
            self.stock -= number
        else :
            print("not enough")    
    def apply_discount(self, perc):
        discount = self.price * (perc / 100)
        self.price -= discount
    @property
    def is_available(self):
        if self.stock > 0 :
            return True
        else:
            return False
    def __str__(self):
        return f"{self.name} ({self.product_id}) - ${self.price} - (stock:{self.stock})"
    def __reper__(self):
        return f"Product('{self.product_id}', '{self.name}', {self.price}, {self.stock}, '{self.category}')"
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.product_id == other.product_id
        return False
    

        