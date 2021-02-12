print("Hello")

# Python interview review
# --- Data types ---
# List
#   editable and indexable
#   Functions https://docs.python.org/3/tutorial/datastructures.html
#       list.append(x) - add item x to the end
#       list.insert(i,x) - add item x at index i, push everything else down
#       list.remove(x) - remove first value that match x
#       list.pop([i]) - remove last item or item at index i
#       list.index(x[,i_start,i_end]) - return index of first match with value x
#       list.count(x) - count instances of a value x
#       list.reverse() - reverse elements of the list
#       list.extend(iterable) - append iterable to the list
my_list = [1,2,3,4,5,32,3,5]
# print(my_list)
# print(my_list.index(3,3))
# print(my_list)

# Tuple
#   immutable
my_tuple = (1,4,6,7,8,3)

# Dictionaries
#   key-value pairs, no multiple values for the same key
my_dict = {'bob':45, 'sharry':65, 'joe':10}
#   for-looping through dict
# for name,age in my_dict.items():
#   print("name and age: ",name,", ",age)

# Set
#   unordered, unindexed, no duplicates, faster look up
#   Functions https://www.w3schools.com/python/python_ref_set.asp
#     set.add(val) - adds val to the set, if not a duplicate
my_set = {90,2,4,6,777,8,8,9,0,2,4}
my_set.add(67)
print(my_set)
  
# List comprehensions
#   great for applying same opperation to the entire list
#   Use rounded brackets for generator expression (less memory)
#   can take the sum of a list comprehension
# x = [ i+1 for i in my_list]
# print(x)

# Generators
#   iterable function, use yield instead of return
#   When to use and when to not use?
# def my_gen(x):
#   for j in range(x):
#     yield str(j+1)

# for i in my_gen(5):
#   print(i)

# --- OOP ---
class animal:
  def __init__(self,name: str,legs: int):
    self.name = name
    self.legs = legs
  def describe(self):
    print("name and legs: ",self.name,", ",self.legs)

class human(animal):
  def __init__(self,name: str, speed: int):
    super().__init__(name,2)
    self.speed = speed
    
bob = animal("bob",4)
bob.describe()

chuck = human("chuck",1)
chuck.describe()

# --- Time complexity ---
# constant, linear, quadratic, exponential, logarithmic

# --- More Tools ---
# https://realpython.com/python-coding-interview-tips/#select-the-right-built-in-function-for-the-job
# https://towardsdatascience.com/10-algorithms-to-solve-before-your-python-coding-interview-feb74fb9bc27
# enumerate(list)
#   use for for loops that need values and indexes
# for index,val in enumerate(my_list):
#     print("index: ",index, "val: ", val)

# sorted(list[,reverse])
#   sorts list, can set reverse to True for reverse order
# print(my_list)
# print(sorted(my_list))

# itertools (import itertools)
#   itertools.permutations(list, r = int) - output a list of lists for every combination of the list (length r)
#   itertools.combinations(list, r = int) - output a list of lists for every combination where order does not matter

# String Operators
#   str.replace(str,str)
#   str.split
#   str + str <- concatenate
#   str * int <- repeate string int times
#   all the normal list operations (looping, indexing)
#   str[::-1] <- reverse order of string
#   "Hi %s" % name
blerp = ['d','e','r','p']
blerp.reverse()
print(blerp)
werp = "derpalopolis"
print(werp[::-1])
