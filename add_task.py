import sqlite3


def adding_task():
    user_id = input(
        'Введите id пользователя, для которого будет предназначаться задача. Если пользователь еще не определен, нажмите Enter.')
    task_title = input('Введите название задачи.')
    task_desc = input('Введите описание задачи.')

    con = sqlite3.connect('todo_list.db')
    cur = con.cursor()
    if user_id:
        cur.execute('''INSERT INTO task(task_title, task_description, user_id) VALUES(?, ?, ?)''',
                    (task_title, task_desc, user_id))
    else:
        cur.execute('''INSERT INTO task(task_title, task_description) VALUES(?, ?)''',
                    (task_title, task_desc))
    print('Задача успешно добавлена!')


adding_task()
