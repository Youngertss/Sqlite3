import sqlite3
my_db=sqlite3.connect("magaz.db")
cur=my_db.cursor()



a=int(input('Привет. Выбери действие. 1 - добавить товар. 2 - удалить товар. 3 - поиск по всем критериям и его вывод:\n'))
if a==1:
    z=int(input("айди: "))
    x=input("категория: ").lower()
    c=input("производитель: ").lower()
    v=int(input("цена: "))
    b=input("точка реализации: ").lower()
    cur.execute("INSERT INTO magaz4 ('айди', 'категория', 'производитель', 'цена', 'точка_реализации') VALUES(?,?,?,?,?)", (z,x,c,v,b))
    my_db.commit()
    print("Вы добавили товар!")
if a==2:
    q=int(input("Введите айди: "))
    w=input("Введите точку реализации: ").lower()
    cur.execute("DELETE FROM magaz4 WHERE айди == (?) AND точка_реализации == (?)", (q,w))
    my_db.commit()
    print("Товар успешно удален.")
if a==3:
    q=int(input("Выберете критерий(1 - айди, 2 - категория, 3 - произваодитель, 4 - цена, 5 - точка реализации): "))
    if q==1:
        z=int(input("айди: "))
        cur.execute("SELECT * FROM magaz4 WHERE айди == (?)", (z,))
    elif q==2:
        z=input("категория: ").lower()
        cur.execute("SELECT * FROM magaz4 WHERE категория == ?", (z,))
    elif q==3:
        z=input("производитель: ").lower()
        cur.execute("SELECT * FROM magaz4 WHERE производитель == (?)", (z,))
    elif q==4:
        z=int(input("цена: "))
        cur.execute("SELECT * FROM magaz4 WHERE цена == (?)", (z,))
    elif q==5:
        z=input("точка реализации: ").lower()
        cur.execute("SELECT * FROM magaz4 WHERE точка_реализации == (?)", (z,))
    data = cur.fetchall()
    print(data)