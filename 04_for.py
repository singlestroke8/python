point_list = [75, 80, 91]
total = 0
for point in point_list:
    total = total + point
number_of_subjects = len(point_list)
average = total / number_of_subjects
print("合計点は{}、平均点は{}です".format(total, average))


for number in range(10):
    print(number)


your_point = 76
if your_point >= 80:
    evaluation = 'Excellent'
elif your_point >= 65:
    evaluation = 'Good'
else:
    evaluation = 'Bad'
print("点数の評価は{}です".format(evaluation))