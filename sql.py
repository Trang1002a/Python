# python -m pip install mysql-connector
# https://viblo.asia/p/a-simple-crud-application-using-python-and-mysql-Eb85oxgWK2G
import mysql.connector
import datetime

def connect_mysql():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    return connection

def create_database(db):
    con = connect_mysql()
    cursor = con.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS ' + db)
    cursor.execute('USE ' +db)
    print('Cơ sở dữ liệu là: ', db)
    cursor.execute('CREATE TABLE IF NOT EXISTS employee(employeeId varchar(10) primary key, fullName varchar(100), birthday date, phone varchar(100))')
    return con

def insert(id, name, birthday, phone, con):
    cursor = con.cursor()
    cursor.execute("INSERT INTO employee values(%s,%s,%s,%s)", (id, name, birthday, phone))
    con.commit()
    cursor.close()

def delete_employee(id, con):
    cursor = con.cursor()
    cursor.execute("DELETE FROM employee WHERE employeeId=%s", (id,))
    con.commit()
    # cursor.close()
    if(cursor.rowcount>0):
        print("Xóa thành công")
    else:
        print("Mã không tồn tại")

def show_all(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM employee")
    records = cursor.fetchall()
    print("---------------- DANH SÁCH NHÂN VIÊN ------------------")
    for r in records:
        print(r[0], "\t", r[1], "\t", r[2], "\t", r[3])
    cursor.close()

def input_employee(con):
    print("--------------- DANH SÁCH NHÂN VIÊN --------------")
    while(True):
        id = input("Mã sinh viên: ")
        name = input("Tên sinh viên: ")
        birthday = datetime.datetime.strptime(input("Ngày sinh dd/mm/yyyy: "), "%d/%m/%Y")
        phone = input("Điện thoại: ")
        insert(id, name, birthday, phone, con)
        choose = input("Bạn có muốn nhập tiếp không? Y/N: ")
        if(choose == "n" or choose == "N"):
            break
    print("---------------------------------------")


con= create_database("lab8")
while(True):
    print("1. Nhập nhân viên")
    print("2. Hiển thị tất cả nhân viên")
    print("3. Xóa nhân viên")
    print("4. Thoát")
    choose = input("Chọn một chức năng: ")
    if(choose == "1"):
        input_employee(con)
    elif(choose == "2"):
        show_all(con)
    elif(choose == "3"):
        id = input("Nhập mã cần xóa: ")
        delete_employee(id, con)
    elif(choose == "4"):
        break
    else:
        print("Bạn chọn sai rồi")
print("Kết thúc chương trình")
