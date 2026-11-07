# Import thư viện
import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

# Tạo app (python)
app = QApplication(sys.argv)

# Danh sách lưu tài khoản: "email:password"
users = ['admin@gmail.com:123456']

# Mỗi trang gia diện là 1 class riêng biệt
class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        # Lấy file giao diện đã tạo (cùng folder)
        uic.loadUi('signup.ui', self)
        # Kết nối nút bấm với hàm xử lý
        self.pushButton_signup.clicked.connect(self.signup_check)

    def test_button(self):
        msg_box('Thông báo', 'Bạn vừa ấn nút!')

    def signup_check(self):
        # Lấy thông tin người dùng đã nhập
        username = self.lineEdit_username.text().strip()
        email = self.lineEdit_email.text().strip()
        password = self.lineEdit_password.text().strip()
        confirm = self.lineEdit_confirm.text().strip()
        checkB = self.checkBox.isChecked()
        # Biến kiểm tra đăng ký
        check = True
        # Kiểm tra đăng ký
        if username == '' or email == '' or password == '' or confirm == '' or checkB == False:
            msg_box('Signup failed', 'Missing information!')
            check = False
        elif len(username) < 3:
            msg_box('Signup failed', 'Username must be at least 3 characters!')
            check = False
        elif check_email(email) == False:
            msg_box('Signup failed', 'Email is not valid!')
            check = False
        elif check_password(password) == False:
            msg_box('Signup failed', 'Password is not valid!')
            check = False
        elif password != confirm:
            msg_box('Signup failed', 'Password and confirm password do not match!')
            check = False
        else:
            # Kiểm tra email đã tồn tại chưa
            for user in users:
                # Tách email và password và lưu vào biến
                stored_email, stored_password = user.split(':', 1)
                if email == stored_email:
                    msg_box('Signup failed', 'Email already exists!')
                    check = False
                    break
        # Kiểm tra đăng ký
        if check == True:
            # Thêm tài khoản mới vào danh sách users
            new_user = f"{email}:{password}"
            users.append(new_user)
            print(users) # để test
            msg_box('Signup success', 'You have successfully signed up!')
            # Chuyển sang giao diện đăng nhập
            switch_window(Login())

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        # Lấy file giao diện đã tạo (cùng folder)
        uic.loadUi('login.ui', self)
        # Kết nối nút bấm với hàm xử lý
        self.pushButton_login.clicked.connect(self.check_login)

    def check_login(self):
        # Lấy thông tin từ giao diện
        email = self.lineEdit_email.text().strip()
        password = self.lineEdit_password.text().strip()
        # Biến kiểm tra đăng nhập
        check = False
        # Kiểm tra đăng nhập
        for user in users:
            stored_email, stored_password = user.split(':')
            if email == stored_email and password == stored_password:
                check = True
                break
        # Kiểm tra đăng nhập
        if check == True:
            msg_box('Login success', 'Welcome to my app !!!')
            switch_window(Signup())
        else:
            msg_box('Login fail', 'Email or password is incorrect!')
        
# Hàm hiển thị thông báo
def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

# Chuyển cửa sổ giao diện
def switch_window(classw):
    global window
    window = classw
    window.show()

# Hàm check email (dùng regex = regular expression)
def check_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False

# Hàm check password (dùng regex = regular expression)
def check_password(password):
    import re
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$'

    if re.match(pattern, password):
        return True
    else:
        return False

# Run app
window = Signup()
window.show()
sys.exit(app.exec())

# Cách chạy file:
    # Bước 1: Chuột phải vào folder muốn chạy
    # Bước 2: Chọn "Open in integrated Terminal"
    # Bước 3: Nhập lệnh "python main.py"