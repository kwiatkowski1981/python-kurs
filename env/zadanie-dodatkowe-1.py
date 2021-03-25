import math
# przekonwertuj czas na standardowy zapis

times = {
"wake_up":  "23400",
"lunch_time": "43200",
"time_to_sleep": "81000",
}

for time in times.items():
    # print(f"{time[0]} = {time[1]}")

    seconds = 1
    minutes = seconds * 60
    hours = minutes * 60

    converted_time_hours = (math.floor(int(time[1]) / hours))
    if converted_time_hours < 10:
        converted_time_hours = str(converted_time_hours).zfill(2)

    converted_time_minutes = (math.floor((int(time[1]) / minutes) % 60))
    if converted_time_minutes < 10:
        converted_time_minutes = str(converted_time_minutes).zfill(2)

    converted_time_seconds = (math.floor(int(time[1]) % 60))
    if converted_time_seconds < 10:
        converted_time_seconds = str(converted_time_seconds).zfill(2)

    print(f"{time[0]}: {converted_time_hours}:{converted_time_minutes}:{converted_time_seconds}")


