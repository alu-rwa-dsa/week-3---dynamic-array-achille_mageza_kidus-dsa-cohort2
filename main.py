class array:
    def __init__(self, array=None):
        if array is None:
            array = [5, 4, 6, 8, 10, 11,34]
        self.array = array


# Space complexity  and Time complexity is O(1)




def length(self):
    print(len(self.array))

# Space complexity  and Time complexity is O(1)


# specification of  item in our list
def get_value(self):
    for n, i in enumerate(self.array):
        if i == 1:
            print(self.array[n])

     # Spatial Competitiveness: in the top code, the function allows you to search for an element in a
     # list containing integers and scrolls through the list to determine the requested element.
     # The algorithm forms a kind of memory for a new element and the elements of the list.
     # then the space of the alogorithm becomes O(n)



def replace(self):
    for n, i in enumerate(self.array):
        if i == 4:
            self.array[n] = 3
            return self.array




# subclass is simple class inherit
class var(array):
    def __init__(self, array=None):
        super().__init__(array=[5, 4, 6, 8, 10, 11,34])
        if array is None:
            array = [5, 4, 6, 8, 10, 11,34]

    # Space complexity  and Time complexity is O(1)

    # this method add an item in list
    def Add_list(self):
        self.array.append(1111)
        print(self.array)

    # Space complexity  and Time complexity is O(1)

    # this method delete an item from our list
    def deleted_list(self):
        del self.array[2:5]
        print(self.array)





length_array = var()
length_array.Add_list()
length_array.deleted_list()
