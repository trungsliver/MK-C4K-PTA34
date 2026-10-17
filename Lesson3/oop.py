class Human:
    # hàm khởi tạo
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print("\n===== HUMAN INFO =====")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print("======================\n")

    def sing(self, song):
        print(f"{self.name} is singing: {song}")

# 4 tính chất của OOP:
    # 1. Đóng gói (encapsulation): che giấu dữ liệu (password)
    # 2. Kế thừa (inheritance): dùng lại thuộc tính & phương thức cũ
    # 3. Đa hình (polymorphism): cùng 1 tên hàm, hành động khác nhau
    # 4. Trừu tượng (abstraction): ghi tên phương thức trước, viết nội dung hành động sau

# Lớp Student kế thừa từ lớp Human
class Student(Human):
    def __init__(self, name, age, gender, school):
        # Gọi hàm khởi tạo từ lớp cha (Human)
        super().__init__(name, age, gender)
        # Thuộc tính riêng của Student
        self.school = school

    # Tính chất đa hình 
    def display_info(self):
        print("\n===== STUDENT INFO =====")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"School: {self.school}")
        print("========================\n")

    # Phương thức sửa thông tin school học sinh
    def change_school(self, new_school):
        if new_school.strip() == "":
            print("Tên trường học không hợp lệ!")
        else:
            # Cập nhật thông tin school
            self.school = new_school
            print('Thay đổi school thành công!')
            # Hiển thị lại thông tin sau chỉnh sửa
            self.display_info()

    # Phương thức sửa tuổi
    def change_age(self):
        try:
            new_age = int(input("Nhập tuổi mới: "))
            if new_age < 0:
                print("Tuổi không hợp lệ!")
            else:
                # Cập nhật thông tin tuổi
                self.age = new_age
                print('Thay đổi tuổi thành công!')
                # Hiển thị lại thông tin sau chỉnh sửa
                self.display_info()
        except:
            print("Tuổi phải là một số nguyên!")