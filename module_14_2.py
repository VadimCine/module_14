import sqlite3


connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER, 
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#добавляем содержимое таблицы
#for i in range(1, 11):
#    cursor.execute("INSERT INTO USERS (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{10*i}", "1000"))

#обновляем balance у каждой второй записи
#for i in range(1,11):
#    if i % 2 ==1:
#        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

#удаляем каждую третью запись
#for i in range(1,11,3):
#    cursor.execute("DELETE FROM Users WHERE id = ?", [i])

#делаем выборку всех записей
#cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", [60])
#users = cursor.fetchall()
#for user in users:
#    print(user)

#удаляем запись с id = 6
cursor.execute("DELETE FROM Users WHERE id = ?", [6])

#подсчитываем общее количество записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(total_users)

#Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
total_balances = cursor.fetchone()[0]
print(total_balances) #сумма всех балансов
print(total_balances/total_users) #почему в задании так нужно считать?


connection.commit()
connection.close()