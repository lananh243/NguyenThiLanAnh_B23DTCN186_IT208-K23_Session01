firstNumber = 20
secondNumber = 10.6
userName = "Nguyễn Lan Anh"
isMarried = True

print(firstNumber)

# Nối chuỗi trong python
print("Tôi tên là:", userName, ", Năm nay tôi", firstNumber)
print(f"Tôi tên là: {userName}, năm nay tôi {firstNumber} tuổi")

# Ép kiểu dữ liệu
print(str(123)) # Ép giá trị kiểu int = 123 sang chuỗi

# Kiểm tra kiểu dữ liệu của 1 biến
print(f"Kiểu dữ liệu của biến firstNumber là: {type(firstNumber)}")

# Nhập xuất dữ liệu
# numberA = input("Enter number A: ")
# numberB = input("Enter number B: ")

# print(f"Kiểu dữ liệu là: {type(numberA)} - {type(numberB)}")

# print(f"{numberA} + {numberB} = {int(numberA) + int(numberB)}")

# Biến trong python
a = 10
print(f"Địa chỉ của a trước: {id(a)}")
a = 20
print(f"Địa chỉ của a sau: {id(a)}")
b = a
print(f"Địa chỉ của biến a trong bộ nhớ: {id(a)}")
print(f"Địa chỉ của biến b trong bộ nhớ: {id(b)}")
print(id(a) == id(b))