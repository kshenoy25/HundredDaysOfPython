student_scores =  [67,89,34,56,78,97,78,95,90,85,89,72,68,77,99,93,83,]
total_exam_score = sum(student_scores)
#print(total_exam_score)

"""
sum = 0
for score in student_scores:
    sum += score

print(sum)

"""
#print(max(student_scores))
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)