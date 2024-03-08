from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMessageBox, QWidget, QFileDialog 
from PyQt6 import uic
import re
import sys

# Lớp chứa giao diện đăng nhập
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/login.ui", self)
        
        # Bắt sự kiện click chuột vào nút login
        self.btnLogin.clicked.connect(self.check_login)
        self.btn_register.clicked.connect(self.showRegister)
      
    def check_login(self):
        # Lấy thông tin email và mật khẩu từ người dùng
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        
        # Kiểm tra email và mật khẩu có được nhập hay không
        if not email: 
            msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        
        # Kiểm tra email và mật khẩu có khớp với tài khoản admin hay không
        if email == "admin@example.com" and password == "admin":
            # Nếu đăng nhập thành công, chuyển sang giao diện chính (Main)
            self.close()
            mainPage.show()  
        else:
            # Nếu đăng nhập không thành công, hiển thị thông báo lỗi
            msg_box.setText("Email hoặc mật khẩu không đúng!")
            msg_box.exec()
            
    def showRegister(self):
        registerPage.show()
        self.close()

# Lớp chứa giao diện đăng ký
class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/register.ui", self)
        self.name = ""
        
        # Bắt sự kiện click chuột vào nút đăng ký
        self.btnRegister.clicked.connect(self.Register)
        self.btn_login.clicked.connect(self.showLoginPage)
    
    def Register(self):
        # Lấy thông tin email, username và mật khẩu từ người dùng
        self.name = self.txtFullName.text()
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        
        # Kiểm tra các trường thông tin có được nhập hay không
        if not self.name:
            msg_box.setText("Vui lòng nhập tên!")
            msg_box.exec()
            return
        if not email: 
            msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        if not self.checkBox.isChecked():
            msg_box.setText("Vui lòng đọc và đồng ý các điều khoản của AdoptMate!")
            msg_box.exec()
            return
        
        # Đóng giao diện đăng ký và hiển thị giao diện lựa chọn đăng ký (registerOption)
        mainPage.lbUsername.setText(self.name)
        mainPage.show()
        self.close()
        
    def showLoginPage(self):
        # Hiển thị giao diện đăng nhập (loginWindow)
        loginPage.show()
        self.close()

# Lớp chứa giao diện chính
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/main.ui", self)

        # Hiển thị bộ lọc danh sách dog
        self.icon_dog.clicked.connect(self.dog_filter)
        self.btn_opt_dog.clicked.connect(self.dog_filter)
        # Hiển thị bộ lọc danh sách cat
        self.icon_cat.clicked.connect(self.cat_filter)
        self.btn_opt_cat.clicked.connect(self.cat_filter)
        # Hiển thị bộ lọc danh sách các thú cưng khác
        self.icon_other.clicked.connect(self.pet_filter)
        self.btn_opt_other.clicked.connect(self.pet_filter)
        #Hiển thị thông tin thú cưng nổi bật
        self.btn_dog.clicked.connect(self.showDetail1)
        self.btn_dogName.clicked.connect(self.showDetail1)
        
    def dog_filter(self):
        dogfilter.show()
        
    def cat_filter(self):
        catfilter.show()
    
    def pet_filter(self):
        petfilter.show()
        
    def showDetail1(self):
        dogDetail1.show()
        self.close()
        
# Lớp chứa bộ lọc danh sách Dog
class Dog_Filter(QtWidgets.QDialog):
    def __init__(self):
        super(Dog_Filter, self).__init__()
        pageName = "gui/dog_filter.ui"
        uic.loadUi(pageName, self)  
        
        self.btn_back.clicked.connect(self.close)  
        self.btn_close.clicked.connect(self.close)  
        self.btn_continue.clicked.connect(self.dog)

    def dog(self):
        dog.show()
        mainPage.close()
        self.close()
    
# Lớp chứa bộ lọc danh sách Cat
class Cat_Filter(QtWidgets.QDialog):
    def __init__(self):
        super(Cat_Filter, self).__init__()
        pageName = "gui/cat_filter.ui"
        uic.loadUi(pageName, self)  
        
        self.btn_back.clicked.connect(self.close)  
        self.btn_close.clicked.connect(self.close)  
        self.btn_continue.clicked.connect(self.cat)

    def cat(self):
        cat.show()
        mainPage.close()
        self.close()

# Lớp chứa bộ lọc danh sách Pet
class Pet_Filter(QtWidgets.QDialog):
    def __init__(self):
        super(Pet_Filter, self).__init__()
        pageName = "gui/animal_filter.ui"
        uic.loadUi(pageName, self)  
        
        self.btn_back.clicked.connect(self.close)  
        self.btn_close.clicked.connect(self.close)
        self.btn_rabbit.clicked.connect(self.showNotFound)
        self.btn_rabbitName.clicked.connect(self.showNotFound)
        self.btn_pig.clicked.connect(self.showNotFound)
        self.btn_pigName.clicked.connect(self.showNotFound)
        self.btn_bird.clicked.connect(self.showNotFound) 
        self.btn_birdName.clicked.connect(self.showNotFound)  
        self.btn_hamster.clicked.connect(self.showNotFound) 
        self.btn_hamsterName.clicked.connect(self.showNotFound) 

    def showNotFound(self):
        notFound.show()
        mainPage.close()
        self.close()

# Lớp chứa giao diện danh sách Dog
class Dog(QtWidgets.QMainWindow):
    def __init__(self):
        super(Dog, self).__init__()
        pageName = "gui/dog.ui"
        uic.loadUi(pageName, self) 
        
        self.icon_state_list = [False] * 6  # Ban đầu, tất cả các icon đều chưa được chọn
        self.heart_buttons = [self.heart1, self.heart2, self.heart3, self.heart4, self.heart5, self.heart6]

        for button in self.heart_buttons:
            button.clicked.connect(self.toggleHeartIcon)
        
        self.btn_back.clicked.connect(self.showMain)
        self.btn_dog1.clicked.connect(self.showDetail)
        self.btn_name_dog1.clicked.connect(self.showDetail)

    def toggleHeartIcon(self):
        button = self.sender()  # Lấy thông tin về nút gửi sự kiện
        if button in self.heart_buttons:  # Kiểm tra nút có trong danh sách
            button_index = self.heart_buttons.index(button)
            if not self.icon_state_list[button_index]:
                iconheart = QtGui.QIcon()
                iconheart.addPixmap(QtGui.QPixmap("img/icons8-heart-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(iconheart)
                self.icon_state_list[button_index] = True
            else:
                iconheart = QtGui.QIcon()
                iconheart.addPixmap(QtGui.QPixmap("img/tyn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(iconheart)
                self.icon_state_list[button_index] = False
                
    def showMain(self):
        self.close() 
        mainPage.show()
        
    def showDetail(self):
        dogDetail.show()

# Lớp chứa giao diện danh sách Cat
class Cat(QtWidgets.QMainWindow):
    def __init__(self):
        super(Cat, self).__init__()
        pageName = "gui/cat.ui"
        uic.loadUi(pageName, self) 
        
        self.icon_state_list = [False] * 6  # Ban đầu, tất cả các icon đều chưa được chọn
        self.heart_buttons = [self.heart1, self.heart2, self.heart3, self.heart4, self.heart5, self.heart6]

        for button in self.heart_buttons:
            button.clicked.connect(self.toggleHeartIcon)
        self.btn_back.clicked.connect(self.showMain)
        
    #Viết hàm để thay đổi hình dạng trái tim khi người dùng click vào
    def toggleHeartIcon(self):
        button = self.sender()  # Lấy thông tin về nút gửi sự kiện
        if button in self.heart_buttons:  # Kiểm tra nút có trong danh sách
            button_index = self.heart_buttons.index(button)
            #Kiểm tra nếu thú cưng chưa được thêm vào danh sách yêu thích khi bấm vào icon trái tym sẽ full màu
            if not self.icon_state_list[button_index]:
                iconheart = QtGui.QIcon()
                iconheart.addPixmap(QtGui.QPixmap("img/icons8-heart-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(iconheart)
                self.icon_state_list[button_index] = True
            ##Kiểm tra nếu thú cưng đã được thêm vào danh sách yêu thích khi bấm vào icon trái tym sẽ không full mày
            else:
                iconheart = QtGui.QIcon()
                iconheart.addPixmap(QtGui.QPixmap("img/tyn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(iconheart)
                self.icon_state_list[button_index] = False
    
    def showMain(self):
        self.close() 
        mainPage.show()       
                      
# Lớp chứa giao diện chi tiết Dog
class Dog_Detail(QtWidgets.QMainWindow):
    def __init__(self):
        super(Dog_Detail, self).__init__()
        pageName = "gui/dog_detail.ui"
        uic.loadUi(pageName, self)
        #Chọn trờ về trang main 
        self.btn_back.clicked.connect(self.close)
        
    def close(self):
        dog.show()
        self.close() 
        
# Lớp chứa giao diện chi tiết Dog 1
class Dog_Detail1(QtWidgets.QMainWindow):
    def __init__(self):
        super(Dog_Detail1, self).__init__()
        pageName = "gui/dog_detail1.ui"
        uic.loadUi(pageName, self) 
        #Chọn trờ về trang main 
        self.btn_back.clicked.connect(self.closePage)
        
    def closePage(self):
        mainPage.show() 
        self.close()        

# Lớp chứa giao diện thông báo không tìm thấy
class NotFound(QtWidgets.QMainWindow):
    def __init__(self):
        super(NotFound, self).__init__()
        pageName = "gui/notFound.ui"
        uic.loadUi(pageName, self)
        
        self.btn_back.clicked.connect(self.showMainWindow)
        
    def showMainWindow(self):
        mainPage.show()
        self.close()
          
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #Tạo các đối tượng tương ứng với các trang giao diện
    loginPage = Login()
    loginPage.show()
    registerPage = Register()
    mainPage = Main()
    dog = Dog()
    dogDetail = Dog_Detail()
    dogDetail1 = Dog_Detail1()
    dogfilter = Dog_Filter()
    catfilter = Cat_Filter()
    petfilter = Pet_Filter()
    cat = Cat()
    notFound = NotFound()
    
    # Thiết lập hộp thoại thông báo lỗi
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Lỗi")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    
    app.exec()