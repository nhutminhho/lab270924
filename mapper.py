#!/usr/bin/env python3
import sys

# Đọc từng dòng dữ liệu từ stdin
for line in sys.stdin:
    # Loại bỏ khoảng trắng đầu và cuối dòng
    line = line.strip()
    
    # Tách dòng thành các từ
    words = line.split()
    
    # Phát ra từng từ kèm giá trị 1
    for word in words:
        print(f'{word}\t1')
