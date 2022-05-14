from bisect import bisect_right


class Person:
    species="Homo Sapiens"
    def __init__(self, name , birth_year):
        self.name = name
        self.birth_year=birth_year
    def Sayhello(this):
        from datetime import datetime
        return f'Hi! I am {this.name} f,I am {datetime.today().year - this.birth_year} years old'

person1=Person('Iskander',2008)
person2=Person('Shavkat',2008)
# person1.name='Iskander'
# person2.name='Shavkat'
# print(person1.species,person1.name,person1.birth_year)
# print(person2.species,person2.name,person2.birth_year)
print(person1.Sayhello())


# class Circle:
#     def __init__(self,side):
#         self.side = side
#     def formula(self):
#         return (self.side **2)/(4 *3.14)
#     # def perimetr(self):
#     #     return self.side * 4

# sq1=Circle(100)
# print(sq1.formula())

