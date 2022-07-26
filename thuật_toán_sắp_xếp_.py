# -*- coding: utf-8 -*-
"""Thuật Toán Sắp Xếp .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18E0RzaMM3UkIJ_OZJc_FdrLN2jrCaU2g

# 1. Selection Sort
**Cách tiếp cận**:  
Selection Sort sử dụng cách tiếp cận đơn giản nhất:
- Tìm phần tử nhỏ nhất và chuyển lên đầu dãy.
- Sau đó, tiếp tục tìm phần tử nhỏ nhất trong phần còn lại của dãy và chuyển lên vị trí thứ hai.
- Tiếp tục như vậy đến khi hết dãy. 
**Cách hoạt động**:  
- Thuật toán Selection Sort chia danh sách cần sắp xếp thành 2 phần: đã được sắp xếp (nằm bên trái) và chưa được sắp xếp (bên phải).
- Ở mỗi lần lặp, thuật toán tìm phần tử nhỏ nhất của phần chưa sắp xếp để đưa vào cuối phần đã sắp xếp.  

**Độ phức tạp thời gian**:
- Thuật toán tìm min *n-1* lần. Lần thứ nhất tìm trên dãy có *n* phần tử, lần thứ hai trên *n-1* phần tử, lần thứ ba trên *n-2* phần tử,...  
- Bỏ qua các lệnh gán và swap (do mỗi lệnh có độ phức tạp *O(1)*), ta có thể tính xấp xỉ số câu lệnh thuật toán cần thực hiện là: \begin{equation} n + (n-1) + (n-2) + ... + 3 + 2 = \frac{(n+2)(n-1)}{2} = \frac{n^2+n-2}{2} \end{equation}
- Do đó, thuật toán Selection Sort có độ phức tạp về thời gian là *O(n<sup>2</sup>)*  

**Độ phức tạp không gian**:
- Thuật toán có độ phức tạp về không gian là *O(n)* để lưu trữ danh sách cần sắp xếp.
"""

# Đoan code này để taoh một hàm trừu tượng hóa đồ thị với thư viện matplotlib 
import matplotlib.pyplot as plt

def show_list(arr, title=''):
  #Khai báo 2 thành phần sau : fig 
    fig, ax = plt.subplots(figsize=(20, 4))
    #plt.subplots()là một hàm trả về một bộ giá trị chứa (các) đối tượng hình và trục.
    ax.bar(range(len(arr)), arr)
    ax.set_title(title)
    ax.set_xlabel('index')
    ax.set_xticks(range(len(arr)))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
 
    plt.show()

# Hàm tìm chỉ số  phần tử min ( sắp xếp các phần tử để đưa phần tử min đó lên đầu dãy)
def find_min(data_list, from_index):
    min_ind = from_index
    for i in range(from_index+1, len(data_list)):
        if data_list[i] < data_list[min_ind]:
            min_ind = i
    return min_ind


def selection_sort(data_list):
    for i in range(len(data_list)-1):
        min_ind = find_min(data_list, i)  # lấy index min 
        if min_ind != i:                  # Đổi vị trí 2 phần tử liền kề nếu thõa mãn điều kiện 
            data_list[i], data_list[min_ind] = data_list[min_ind], data_list[i]

num_list=[1,6,3,4,5,11,24,33,88,36,44,55,78]

selection_sort(num_list)


print("Sau khi sắp xếp:  {}".format(num_list))
show_list(num_list, title='Dãy sau sắp xếp')

"""**Cách hoạt động:**

Thuật toán Selection Sort chia danh sách cần sắp xếp thành 2 phần: đã được sắp xếp (nằm bên trái) và chưa được sắp xếp (bên phải).

Ở mỗi lần lặp, thuật toán tìm phần tử nhỏ nhất của phần chưa sắp xếp để đưa vào cuối phần đã sắp xếp.

**Độ phức tạp thời gian:**

Thuật toán tìm min n-1 lần. Lần thứ nhất tìm trên dãy có n phần tử, lần thứ hai trên n-1 phần tử, lần thứ ba trên n-2 phần tử,...

Bỏ qua các lệnh gán và swap (do mỗi lệnh có độ phức tạp O(1)), ta có thể tính xấp xỉ số câu lệnh thuật toán cần thực hiện là:
n+(n−1)+(n−2)+...+3+2=(n+2)(n−1)2=n2+n−22 

Do đó, thuật toán Selection Sort có độ phức tạp về thời gian là O(n2)

**Độ phức tạp không gian:**

Thuật toán có độ phức tạp về không gian là O(n) để lưu trữ danh sách cần sắp xếp.

# 2. Bubble Sort

**Bài toán**: Bubble Sort (sắp xếp nổi bọt) cũng xử lý bài toán như Selection Sort, nhưng với cách tiếp cận khác.

Bubble Sort sử dụng **cách tiếp cận** sau:
- Xét lần lượt các cặp 2 phần tử liên tiếp. Nếu phần tử đứng sau nhỏ hơn phần tử đứng trước, ta đổi chỗ 2 phần tử đó.
- Giả sử ta xét các cặp theo thứ tự index (0, 1), (1, 2), (2, 3),... thì sau một lần xét qua dãy, phần tử có giá trị lớn nhất sẽ nằm ở cuối dãy.
- Như vậy, lúc này dãy cần sắp xếp cũng được chia thành 2 phần: đã được sắp xếp (nằm bên phải) và chưa được sắp xếp (bên trái). Ta tiếp tục thực hiện việc xét các cặp ở phần chưa được sắp xếp để đưa phần tử lớn nhất vào phần đã được sắp xếp.  

Bubble Sort có tên như vậy vì sau mỗi lượt xét các cặp ở phần chưa được sắp xếp, một phần tử sẽ "nổi lên" ở phần đã được sắp xếp. Ngoài ra, Bubble Sort còn có tên là Sinking Sort (chìm xuống).
"""

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):  # i is the index between the sorted and unsorted part
        for j in range(i):              # loop j through the pairs in the unsorted part
            if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]

num_list=[1,6,3,4,5,11,24,33,88,36,44,55,78]
bubble_sort(num_list)


print("Sau khi sắp xếp:  {}".format(num_list))
show_list(num_list, title='Dãy sau sắp xếp')

"""**Độ phức tạp thời gian**:
- Thuật toán Bubble Sort chạy vòng lặp trên biến i *n-1* lần. Lần thứ nhất kiểm tra *n-1* cặp số, lần thứ hai kiểm tra *n-2* cặp, lần thứ ba *n-3* cặp,...
- Bỏ qua các lệnh gán và swap, ta có thể tính xấp xỉ số câu lệnh thuật toán cần thực hiện là: \begin{equation} (n-1) + (n-2) + ... + 2 + 1 = \frac{n(n-1)}{2} = \frac{n^2-n}{2} \end{equation}
- Do đó, thuật toán Bubble Sort có độ phức tạp về thời gian là *O(n<sup>2</sup>)*  


**Độ phức tạp không gian**:
- Thuật toán có độ phức tạp về không gian là *O(n)* để lưu trữ danh sách cần sắp xếp.

# **3. Insertion Sort**
Bài toán: Insertion Sort (sắp xếp chèn) cũng là một cách tiếp cận khác của thuật toán sắp xếp.

Insertion Sort sử dụng cách tiếp cận sau:

Insertion sort cũng chia danh sách dữ liệu thành 2 phần: phần đã được sắp xếp nằm bên trái và chưa được sắp xếp nằm bên phải.

Giả sử ta đã sắp xếp xong i phần tử của dãy. Ta tiếp tục sắp xếp bằng cách tìm vị trí phù hợp của phần tử thứ i+1 và "chèn" nó vào đó.

Ta bắt đầu thuật toán bằng cách xem phần đã được sắp xếp là dãy gồm một phần tử đầu tiên, sau đó thực hiện chèn phần tử thứ 2, 3, 4,... vào dãy đã sắp xếp.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):  d
        j = i
        while j > 0 and arr[j] < arr[j-1]: 
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

num_list=[1,6,3,4,5,11,24,33,88,36,44,55,78]
insertion_sort(num_list)


print("Sau khi sắp xếp:  {}".format(num_list))
show_list(num_list, title='Dãy sau sắp xếp')