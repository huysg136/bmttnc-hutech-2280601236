so_gio_lam = float(input("Nhập số giờ làm việc trong tháng: "))
luong_mot_gio = float(input("Nhập lương theo giờ: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = (gio_tieu_chuan * luong_mot_gio) + (gio_vuot_chuan * luong_mot_gio * 1.5)
print("Số tiền thực lĩnh trong tháng là:", thuc_linh)