number_str = input("Nhập một số thập phân: ")

# Chuyển chuỗi sang số thực (float)
number_float = float(number_str)

# Làm tròn số đến 1 chữ số thập phân
rounded_number = round(number_float, 1)

# Chuyển số đã làm tròn thành số nguyên
integer_number = int(round(rounded_number))

print(f"Số sau khi làm tròn và chuyển thành số nguyên: {integer_number}")
