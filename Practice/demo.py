import csv
import os
import matplotlib.pyplot as plt

FILE_NAME = "Practice/data.csv"

# ===============================
# HÀM MENU
# ===============================
def show_menu():
    print("================== MENU QUẢN LÝ ===================")
    print("1. Hiển thị danh sách sinh viên")
    print("2. Thêm mới sinh viên")
    print("3. Cập nhật thông tin sinh viên")
    print("4. Xóa sinh viên")
    print("5. Tìm kiếm sinh viên")
    print("6. Sắp xếp danh sách sinh viên")
    print("7. Thống kê điểm TB")
    print("8. Vẽ biểu đồ thống kê điểm TB")
    print("9. Lưu vào file CSV")
    print("10. Thoát")
    print("===================================================")

# ===============================
# HÀM TÍNH ĐIỂM TRUNG BÌNH & XẾP LOẠI
# ===============================
def calc_average(math, physics, chemistry):
    return round((math + physics + chemistry) / 3, 2)

def classify(avg):
    if avg >= 8:
        return "Giỏi"
    elif avg >= 6.5:
        return "Khá"
    elif avg >= 5:
        return "Trung bình"
    else:
        return "Yếu"

# ===============================
# HÀM ĐỌC DỮ LIỆU CSV
# ===============================
def load_data():
    students = []
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            math = float(row["math"])
            physics = float(row["physics"])
            chemistry = float(row["chemistry"])
            avg = calc_average(math, physics, chemistry)
            rank = classify(avg)
            sv = {
                "id": row["id"],
                "name": row["name"],
                "math": math,
                "physics": physics,
                "chemistry": chemistry,
                "avg": avg,
                "rank": rank
            }
            students.append(sv)
    return students

# ===============================
# HÀM LƯU DỮ LIỆU CSV
# ===============================
def save_data(students):
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["id","name","math","physics","chemistry","avg","rank"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    print("✔ Đã lưu dữ liệu vào file CSV!")

# ===============================
# HÀM HIỂN THỊ DANH SÁCH
# ===============================
def show_students(students):
    if not students:
        print("Danh sách trống!")
        return
    print(f"{'Mã SV':<10} {'Họ Tên':<20} {'Toán':<5} {'Lý':<5} {'Hóa':<5} {'TB':<6} {'Xếp loại'}")
    print("-"*60)
    for sv in students:
        print(f"{sv['id']:<10}{sv['name']:<20}{sv['math']:<5}{sv['physics']:<5}{sv['chemistry']:<5}{sv['avg']:<6}{sv['rank']}")
    print()


# ===============================
# HÀM THÊM SINH VIÊN
# ===============================
def add_student(students):
    sid = input("Nhập mã sinh viên: ")
    for sv in students:
        if sv["id"] == sid:
            print("❌ Mã sinh viên đã tồn tại!")
            return

    name = input("Nhập tên sinh viên: ")
    try:
        math = float(input("Điểm Toán: "))
        physics = float(input("Điểm Lý: "))
        chemistry = float(input("Điểm Hóa: "))
    except:
        print("❌ Điểm phải là số!")
        return

    if not all(0 <= d <= 10 for d in [math, physics, chemistry]):
        print("❌ Điểm phải trong khoảng 0-10!")
        return

    avg = calc_average(math, physics, chemistry)
    rank = classify(avg)

    students.append({
        "id": sid,
        "name": name,
        "math": math,
        "physics": physics,
        "chemistry": chemistry,
        "avg": avg,
        "rank": rank
    })
    print("✔ Thêm sinh viên thành công!")

# ===============================
# HÀM CẬP NHẬT SINH VIÊN
# ===============================
def update_student(students):
    sid = input("Nhập mã sinh viên cần sửa: ")
    for sv in students:
        if sv["id"] == sid:
            print("Nhập điểm mới:")
            try:
                math = float(input("Điểm Toán: "))
                physics = float(input("Điểm Lý: "))
                chemistry = float(input("Điểm Hóa: "))
            except:
                print("❌ Điểm phải là số!")
                return
            if not all(0 <= d <= 10 for d in [math, physics, chemistry]):
                print("❌ Điểm phải trong khoảng 0-10!")
                return

            sv["math"] = math
            sv["physics"] = physics
            sv["chemistry"] = chemistry
            sv["avg"] = calc_average(math, physics, chemistry)
            sv["rank"] = classify(sv["avg"])
            print("✔ Cập nhật thành công!")
            return
    print("❌ Không tìm thấy sinh viên!")

# ===============================
# HÀM XÓA SINH VIÊN
# ===============================
def delete_student(students):
    sid = input("Nhập mã sinh viên cần xóa: ")
    for sv in students:
        if sv["id"] == sid:
            confirm = input("Bạn có chắc muốn xóa? (y/n): ")
            if confirm.lower() == "y":
                students.remove(sv)
                print("✔ Đã xóa sinh viên!")
            else:
                print("❌ Hủy xóa.")
            return
    print("❌ Không tìm thấy sinh viên!")

# ===============================
# HÀM TÌM KIẾM SINH VIÊN
# ===============================
def search_student(students):
    keyword = input("Nhập tên hoặc mã SV để tìm: ").lower()
    result = [sv for sv in students if keyword in sv["name"].lower() or keyword == sv["id"].lower()]
    if result:
        show_students(result)
    else:
        print("❌ Không tìm thấy sinh viên!")

# ===============================
# HÀM SẮP XẾP
# ===============================
def sort_students(students):
    print("1. Sắp xếp theo điểm TB giảm dần")
    print("2. Sắp xếp theo tên A → Z")
    choice = input("Chọn: ")

    # Tạo bản copy của danh sách để sort, giữ nguyên danh sách gốc
    sorted_list = students.copy()

    if choice == "1":
        students.sort(key=lambda x: x["avg"], reverse=True)
        print("✔ Sắp xếp theo điểm TB giảm dần!")
    elif choice == "2":
        students.sort(key=lambda x: x["name"])
        print("✔ Sắp xếp theo tên A → Z!")
    else:
        print("❌ Lựa chọn không hợp lệ!")
        return
    show_students(sorted_list)

# ===============================
# HÀM THỐNG KÊ
# ===============================
def statistics(students):
    stats = {"Giỏi":0, "Khá":0, "Trung bình":0, "Yếu":0}
    for sv in students:
        stats[sv["rank"]] += 1
    print("===== THỐNG KÊ XẾP LOẠI =====")
    for loai, so in stats.items():
        print(f"{loai}: {so} sinh viên")
    return stats

# ===============================
# HÀM VẼ BIỂU ĐỒ
# ===============================
def draw_chart(stats):
    print("Chọn loại biểu đồ:")
    print("1. Pie chart")
    print("2. Bar chart")
    choice = input("Chọn: ")
    labels = list(stats.keys())
    values = list(stats.values())
    if choice == "1":
        plt.pie(values, labels=labels, autopct="%1.1f%%")
        plt.title("Tỷ lệ xếp loại sinh viên")
    elif choice == "2":
        plt.bar(labels, values)
        plt.title("Tỷ lệ xếp loại sinh viên")
        plt.ylabel("Số sinh viên")
    else:
        print("❌ Lựa chọn không hợp lệ!")
        return
    plt.show()

# ===============================
# CHƯƠNG TRÌNH CHÍNH
# ===============================
def main():
    students = load_data()
    print("DEBUG: Danh sách sau khi load:", students)
    while True:
        show_menu()
        choice = input("Nhập lựa chọn (1 - 10): ")

        if choice == "1":
            show_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            search_student(students)
        elif choice == "6":
            sort_students(students)
        elif choice == "7":
            statistics(students)
        elif choice == "8":
            stats = statistics(students)
            draw_chart(stats)
        elif choice == "9":
            save_data(students)
        elif choice == "10":
            save_data(students)
            print("Thoát chương trình. Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng nhập lại!")

if __name__ == "__main__":
    main()
