import pprint
import sys

import psycopg2


class StudentDAO:

    def __init__(self, dbname: str, user: str, pw: str, host: str = 'localhost'):
        self.dbname: str = dbname
        self.user: str = user
        self.pw: str = pw
        self.host: str = host
        self.conn = self.__get_connection()
        self.cursor = self.__get_cursor()

    def __get_connection(self):
        try:
            conn = psycopg2.connect(
                host=self.host,
                database=self.dbname,
                user=self.user,
                password=self.pw
            )
            return conn
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
            exit()

    def __get_cursor(self):
        return self.conn.cursor()

    def getAllStudents(self) -> list[tuple]:
        self.cursor.execute('SELECT * FROM students;')
        res = self.cursor.fetchall()
        pprint.pprint(res)
        return res

    def addStudent(self, first_name: str, last_name: str, email: str, enrollment_date: str) -> None:
        try:
            query = f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');"
            self.cursor.execute(query)
            self.conn.commit()
            print("Student record added.")
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
            return

    def updateStudentEmail(self, id: str, new_email: str) -> None:
        try:
            query = f"UPDATE students SET email = '{new_email}' WHERE student_id = {id};"
            self.cursor.execute(query)
            self.conn.commit()
            print(f"Student with id {id}'s email has been updated.")
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
            return

    def deleteStudent(self, id: str) -> None:
        try:
            query = f"DELETE FROM students WHERE student_id = {id};"
            self.cursor.execute(query)
            self.conn.commit()
            print(f"Student with id {id} has been deleted.")
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
            return


def main():
    # in order of dbname, user, pw
    args = sys.argv[1:]
    if len(args) < 3:
        print('Missing db connection arguments.')
        print('Make sure to provide db name, user and password as command line arguments when running script.')
        return

    db = StudentDAO(*args)

    while True:
        print('Commands:')
        print('1. getAllStudents')
        print('2. addStudent')
        print('3. updateStudentEmail')
        print('4. deleteStudent')
        print('-1. Exit')
        ans = int(input('Enter command number:'))
        match ans:
            case -1:
                print('Exiting....')
                exit()
            case 1:
                print('All Students:')
                db.getAllStudents()
            case 2:
                print('Enter Student Details:')
                fname = input('First Name:')
                lname = input('Last Name:')
                email = input('Email:')
                enrollment_date = input('Enrollment Date (YYYY-MM-DD):')
                db.addStudent(fname, lname, email, enrollment_date)
            case 3:
                print('Enter Student Details:')
                id = input('ID:')
                new_email = input('New Email:')
                db.updateStudentEmail(id, new_email)
            case 4:
                print('Enter Student Details:')
                id = input('ID:')
                db.deleteStudent(id)
            case _:
                print('Invalid entry. Try again.')

if __name__ == "__main__":
    main()
