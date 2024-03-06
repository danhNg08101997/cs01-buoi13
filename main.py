"""
2 kiểu dữ liệu
- kiểu dũ liệu cơ sở (primitive type): str, boolean, float, int, None,... tham trị (tham chiếu giá trị vì vậy khi thay đổi thì nó sẽ tạo ra địa chỉ chứa giá trị mới trên biến đó)
=> khi truyền các giá trị input vào hàm là primitive value thì các giá trị gốc không bị thay đổi dù trong hàm đã xử lý thay đổi

kiểu dữ liệu collection (reference value): dict, tuple, set, list,... khi thay đổi các giá trị thì vị trí trong vùng nhớ vẫn không thay đổi, collection trong hàm giống như collection ở ngoài truyền vào
"""
import random

lst = [1,2,3]
print(id(lst))
print(id(lst[0]))
print(id(lst[1]))
print(id(lst[2]))
def tinh_tong_x2(a,b):
    print('id cua a', id(a))
    print('id cua b', id(b))
    a = a * 2
    b = b * 2
    print('id input a sau khi doi', id(a))
    print('id input b sau khi doi', id(b))
    tong = a+b
    return tong
c = 10
d = 20
print(tinh_tong_x2(c,d))
print('id c', id(c))
print('id d', id(d))


def change_list(lst_input):
    lst_input.append(random.randint(0, 1000))
    print('id lst_input', id(lst_input))
    return lst_input

print('id lst', id(lst))
change_list(lst)
print(lst)