# Lập trình hướng đối tượng (OOP)
# Object Oriented Programming

#  Khái niệm: là cách mô tả thế giới thực vào chương trình máy tính

# Ví dụ: mô phỏng Human (con người)
    # attributes (thuộc tính): đặc điểm đối tượng (tên, tuổi, giới tính,...)
    # methods (phương thức): hành động của đối tượng (ăn, ngủ, nói chuyện,...)

# Đối tượng tổng quát: class
# Đối tượng cụ thể: object

# Khai báo lớp đối tượng (đối tượng tổng quát)
class Human:
    # Khởi tạo giá trị (thuộc tính), đây là hàm có sẵn
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (đặc điểm)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức hiển thị thông tin
    def __str__(self):
        return f'{self.name} - {self.age} - {self.gender}'

    # Phương thức hiển thị thông tin
    def display_info(self):
        print('===== HUMAN INFO =====')
        print('Name:', self.name)
        print('Age:', self.age)
        print('Gender:', self.gender)
        print('======================')

    # Phương thức hát
    def sing(self, song:str):
        print(f'{self.name} is singing {song}')

# Khai báo đối tượng cụ thể
human1 = Human('Duc Huy', 13, 'male')
human2 = Human('Gia Linh', 14, 'female')

# Hiển thị thông tin
print(human1)
print(human2)
human1.display_info()
human2.sing('Baby Shark')