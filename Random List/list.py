import random

class Random_list(list):
    def get_random_element(self):
        ran = random.randint(0, len(self)-1)
        return self.pop(ran)


my_list = Random_list([1, 2, 3, 4, 5])
print("Random Element:", my_list.get_random_element())
print("Updated List:", my_list)
