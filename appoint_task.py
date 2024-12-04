import sqlite3

def appoint_task(task_id, user_id):
    con = sqlite3.connect('todo_list.db')
    cur = con.cursor()
    if cur.execute('SELECT * from user WHERE user_id == ?', (user_id,)).fetchall():
        if cur.execute('SELECT * from task WHERE task_id == ?', (task_id,)).fetchall():
            cur.execute('UPDATE task SET user_id = ? WHERE task_id = ?', (user_id, task_id))
            con.commit()
            print('Успешно!')
        else:
            print('Такой задачи не существует!')
    else:
        print('Такого пользователя не существует!')

if __name__ == '__main__':
    task, user = input().split()
    appoint_task(int(task), int(user))
