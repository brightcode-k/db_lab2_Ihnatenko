import psycopg2

username = 'Ihnatenko_Nikolai'
password = 'Kolya'
database = 'Nikolai_DB'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT coalesce(s.name, '') || ' ' || coalesce(s.surname, '') AS student, sc.math_score 
FROM students s
INNER JOIN scoring sc
USING(stud_id)
WHERE sc.reading_score > 80
'''

query_2 = '''
SELECT ge.gender, ROUND(AVG(sc.math_score), 2) AS average_math_score
FROM scoring sc
INNER JOIN gender ge
USING(stud_id)
GROUP BY ge.gender
'''

query_3 = '''
SELECT s.surname, sc.reading_score
FROM students s
INNER JOIN scoring sc
USING(stud_id)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cur = conn.cursor()

def query_result(query_n):
    query = query_n
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def query1():
    result = query_result(query_1)
    data = {
        'Student': [i[0] for i in result],
        'Math Score': [i[1] for i in result],
    }
    return data


def query2():
    result = query_result(query_2)
    data = {
        'Gender': [i[0] for i in result],
        'Average Math Score': [i[1] for i in result],
    }
    return data


def query3():
    result = query_result(query_3)
    data = {
        'Student Surname': [i[0] for i in result],
        'Reading Score': [i[1] for i in result],
    }
    return data


def print_result(data):
    keys = list(data.keys())
    print(f"{keys[0]} {keys[1]}")
    for i in range(len(data[keys[0]])):
        print(f"{data[keys[0]][i]} {data[keys[1]][i]}")
    print('\n')


print("First query:\n")
print_result(query1())
print("Second query:\n")
print_result(query2())
print("Third query:\n")
print_result(query3())