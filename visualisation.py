import matplotlib.pyplot as plt
from main import query1, query2, query3

first_data = query1()
second_data = query2()
third_data = query3()

name_student = first_data['Student']
math_score = first_data['Math Score']

fig, ax = plt.subplots()
ax.bar(name_student, math_score)
ax.set_title('Students, which have reading score more than 80', fontsize=20)
plt.xlabel('Students')
plt.ylabel('Reading score')

fig.set_figwidth(12)
fig.set_figheight(6)
plt.show()


fig1, ax1 = plt.subplots(figsize=(12, 6), dpi=180)

genders = second_data["Gender"]
avg_math = second_data["Average Math Score"]

wedges, texts, autotexts = ax1.pie(avg_math, labels=genders, autopct='%.1f%%',startangle=140)
ax1.set_title('Average Math Score by Gender of Students', fontsize=20)
plt.show()

surname = third_data['Student Surname']
reading_score = third_data['Reading Score']

fig2, ax2 = plt.subplots()

ax2.scatter(surname, reading_score)
ax2.set_title('Students and their reading scores', fontsize=20)
plt.xlabel('Students')
plt.ylabel('Reading score')

fig2.set_figwidth(12)
fig2.set_figheight(6)
plt.show()