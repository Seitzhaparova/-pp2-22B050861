import psycopg2
import csv

conn = psycopg2.connect(
    host ="localhost",
    database = "suppliers",
    user = "postgres",
    password = "postgre",
)

cursor = conn.cursor() 

init_action = input('''Please 
                \n\ttype 'create' to CREATE contact
                \n\ttype 'read' to GET contact from phonebooks
                \n\ttype 'update' to CHANGE something 
                \n\ttype 'delete' to DELETE contact
                \n\ttype 'insert' to INSERT data from file 
                \n\ttype 'page' to use pagination on table
       ---> : ''')


#cursor.execute(f"create table phonebooks(id serial, name char(30), email char(30), number char(30), company char(30), primary key(id));")

def func(action):
    if action == 'create':
        name = input('type your NAME: ')
        email = input('type your EMAIL: ')
        number = input('type your PHONE NUMBER: ')
        company = input('type your COMPANY: ')
        cursor.execute(f"select count(*) from phonebooks where name = '{name}'")
        result = cursor.fetchone()
        for r in result:
            if r >= 1:
                cursor.execute(f"update phonebooks set email = '{email}' where name = '{name}';")
                cursor.execute(f"update phonebooks set number = '{number}' where name = '{name}';")
                cursor.execute(f"update phonebooks set company = '{company}' where name = '{name}';")
            else:
                cursor.execute(f"insert into phonebooks (name, email, number, company) values ('{name}', '{email}', '{number}', '{company}');")
        
        conn.commit()
        print(f'\nYou have succesfully created contact of {name}\n')
        

    if action == 'read':
        way1= input('Do you want to print all records? If so, print yes, otherwise no:  ')
        if way1 == 'yes':
            cursor.execute(f"select * from phonebooks")
            contacts = cursor.fetchall()
            for row in contacts:
                print(f"\n\tid: {row[0]} | NAME: {row[1]} | EMAIL: {row[2]} | NUMBER: {row[3]} | COMPANY: {row[4]}\n")
        else:
            way = int(input('Do you want to read by name(1), phone(2), email(3), company(4)? Type the corresponding number:  '))
            if way == 1:
                name = input('Who? type NAME:  ') 
                cursor.execute(f"select * from phonebooks where name like '%{name}%';")
                contacts = cursor.fetchall()
                for contact in contacts:
                    print(f"\n\tid: {contact[0]} | NAME: {contact[1]} | EMAIL: {contact[2]} | NUMBER: {contact[3]} | COMPANY: {contact[4]}\n")
            elif way == 2:
                number = input('Who? type NUMBER:  ')
                cursor.execute(f"select * from phonebooks where number = '{number}'")
                contacts = cursor.fetchall()
                for row in contacts:
                    print(f"\n\tid: {row[0]} | NAME: {row[1]} | EMAIL: {row[2]} | NUMBER: {row[3]} | COMPANY: {row[4]}\n")
            elif way == 3:
                email= input('Who? type EMAIL:  ')
                cursor.execute(f"select * from phonebooks where email = '{email}'")
                contacts = cursor.fetchall()
                for row in contacts:
                    print(f"\n\tid: {row[0]} | NAME: {row[1]} | EMAIL: {row[2]} | NUMBER: {row[3]} | COMPANY: {row[4]}\n")
        conn.commit() 
        

    if action == 'update':
        name = input('Who?, type NAME:  ')
        cursor.execute(f"select count(*) from phonebooks where name = '{name}'")
        result = cursor.fetchone()
        for r in result:
            if r>1:
                id = int(input('What ID:  '))
                a = input(f"What do u wanna CHANGE in {name}'s of {id} contact? Type 'email', 'number', 'company'! :   ")
                if a == 'email':
                    email = input('type email: ')
                    cursor.execute(f"update phonebooks set email = '{email}' where name = '{name}' and id='{id}';")
                    conn.commit()
                if a == 'number':
                    number = input('type number: ')
                    cursor.execute(f"update phonebooks set number = '{number}' where name = '{name}' and id='{id}';")
                    conn.commit()
                if a == 'company':
                    company = input('type company: ')
                    cursor.execute(f"update phonebooks set company = '{company}' where name = '{name}' and id='{id}';")
                    conn.commit()
            else:
                a = input(f"What do u wanna CHANGE in {name}'s contact? Type 'email', 'number', 'company'! :   ")
                if a == 'email':
                    email = input('type email: ')
                    cursor.execute(f"update phonebooks set email = '{email}' where name = '{name}';")
                    conn.commit()
                if a == 'number':
                    number = input('type number: ')
                    cursor.execute(f"update phonebooks set number = '{number}' where name = '{name}';")
                    conn.commit()
                if a == 'company':
                    company = input('type company: ')
                    cursor.execute(f"update phonebooks set company = '{company}' where name = '{name}';")
                    conn.commit()
        print('\nSuccessfully updated!\n')

    if action == 'delete':
        way = int(input('Do you want to delete by name(1) or phone(2)? Type the corresponding number:  '))
        if way == 1:
            name = input('Who?, type NAME:  ')
            cursor.execute(f"select count(*) from phonebooks where name = '{name}'")
            result = cursor.fetchone()
            for r in result:
                if r>1:
                    id = int(input('What ID:  '))
                    cursor.execute(f"delete from phonebooks where name = '{name}' AND id= '{id}'")
                else:
                    cursor.execute(f"delete from phonebooks where name = '{name}'")
        else:
            number = input('Who?, type NUMBER:  ')
            cursor.execute(f"select count(*) from phonebooks where number = '{number}'")
            result = cursor.fetchone()
            for r in result:
                if r>1:
                    id = int(input('What ID:  '))
                    cursor.execute(f"delete from phonebooks where number = '{number}' AND id= '{id}'")
                else:
                    cursor.execute(f"delete from phonebooks where number = '{number}'")
        print('\nSuccessfully deleted!\n')
    if action == 'insert':
        f = open(r"C:\Users\User\Desktop\pp2\new_contacts.csv", 'r')
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        for row in reader:
            cursor.execute(f"insert into phonebooks(name, email, number, company) values (%s, %s, %s, %s)", row)
        conn.commit()
        print('\nSuccessfully inserted!\n')

    if action == 'page':
        limit = int(input('type limit: '))
        offset = int(input('type offset: '))
        cursor.execute(f"select * from phonebooks order by id limit {limit} offset {offset};")
        conn.commit()
        result = cursor.fetchall()
        for i in result:
            print(i)

    act = input('''What else do you want to do? 
                    If NOTHING, push ENTER button.
                    If YES, please type 'create', 'read', 'update', 'delete' , 'insert' , 'page':  ''')
    if len(act) <= 3:
        print('\nOk, thank you!\n')
        cursor.close()
        conn.close() 
        return 
    else:
        return func(act)


func(init_action)
