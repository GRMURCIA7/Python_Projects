# dictionary of course number (Key) and room number (Value)

room_number = {
    "CSC101": "Room 3004",
    "CSC102": "Room 4501",
    "CSC103": "Room 6755",
    "NET110": "Room 1244",
    "COM241": "Room 1411"
}

# dictionary of course number (Key) and instructor name (Value)
instructor_name = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# dictionary of course number(Key) and meeting time(Value)
meeting_time = {
    "CSC101": "8:00 am",
    "CSC102": "9:00 am",
    "CSC103": "10:00 am",
    "NET110": "11:00 am",
    "COM241": "1:00 pm"
}

# prompt user for course number
course_number = input("Enter the course number: ")

# valiadate the course number exisit in the dictionary
if course_number in room_number and course_number in instructor_name and course_number in meeting_time:
    print(f"Course Number: {course_number}")
    print(f"Room Number: {room_number[course_number]}")
    print(f"Instructor: {instructor_name[course_number]}")
    print(f"Meeting Time: {meeting_time[course_number]}")
else:
    print("Course number not found.")
    
# Code by Garen Murcia Mod 7



