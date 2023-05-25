from db_connection import connection


class Executor:
    def __init__(self):
        self.cursor = connection.cursor()

    def task1(self):
        query1 = "BEGIN TRANSACTION " \
                 "SELECT * FROM users "
        query2 = "ALTER TABLE login_history " \
                 "DROP CONSTRAINT [history_fk] " \
                 "ALTER TABLE login_history " \
                 "WITH CHECK ADD CONSTRAINT [history_fk] " \
                 "FOREIGN KEY (user_id) REFERENCES users(user_id) " \
                 "ON DELETE CASCADE " \
                 "DELETE FROM users " \
                 "WHERE user_id IN " \
                 "(SELECT U.user_id FROM users U " \
                 " JOIN login_history LH " \
                 "ON U.user_id=LH.user_id " \
                 "WHERE DATEDIFF(year,LH.login_date,GETDATE())>1) "
        query3 = "SELECT * FROM users " \
                 "ROLLBACK"
        self.cursor.execute(query1)
        rows1 = self.cursor.fetchall()
        self.cursor.execute(query2)
        self.cursor.execute(query3)
        rows2 = self.cursor.fetchall()
        print("BEFORE DELETION:")
        for row in rows1:
            print(row)
        print("AFTER DELETION:")
        for row in rows2:
            print(row)

    def task2(self):
        query1 = "BEGIN TRANSACTION " \
                 "SELECT * FROM users"
        self.cursor.execute(query1)
        rows1 = self.cursor.fetchall()
        print("BEFORE UPDATE:")
        for row in rows1:
            print(row)
        query2 = "UPDATE users " \
                 "SET total_balance=1500, " \
                 "amount_of_wallets=10, " \
                 "initial_avg_balance=total_balance/amount_of_wallets " \
                 "SELECT * FROM users " \
                 "ROLLBACK"
        self.cursor.execute(query2)
        rows2 = self.cursor.fetchall()
        print("AFTER UPDATE:")
        for row in rows2:
            print(row)

    def task3(self):
        query1 = "BEGIN TRANSACTION " \
                 "SELECT * FROM users"
        self.cursor.execute(query1)
        rows1 = self.cursor.fetchall()
        print("BEFORE UPDATE:")
        for row in rows1:
            print(row)
        query2 = "UPDATE users " \
                 "SET total_balance=total_balance+1000 " \
                 "SELECT * FROM users "
        self.cursor.execute(query2)
        rows2 = self.cursor.fetchall()
        print("AFTER UPDATE:")
        for row in rows2:
            print(row)
        query3 = "INSERT INTO users(email,birthday_date,city_id,amount_of_wallets,total_balance,initial_avg_balance) " \
                 "VALUES ('newuser',GETDATE(),5,5,2000,0) " \
                 "UPDATE users " \
                 "SET initial_avg_balance=total_balance/amount_of_wallets " \
                 "WHERE email='newuser' " \
                 "SELECT * FROM users " \
                 "ROLLBACK"
        self.cursor.execute(query3)
        rows3 = self.cursor.fetchall()
        print("AFTER INSERTION:")
        for row in rows3:
            print(row)
