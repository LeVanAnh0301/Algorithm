# -*- coding: utf-8 -*-
"""Thuật  Toán Tìm Kiếm .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EtGdl8CloOFimk5TKMI04Nc_65eyGhk-

# 2. Thuật Toán Tìm Kiếm Nhị Phân (Binary Search)

**Bài toán**: Tìm kiếm vị trí của một phần tử dựa vào giá trị của nó trên một *danh sách đã được sắp xếp*.  
**Cách hoạt động**:
Giả sử danh sách đầu vào được sắp xếp theo thứ tự tăng dần.  
1. Ta định nghĩa khoảng tìm kiếm là toàn bộ mảng.
2. Thực hiện lặp lại các bước sau:  
   2.1. So sánh giá trị ở chính giữa khoảng tìm kiếm với giá trị cần tìm:
      + Nhỏ hơn: Mọi phần tử bên trái giá trị giữa đều nhỏ hơn giá trị cần tìm. Do đó, ta thu hẹp khoảng tìm kiếm lại thành nửa bên phải khoảng tìm kiếm.
      + Lớn hơn: Mọi phần tử bên phải giá trị giữa đều lớn hơn giá trị cần tìm. Do đó, ta thu hẹp khoảng tìm kiếm lại thành nửa bên trái khoảng tìm kiếm.
      + Bằng: Kết thúc vòng lặp và trả về vị trí tìm thấy.  
      
   2.2. Vòng lặp kết thúc sau khi khoảng tìm kiếm chỉ còn một phần tử và vẫn không tìm thấy giá trị.
3. Trả về "không tìm thấy" sau khi kết thúc vòng lặp.

**Độ phức tạp**:
- Thời gian: *O(log(n))*, do mỗi lần lặp ta thu hẹp một nửa khoảng tìm kiếm.  
  Chứng minh: Do mỗi lần lặp ta thu hẹp một nửa khoảng tìm kiếm (nếu chưa tìm thấy), ta có kích thước của khoảng tìm kiếm sau mỗi lần lặp là:
\begin{equation} n → \frac{n}{2} → \frac{n}{4} → \frac{n}{8} → ... → 2 → 1 \end{equation}
Ở mỗi lần lặp, ta thực hiện một phép so sánh và một vài phép gán với tổng độ phức tạp là *O(1)*. Do đó, độ phức tạp của thuật toán là *O(k)*, với *k* là số lần lặp trong trường hợp xấu nhất.  
Sau khi thu hẹp một nửa khoảng tìm kiếm *k* lần thì kích thước khoảng tìm kiếm còn 1 phần tử, như vậy ta có:
\begin{equation} \frac{n}{2^k} = 1 <=> k = log_2(n) \end{equation}
Như vậy độ phức tạp về thời gian của thuật toán tìm kiếm nhị phân là *O(log<sub>2</sub>(n))* = *O(log(n))*
- Không gian: *O(n)*, để lưu danh sách các giá trị.
"""

# Hàm tìm index nơi có số cần tìm
def binary_search(arr, m ): # arr là dãy số đã sắp xếp , m là giá trị cần tìm trong dãy số 
  left=0
  right=len(arr)-1
  while left<= right:
     mid = (left+right)//2 #Lưu ý đây là chỉ số 
     if arr[mid] < m:
       left= mid+1
     elif arr[mid]>m:
       right= mid-1
     else:
       return mid
  return -1  # không tìm được 
# Hàm tìm số khi đã biết chỉ số của nó.
def find_number(arr,mi):
  index= binary_search(arr, mi )
  if index != -1:
    print('Phần tử có giá trị' + mi +'nằm ở vị trí'+ index)
  else:
      print("không có phần tử trong dãy")

# Thử xét với một ví dụ sau:
arr= [1,2,5,6,17,23,46,55,88,99,100]
find_number(arr,50)

"""Bên trên là Cách 1 tìm kiếm theo cách sử dụng vòng lặp. 

Sau đây là cách 2 Sử dụng đệ quy (Recursion).Lát nữa mình sẽ phân tích vì sao nên sử dụng đệ quy.
## Tìm Kiếm Nhị Phân Bằng Đệ Quy

**Cách hoạt động**:
Cách hoạt động của thuật toán tìm kiếm nhị phân vẫn giữ nguyên, ta chỉ thay đổi code bằng cách gọi đệ quy mỗi lần cập nhật khoảng tìm kiếm.  
  
**Độ phức tạp**:
- Thời gian: *O(log(n))*.
- Không gian: *O(n+log(n))* = *O(n)*. Ta có *log(n)* do mỗi lần gọi đệ quy, ta phải lưu lại trong bộ nhớ stack để chờ kết quả.
"""

#Hàm này trả về index của giá trị x còn không tìm được thì trả về -1 

def binarySearch(arr, l, r, x): # l : left , r:right 
  
    # Check base case
    if r >= l:
  
        mid = l + (r - l) // 2
  
        # Nếu phần tử đó đúng với giá trị ở giữa 
        if arr[mid] == x:
            return mid
  
        # Nếu phần tử đó nhỏ hơn phần tử ở giữa 
        # thì ta cần so sảnh tiếp tục thực hiện các bước tương tự với dãy mới : là dãy nằm bên trái mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
  
       # ngược lại với trường hợp trên
        else:
            return binarySearch(arr, mid + 1, r, x)
  
    else:
       
        return -1
  
  
# Ví dụ với một dãy số 
arr = [2, 3, 4, 10, 40]
x = 10
  
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
  
if result != -1:
    print("Index của giá trị trong dãy: % d" % result)
else:
    print("Phần tử ko xuất hiện trong dãy")

"""# 3. Đệ Quy

Đệ quy là một thuật ngữ chỉ việc một hàm tự gọi chính nó. Thuật toán đệ quy thường dùng để giải quyết những bài toán có thể xử lý bằng cách đưa về các bài toán nhỏ hơn cùng loại.
### Tại Sao Phải Sử Dụng Đệ Quy?

Mọi thuật toán đệ quy đều có thể được viết dưới dạng vòng lặp. Bên cạnh đó, nhược điểm của đệ quy là nguy cơ cao tràn bộ nhớ stack.  

Tuy nhiên, một số thuật toán có thể được code nhanh và gọn gàng hơn nếu dùng phương pháp đệ quy. Ví dụ, một số thuật toán dùng để:  
- Xử lý trên cây thư mục (tìm kiếm, xóa file và thư mục,...)
- Tìm đường đi trên đồ thị
- Sắp xếp dãy  

Do đó, tùy theo bài toán mà ta chọn phương pháp phù hợp để giải quyết.

## Ví dụ thực hành . Tìm Ước Chung Lớn Nhất

Có nhiều cách để tìm ước chung lớn nhất của hai số nguyên dương, một trong số đó là sử dụng *Giải thuật Euclid*:
> Cho hai số nguyên dương *a, b* > 0. Gọi *r* là phần dư của phép chia *a/b*, ước chung lớn nhất của *a* và *b* được tính bằng công thức:
![](./assets/gcd.webp)


**Yêu cầu**: Cho hai số nguyên dương *0 < a, b < 10^9*. Tìm ước chung lớn nhất của *a* và *b*

**Ví dụ**:  
- Input: 20, 6
- Output: 2

Nói thêm một chút về thuật toán Euclid
"""

