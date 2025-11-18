from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("**********************************")
    print("**1. Them sinh vien**")
    print("**2. Cap nhat thong tin sinh vien theo ID**")
    print("**3. Xoa sinh vien theo ID**")
    print("**4. Tim kiem sinh vien theo ten**")
    print("**5. Hien thi danh sach sinh vien**")
    print("**6. Sap xep sinh vien theo diem trung binh**")
    print("**7. Sap xep sinh vien theo ten**")
    print("**0. Thoat chuong trinh**")
    print("**********************************")

    try:
        key = int(input("Nhap tuy chon: "))
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")
        continue

    if key == 1:
        print("\n1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("Them sinh vien thanh cong")

    elif key == 2:
        if qlsv.so_luong_sinh_vien() > 0:
            try:
                id_update = int(input("Nhập ID sinh viên cần cập nhật: "))
                qlsv.updateSinhVien(id_update)
                print("Cập nhật sinh viên thành công")
            except ValueError:
                print("ID phải là số nguyên!")
        else:
            print("Chưa có sinh viên nào trong danh sách")

    elif key == 3:
        if qlsv.so_luong_sinh_vien() > 0:
            try:
                id_delete = int(input("Nhập ID sinh viên cần xóa: "))
                qlsv.deleteById(id_delete)
            except ValueError:
                print("ID phải là số nguyên!")
        else:
            print("Chưa có sinh viên nào trong danh sách")

    elif key == 4:
        if qlsv.so_luong_sinh_vien() > 0:
            name_search = input("Nhập tên sinh viên cần tìm: ")
            result = qlsv.findByName(name_search)
            if len(result) > 0:
                qlsv.showSinhVien(result)
            else:
                print("Không tìm thấy sinh viên với tên:", name_search)
        else:
            print("Chưa có sinh viên nào trong danh sách")

    elif key == 5:
        if qlsv.so_luong_sinh_vien() > 0:
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Chưa có sinh viên nào trong danh sách")

    elif key == 6:
        if qlsv.so_luong_sinh_vien() > 0:
            qlsv.sortByDiemTB()
            print("Danh sách sinh viên đã được sắp xếp theo điểm trung bình")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Chưa có sinh viên nào trong danh sách")

    elif key == 7:
        if qlsv.so_luong_sinh_vien() > 0:
            qlsv.sortByName()
            print("Danh sách sinh viên đã được sắp xếp theo tên")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Chưa có sinh viên nào trong danh sách")

    elif key == 0:
        print("Thoát chương trình. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
