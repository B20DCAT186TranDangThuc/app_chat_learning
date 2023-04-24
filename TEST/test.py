# tách thành một danh sách thành username và Full name
x = "[('thucboykk', 'Dang Thuc'), ('thucboykk2', 'dangthuc'), ('dangthuc02','Dang Thuc'), ('tranthuc', 'Trần Đăng Thức'), ('dangthuc001', 'Dang Thuc 1')]"


lst = eval(x)

for i in lst:
    print(i[0], i[1])