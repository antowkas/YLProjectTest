import sqlite3

# Пожалуйста сделайте хоть что то, я не могу работать с ничем.
# Я приверженец метода работы с ошибками по мере их поступления
# Как я должен проверять работоспособность программы если нет ничего?
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