import sqlite3
import os

DB_PATH = "todo_list.db"

# SQL для создания таблиц
CREATE_USER_TABLE = """
CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_username TEXT NOT NULL UNIQUE,
    user_password TEXT NOT NULL,
    user_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_TASKS_TABLE = """
CREATE TABLE IF NOT EXISTS task (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_title TEXT NOT NULL,
    task_description TEXT,
    task_status TEXT CHECK(task_status IN ('new', 'in progress', 'done')) DEFAULT 'new',
    user_id INTEGER,
    task_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    task_updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE SET NULL
);
"""

CREATE_COMMENTS_TABLE = """
CREATE TABLE IF NOT EXISTS comment (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    comment_comment TEXT NOT NULL,
    comment_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES task (task_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE CASCADE
);
"""


def initialize_database():
    """Создает базу данных и таблицы, если их нет."""
    if os.path.exists(DB_PATH):
        print(f"База данных уже существует: {DB_PATH}")
        return

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    try:
        # Создаем таблицы
        cursor.execute(CREATE_USER_TABLE)
        cursor.execute(CREATE_TASKS_TABLE)
        cursor.execute(CREATE_COMMENTS_TABLE)
        connection.commit()
        print("База данных успешно инициализирована.")
    except sqlite3.Error as e:
        print(f"Ошибка при создании базы данных: {e}")
    finally:
        connection.close()


if __name__ == "__main__":
    initialize_database()
