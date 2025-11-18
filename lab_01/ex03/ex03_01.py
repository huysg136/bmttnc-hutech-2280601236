def tinh_tong_so_chan(lst):
    tong = 0
    for so in lst:
        if so % 2 == 0:
            tong += so
    return tong

input_list = input("Nhập danh sách số nguyên, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

tong_so_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn là:", tong_so_chan)