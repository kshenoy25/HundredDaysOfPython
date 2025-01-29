students_dict = {
    "students": ["Haley", "Kunal", "Abby"] ,
    "score": [98, 87, 90]
}

import pandas

student_data_frame = pandas.DataFrame(students_dict)
# print(student_data_frame)

# loop through data frame
#for (key, value) in students_dict.items():
    #print(key)

# loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    if row.students == "Haley":
        print(row.score)
    #print(row)