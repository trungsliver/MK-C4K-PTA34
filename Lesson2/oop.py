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

# Bài 2: Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        # Khai báo thêm thuộc tính (không cần truyền tham số)
        self.area = self.length * self.width
        self.perimeter = 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        print('===== RECTANGLE INFO =====')
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_perimeter()}")
        print('===========================')

    def display_info_2(self):
        print('===== RECTANGLE INFO =====')
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.area}")
        print(f"Perimeter: {self.perimeter}")
        print('===========================')

# Bài 3: BankAccount
class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def display_balance(self):
        print('\n===== BANK ACCOUNT INFO =====')
        print(f"Account Number: {self.account_number}")
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance}")
        print('==============================')

    def deposit(self, amount:float):
        if amount <= 0:
            print("Số tiền nạp không hợp lệ!")
        else:
            # Cộng tiền vào tài khoản
            self.balance += amount
            print(f"Đã nạp ${amount} vào tài khoản.")
        # Hiển thị lại só dư
        self.display_balance()

    def withdraw(self, amount:float):
        if amount <= 0 or amount > self.balance:
            print("Số tiền rút không hợp lệ!")
        else:
            # Trừ tiền từ tài khoản
            self.balance -= amount
            print(f"Đã rút ${amount} từ tài khoản.")
        # Hiển thị lại só dư
        self.display_balance()