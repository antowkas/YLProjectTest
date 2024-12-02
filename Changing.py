import sqlite3

con = sqlite3.connect("todo_list.db")
cur = con.cursor()

task_id = str(input("Введите id задачи: "))
new_status = str(input("Новой статус: "))

res = cur.execute(f"""UPDATE task
                SET task_status = '{new_status}'
                WHERE task_id = '{task_id}'""")

con.commit()
cur.close()
con.close()