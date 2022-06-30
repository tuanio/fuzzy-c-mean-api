Khoa học dữ liệu: Nhập môn lập trình, toán rời rạc, khai thác dữ liệu, cơ sở dữ liệu
Hệ thống thông tin: Cơ sở dữ liệu, hệ quản trị cơ sở dữ liệu, nhập môn lập trình, cấu trúc dữ liệu và giải thuật
Công nghệ phần mềm: Nhập môn lập trình, lập trình hướng đối tượng, cơ sở dữ liệu
Mạng máy tính: Kiến trúc máy tính, mạng máy tính, nhập môn lập trình, hệ điều hành

# Những môn yêu cầu nhập vào
nhập môn lập trình
toán rời rạc
khai thác dữ liệu
cơ sở dữ liệu
hệ quản trị cơ sở dữ liệu
cấu trúc dữ liệu và giải thuật
lập trình hướng đối tượng 
kiến trúc máy tính
mạng máy tính
hệ điều hành

# Requirements:
- Yêu cầu sinh viên nhập điểm của các môn trên.
    + không có điểm thì thay bằng 5 (lúc nhập).

# Database cho hệ thống
khoa học dữ liệu: 1, 5, 8
hệ thống thông tin: 1, 2, 6

1: nhập môn lập trình, ngôn ngữ lập trình, giới thiệu lập trình, lập trình C, lập trình python
- Từ data excel -> import vào database điểm của sinh viên đống điểm đó
- Tạo model fuzzy c mean dựa trên data đã import vào.

Bảng:
- Khóa
    + id khóa: 1
    + mã số khóa: 9
    + id chương trình đào tạo
- Sinh viên:
    + id sinh viên
    + tên sinh viên
    + id khóa
- Môn học:
    + id môn học
    + tên môn học
    + id chương trình đào tạo
- Điểm:
    + id sinh viên
    + id môn học
    + điểm
- Chuyên ngành:
    + id chuyên ngành
    + tên chuyên ngành
- Chương trình đào tạo
    + id chương trình đào tạo
    + mã số chương trình đào tạo
    + tên chương trình đào tạo
- Xét chuyên ngành:
    + id xét chuyên ngành
    + id chuyên ngành: 1
    + id chương trình đào tạo
    + id của môn cần xét: id của môn nhập môn lập trình, id của môn toán rời rạc

# Set environment

- Powershell: `$env:DATABASE_URL = "postgresql://postgres:TSnXnLIazWq1U6r4ds3G@containers-us-west-58.railway.app:7485/railway"`