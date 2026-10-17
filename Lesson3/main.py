import oop

# Khởi tạo object Human
human1 = oop.Human("Tuấn Phong", 13, "Male")
    # Test phương thức (methods)
human1.display_info()
human1.sing("Happy Birthday")

# Khởi tạo object Student
stu1 = oop.Student("Châu Anh", 13, "Female", "MindX")
    # Tính đa hình (ghi đè phương thức)
stu1.display_info()
    # Tính kế thừa (dùng phương thức của lớp cha)
stu1.sing("Baby Shark")
    # Phương thức thay đổi thông tin school
stu1.change_school("THCS Trưng Vương")