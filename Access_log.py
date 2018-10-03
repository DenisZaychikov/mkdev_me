import datetime

current_time = datetime.datetime.now().time()
current_time_minutes = current_time.hour * 60 + current_time.minute + current_time.second / 60
filename = input() + '.log'
with open(filename) as file:
    for line in file:
        time_from_line = line[(line.find(':') + 1):line.find(' -')]
        hours, minutes, seconds = [int(i) for i in time_from_line.split(':')]
        time_from_line_minutes = hours * 60 + minutes + seconds / 60
        if current_time_minutes - time_from_line_minutes <= 5:
            print(line)


