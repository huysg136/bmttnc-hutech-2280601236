from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxId = 1
        if self.so_luong_sinh_vien() > 0:
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if sv._id > maxId:
                    maxId = sv._id
            maxId += 1
        return maxId

    def so_luong_sinh_vien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        svName = input("Nhập tên sinh viên: ")
        svSex = input("Nhập giới tính sinh viên: ")
        svMajor = input("Nhập ngành học sinh viên: ")
        svDiemTB = float(input("Nhập điểm trung bình sinh viên: "))
        sv = SinhVien(svId, svName, svSex, svMajor, svDiemTB)
        self.xep_loai_hoc_luc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, id):
        sv: SinhVien = self.findById(id)
        if sv:
            sv._name = input("Nhập tên sinh viên: ")
            sv._sex = input("Nhập giới tính sinh viên: ")
            sv._major = input("Nhập ngành học sinh viên: ")
            sv._diemTB = float(input("Nhập điểm trung bình sinh viên: "))
            self.xep_loai_hoc_luc(sv)
            print("Cập nhật sinh viên thành công")
        else:
            print("Không tìm thấy sinh viên với ID:", id)

    def sortByID(self):
        self.listSinhVien.sort(key=lambda sv: sv._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda sv: sv._name.lower(), reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda sv: sv._diemTB, reverse=False)

    def findById(self, id):
        for sv in self.listSinhVien:
            if sv._id == id:
                return sv
        return None

    def findByName(self, name):
        result = []
        for sv in self.listSinhVien:
            if name.lower() in sv._name.lower():
                result.append(sv)
        return result

    def deleteById(self, id):
        sv: SinhVien = self.findById(id)
        if sv:
            self.listSinhVien.remove(sv)
            print(f"Xóa sinh viên ID {id} thành công")
        else:
            print("Không tìm thấy sinh viên với ID:", id)

    def xep_loai_hoc_luc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung Bình"
        else:
            sv._hocLuc = "Yếu"

    def showSinhVien(self, listSV):
        print("{:<5} {:<20} {:<10} {:<15} {:<10} {:<10}".format(
            "ID", "Họ Tên", "Giới Tính", "Ngành Học", "Điểm TB", "Học Lực"
        ))
        if listSV:
            for sv in listSV:
                print("{:<5} {:<20} {:<10} {:<15} {:<10} {:<10}".format(
                    sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc
                ))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
