import os.path


def get_seq(middle_number):
    f.seek(middle_number)
    return f.read(len(pattern))


flag = True
start = 0
f = open('file1.txt')
pattern = 'egtu'
file_length = os.path.getsize('file1.txt')
middle_number = int(((file_length / len(pattern)) // 2) * len(pattern))

while flag:
    seq = get_seq(middle_number)
    if seq > pattern:
        middle_number = (middle_number - start) // 2
    elif seq < pattern:
        middle_number = start
        flag = False
        seq = get_seq(middle_number)
        while seq < pattern and middle_number != file_length:
            print(seq)
            middle_number += len(pattern)
            seq = get_seq(middle_number)
