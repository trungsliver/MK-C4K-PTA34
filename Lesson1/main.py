# Variables - Biến số
    # Dùng để lưu trữ dữ liệu
    # Có thể thay đổi được khi lập trình
name = 'Duc Trung'
a, b, c = 1, 2, 3
    # 2 kiểu đặt biến / hàm
        # camelCase
myFullName = 'Bui Duc Trung'
        # snake_case
my_full_name = 'Bui Duc Trung'

# Data Types - Kiểu dữ liệu
    # string: chuỗi / xâu ký tự 
name = 'Duc Trung'
    # int (integer): số nguyên
age = 2
    # float: số thực (số thập phân)
score = 8.5
    # bool/boolean: logic, chỏ gồm True/False
is_male = True

# Các cách hiển thị dữ liệu
    # Cách 1: Dùng dấu +
print('Name: ' + name)
    # Cách 2: Dùng dấu ,
print('Age:', age)
    # Cách 3: Dùng f-string
print(f'Tôi tên là {name}, hiện {age} tuổi')
    # Cách 4:
print(f'''
===== THÔNG TIN =====
Name: {name}
Age: {age}
Score: {score}
Is male: {is_male}
=====================''')
    # Lưu ý:
        # \n: xuống dòng
print('Dòng 1 \nDòng 2 \nDòng 3')
        # \t: tab (1 tab = 4 khoảng trắng)
print('Cột 1 \tCột 2 \tCột 3')
        # end = ' ': thay đổi ký tự cuối cùng

# Các phép toán:
    # Thông thường: + - * /
    # Chia lấy nguyên: //
    # Chia lấy dư: %
    # Lũy thừa: **
    # Phép toán logic: and - or - not

# Câu điều kiện: 
    # Các phép so sánh: == != > < >= <=
    # Cấu trúc: 3 dạng
        # Dạng thiếu:       if ...
        # Dạng đủ:          if ... else ...
        # Dạng đa nhánh:    if ... elif ... else ...

# Vòng lặp for - Vòng lặp hữu hạn
    # range(start, stop, step)
