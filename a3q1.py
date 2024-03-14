import psycopg2
from psycopg2 import sql

#Step 1: I have to connect to the database thats on pgadmin
conn = psycopg2.connect(
    dbname='a3q1', user='postgres', password='postgres', host='localhost'
)
cursor = conn.cursor() # create the cursor to be able to interact with the database

#--------defintions-------------------------------------------------------------
#function gets all studnets
def getAllStudents():
    cursor.execute("SELECT * FROM students;" )
    # This line executes an SQL query that selects all records from the students table
    for record in cursor.fetchall():
        print(record)
# This loop gets all the rows from the database and prints them.

#this function adds a student to database
def addStudent(first_name, last_name, email, enrollment_date):
    cursor.execute(
# Executes a command to insert a new studnet into the  table with the provided details
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
        (first_name, last_name, email, enrollment_date)
    )
    conn.commit()
    #commites the change so its set in database
    print("The student was added.")

#updates the student email of choice based on studnet number
def updateStudentEmail(student_id, new_email):
    cursor.execute(

        "UPDATE students SET email = %s WHERE student_id = %s;",
        (new_email, student_id)
        #updates the email of a student record based on the given student_id.
    )
    conn.commit()
    #commites the change so its set in database
    print("email was updated.")

#function to delete a given student
def deleteStudent(student_id):

    cursor.execute(
        "DELETE FROM students WHERE student_id = %s;",
        (student_id,)
)
     # deletes the student record with the specified student_id from the table
    conn.commit()
    #commites the change so its set in database
    print("the student has been deleted.")



#--------------Functions calls--------------------------------------------------

#addStudent('Samer', 'Frangieh', 'samerfrangieh@example.com', '2024-03-14')
#updateStudentEmail(1, 'john.updated@example.com')
deleteStudent(2)
getAllStudents()
#---------------------------------------------------------------------

cursor.close()
conn.close()
