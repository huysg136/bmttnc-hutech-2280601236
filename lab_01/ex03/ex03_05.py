def dem_so_lan_xuat_hien(lst):
    dem = {}
    for so in lst:
        if so in dem:
            dem[so] += 1
        else:
            dem[so] = 1
    return dem

input_list = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
words = input_list.split()

dem_xuat_hien = dem_so_lan_xuat_hien(words)
print("Số lần xuất hiện của từng từ:", dem_xuat_hien)
