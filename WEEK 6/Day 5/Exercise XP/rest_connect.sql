import psycopg2
import sys

HOSTNAME = '127.0.0.1'
USERNAME = 'postgres'
PASSWORD = 'postgre'
DATABASE = 'theMenu'

def exec(query):
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError: # when query other than SELECT, nothing to fetch.
        results = None
    connection.close()
    return results

class MenuItem():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def save(self):
        for id, name, price in MenuItem.all():
            if self.name == name:
                print(f"Item {name} is already in the menu.")
                return None
        query = f"INSERT INTO menuitem (name, price) VALUES ('{self.name}', {self.price});"
        return exec(query)

    def delete(self):
        for id, name, price in MenuItem.all():
            if self.name == name:
                query = f"DELETE FROM menuitem WHERE name = '{self.name}';"
                return exec(query)
        print(f"Item {name} is not yet in the menu.")
        return None

    @staticmethod
    def update(name, price):
        for id, na, pr in MenuItem.all():
            if na == name:
                query = f"UPDATE menuitem SET price  = {price} WHERE name = '{name}';"
                return exec(query)
        print(f"Item {name} is not yet in the menu.")
        return None

    @staticmethod
    def all():
        query = f"SELECT * FROM menuitem"
        return exec(query)

    @staticmethod
    def get_by_name(str):
        query = f"SELECT * FROM menuitem WHERE name = '{str}'"
        return exec(query)

def main():
    item = MenuItem('Imperial Burger', 35)
    item.save()
    print("After adding Imperial Burger:\n", MenuItem.all())
    item.delete()
    print("After deleting Imperial Burger:\n", MenuItem.all())
    item.update('Veggie Burger', 37)
    print("After updating Veggy Burger:\n", MenuItem.all())
    print(MenuItem.get_by_name('Beef Stew'))
    print(MenuItem.get_by_name('Ratatouille'))

if __name__ == "__main__": # not executed when file imported as a module in other files.
    main()