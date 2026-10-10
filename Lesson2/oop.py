# Khai báo đối tượng tổng quát
class Animal:
    # Hàm khởi tạo
    def __init__(self, name, species, age, color):
        self.name = name
        self.species = species
        self.age = age
        self.color = color

    # Phương thức hiển thị thông tin
    def __str__(self):
        return f"{self.name} - {self.species} - {self.age} - {self.color}"

    def display_info(self):
        print('===== ANIMAL INFO =====')
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Color: {self.color}")
        print('=======================')

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

# Khai báo object
animal_1 = Animal("Loopy", 'Beaver', 5, 'Pink')
# Hiển thị thông tin
print(animal_1)  
animal_1.display_info()
animal_1.eat("fish")