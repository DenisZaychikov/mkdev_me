import datetime
import os.path

current_time = datetime.datetime.now().time()
current_time_minutes = current_time.hour * 60 + current_time.minute + current_time.second / 60
f=open('trendybelly.log')
flag = True
file_length = os.path.getsize('trendybelly.log')
start=0
stop=file_length

mid_num = int((stop + start) // 2)
f.seek(mid_num)
mid_num+=len(f.readline())
f.seek(mid_num)
line=f.readline()

while flag:
    time_from_line = line[(line.find(':') + 1):line.find(' -')]
    hours, minutes, seconds = [int(i) for i in time_from_line.split(':')]
    time_from_line_minutes = hours * 60 + minutes + seconds / 60
    if current_time_minutes - time_from_line_minutes > 5:
        stop=mid_num
        mid_num=int((stop+start)//2)
        f.seek(mid_num)
        mid_num+=len(f.readline())
        f.seek(mid_num)
        line=f.readline()
    elif current_time_minutes - time_from_line_minutes <= 5:
        r_stop=mid_num
        r_start=start
        l_start=mid_num
        l_stop=file_length
        while     
        
        l_start=


