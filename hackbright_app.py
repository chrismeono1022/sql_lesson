import sqlite3

CONN = sqlite3.connect("my_database.db")
DB = CONN.cursor()

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values(?,?,?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s"%(first_name, last_name)

def get_project(title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title,)) 
    row = DB.fetchone()
    print """\
Project: %s
Description: %s
Max grade: %s"""%(row[0], row[1], row[2])

def make_new_project(title, description, max_grade):
    query = """INSERT into Projects values(?,?,?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project: %s %s %s" %(title, description, max_grade) 

def student_grade(project_title):
    query = """SELECT student_github, project_title, grade FROM Grades WHERE project_title = ?"""
    DB.execute(query, (project_title,))
    row = DB.fetchone()
    print """\
Student Github: %s
Project: %s
Grade: %s"""%(row[0], row[1], row[2])

def  grade_student(student_github, project_title, grade):
    query = """INSERT into Grades values(?,?,?)"""
    DB.execute(query, (student_github, project_title, grade))
    CONN.commit()
    print "Successfully graded student: %s %s %s" %(student_github, project_title, grade)

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("my_database.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "projects":
            new_args = [" ".join(args)]
            get_project(*new_args)
        elif command == "new_project":
            new_args = " ".join(args).split(",")
            make_new_project(*new_args)
        elif command == "grade":
            new_args = [" ".join(args)]
            student_grade(*new_args)
        elif command == "grade_student":
            new_args = " ".join(args).split(",")
            grade_student(*new_args)

    CONN.close()

if __name__ == "__main__":
    main()
