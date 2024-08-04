# 24 hour clock

# Current time set from the user
current_time = int(input("Enter the current time (in hours, 0-23):"))

# Current time to wait for setting the alarm
wait_time = int(input("Enter the number of wait time for the alarm"))

# Calculation to sound the alarm
alarm_time = (current_time + wait_time) % 24

# Show alarm clock
print(f"The alarm will sound off at {alarm_time}:00 (24-hour clock).")
