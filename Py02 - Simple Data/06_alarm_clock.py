hour = int(input('Hour: '))
minutes = int(input('Minutes: '))
out_hour = hour + 6
out_minutes = minutes + 51
if out_minutes > 59:
    out_minutes -= 60
    out_hour += 1
if out_hour > 24:
    out_hour -= 24
if out_minutes < 10:
    print('{}:0{}'.format(out_hour, out_minutes))
elif out_hour < 10:
    print('0{}:{}'.format(out_hour, out_minutes))
else:
    print('{}:{}'.format(out_hour, out_minutes))
