import pymysql.cursors
import pprint

connection = pymysql.connect(host='localhost',
                             user='horiuchi',
                             password='hori',
                             db='rensyu',
                             charset='utf8',
                             # 結果の受け取り方の指定。Dict形式で結果を受け取ることができる
                             cursorclass=pymysql.cursors.DictCursor)
def insert_data(name,age,height,weight):
    with connection.cursor() as cursor:
        sql = "INSERT INTO people (name, age,weight,height) VALUES (%s, %s,%s,%s)"
        cursor.execute(sql, (name,age,height,weight))

    connection.commit()

def select_data():
    with connection.cursor() as cursor:
        sql = "SELECT name,age,weight,height FROM people"
        cursor.execute(sql)

        results = cursor.fetchall()
        for r in results:
            print(r)

def update_data():
    with connection.cursor() as cursor:
        sql = "UPDATE people SET age = 26"
        cursor.execute(sql)

    connection.commit()

def delete_data():
    with connection.cursor() as cursor:
        sql = "DELETE FROM people WHERE name = %s"
        cursor.execute(sql,("tanaka"))

    connection.commit()

def insert_dict_data():
    for people in people_list:
        name = people["name"]
        age = people["age"]
        weight = people["weight"]
        height = people["height"]
        insert_data(name,age,height,weight)

def data_to_list():
    people_information = []
    with connection.cursor() as cursor:
        sql = "SELECT name,age,weight,height FROM people"
        cursor.execute(sql)

        results = cursor.fetchall()
        for r in results:
            people_information.append(r)
    return people_information


people_list =[{"name":"ando","age":"20","weight":"50","height":"150"},
              {"name":"ishikawa","age":"60","weight":"43","height":"160"},
              {"name":"suzuki","age":"74","weight":"77","height":"175"},
              {"name":"toda","age":"32","weight":"55","height":"166"},
              {"name":"nagai","age":"19","weight":"43","height":"158"},
              {"name":"hamada","age":"28","weight":"45","height":"172"},
              {"name":"matsumoto","age":"52","weight":"69","height":"190"},
              {"name":"yamada","age":"47","weight":"54","height":"169"},
              {"name":"yoshida","age":"91","weight":"40","height":"140"},
              {"name":"watanabe","age":"29","weight":"80","height":"181"},
              ]

select_data()
pprint.pprint(data_to_list()[0:4])

