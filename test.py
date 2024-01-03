# newlist = [expression for item in iterable if condition == True]

user_input = "Dnes je na Slovensku jesenné počasie.".split()

newlist = [word for word in user_input if "o" not in word and "O" not in word and "a" not in word and "A" not in word]
    
print(" ".join(newlist))




class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
point1 = Point(3, 2)
print(isinstance(point1, Point))