
# coding: utf-8

# In[19]:

class Triangle():
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        
    def __str__(self):
        return ("The three sides of the triangle measure %s, %s, %s" % (self._side1, self._side2, self._side3))
    
class Area(Triangle):
    def __init__(self, *args, **kwargs):
        super(Area, self).__init__(*args, **kwargs)
        
    def Answer(self):
        s = ((self._side1 + self._side2 + self._side3)/2)
        Area = (s*(s-self._side1)*(s-self._side2)*(s-self._side3)) ** 0.5
        return (Area)
    
a = Area(20, 25, 32).Answer()
print (a)



def filter_long_words(a, b):
    a = input("Enter list of words separated by 'Space': ")
    b = input("Enter word threshold: ")
    d = list(filter(lambda c: len(c) > int(b), a.split(" ")))
    return (d)

Solution = filter_long_words("a", "b")
print (Solution)

