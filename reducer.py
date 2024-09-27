#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None

# Đọc từng dòng dữ liệu từ stdin
for line in sys.stdin:
    # Loại bỏ khoảng trắng đầu và cuối dòng
    line = line.strip()

    # Tách từ và số đếm dựa trên ký tự tab
    word, count = line.split('\t')

    # Chuyển đổi số đếm từ chuỗi sang số nguyên
    count = int(count)

    # Nếu từ hiện tại giống từ trước đó, cộng dồn số đếm
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # In ra từ trước đó và tổng số đếm
            print(f'{current_word}\t{current_count}')
        current_word = word
        current_count = count

# In ra từ cuối cùng và tổng số đếm
if current_word == word:
    print(f'{current_word}\t{current_count}')
