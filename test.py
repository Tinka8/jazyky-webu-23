# newlist = [expression for item in iterable if condition == True]

user_input = "Dnes je na Slovensku jesenné počasie.".split()

newlist = [word for word in user_input if "o" not in word and "O" not in word and "a" not in word and "A" not in word]
    
print(" ".join(newlist))


##
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
point1 = Point(3, 2)
print(isinstance(point1, Point))


def add_one(my_list=None):
  if my_list is None:
    my_list = []
  my_list.append(1)
  return my_list


list_1 = add_one()
list_2 = add_one()
print(list_2)


original_data = {
  "log": [2, 3]
}
copied_data = dict(original_data)
copied_data["log"].append(4)
print(original_data["log"])


def extract_username(path):
  path_components = path.split("/")
  # Mistakenly refer to `path`, not `path_components`.
  username = path[2]
  return username

print(extract_username("/home/amir/proj/"))



coordinates = [(2, 3), (5, 2)]
total = 0
for coord in coordinates:
  x = coord[0]
  y = coord[1]
  total += x * y
print(total)


some_list = [[]]
three_lists = some_list * 3
three_lists[0].append(1)
three_lists[1].append(2)
three_lists[2].append(3)
print(three_lists)


def check_pin(correct_pin, provided_pin):
  global failed_attempts
  if provided_pin == correct_pin:
    return True
  else:
    return False
    failed_attemps += 1

print(check_pin("1234", "5678"))


def add_one(my_list=[]):
  my_list.append(1)
  return my_list

list_1 = add_one()
list_2 = add_one()
list_3 = add_one()
print(list_3)


trace = []

try:
  1 / 0
  trace.append("try finished")
except ZeroDivisionError:
  trace.append("caught zero division")
except KeyError:
  trace.append("caught key error")
finally:
  trace.append("finally")

print(trace)


phone_numbers = {
  "Amir": "555-1234",
  "Cindy": "601-5362"
}

def phone_number_length(name):
  return len(phone_numbers.get(name, ""))

print(phone_number_length("Betty"))


visitors = ["Amir", "Betty", "Cindy", "Dalili"]
print(visitors[0:4:2])


some_dict = {}
some_dict["b"] = 2
some_dict["a"] = 1
some_dict["c"] = 3
print(list(some_dict.keys()))


winning_ids = [10, 5, 3, 2, 1]
print(winning_ids[:-2])


s = "5,3,1,2,4"
string = s.split(",")
print(string)
for num in string:
  num = int(num)
  total += num
    
print(total)


empty_dict = {}
print(empty_dict.get("Betty"))


print(sum([[1, 2], [3, 4], [5, 6]], start=[]))
print([value + 10 for value in range(6)])


names = ["Amir", "Betty", "Cindy"]

##
for name in names:
  if name.endswith("y"):
    print(name)
