import oop

# Khai báo object
animal_2 = oop.Animal('Mickey', 'Mouse', 3, 'Black')
# Sử dụng phương thức (methods)
print(animal_2)
animal_2.display_info()
animal_2.eat("cheese")

# Bài 2: Tạo lớp Rectangle với các thuộc tính: length, width.  
# Tạo phương thức tính diện tích và chu vi của hình chữ nhật. 
# Test ở file main.py: tạo đối tượng, tính chu vi, diện tích.
rectangle_1 = oop.Rectangle(5, 3)
rectangle_1.display_info()
rectangle_1.display_info_2()

# Bài 3: Tạo lớp BankAccount với các thuộc tính: 
            # account_number: số tài khoản 
            # owner: tên chủ tài khoản
            # balance: số dư tài khoản
# Tạo phương thức:
            # deposit(amount): nạp tiền vào tài khoản
            # withdraw(amount): rút tiền từ tài khoản
            # display_balance(): hiển thị số dư tài khoản
            # (amount: số tiền nạp/rút theo đơn vị $)
account_1 = oop.BankAccount("9999", "Duc Trung", 1000)

account_1.display_balance()

account_1.deposit(500)
account_1.deposit(-100)  # Test nạp tiền không hợp lệ

account_1.withdraw(200)
account_1.withdraw(-50)
account_1.withdraw(99999999)

account_1.menu()