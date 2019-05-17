import psycopg2
import coonection
import mysql.connector


class hello():
  def data(self):

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="school"
)
    mycursor = mydb.cursor()

    queryjoin = "SELECT student.stu_id, student.stu_name, student.age,teachers.t_id,teachers.t_name FROM student Inner JOIN teachers ON student.stu_id=teachers.stu_id;"

    mycursor.execute(queryjoin)
    myresult = mycursor.fetchall()
    print myresult
    self.postgres(myresult)

  def postgres(self,myresult):

    conn = psycopg2.connect(coonection.connection)
    cursor = conn.cursor()
    for i in myresult:
        id = i[0]
        name = i[1]
        age = i[2]
        tid = i[3]
        tname = i[4]
        print tname
        query = "INSERT INTO college(stu_id, stu_name, age, t_id ,t_name) VALUES({0},'{1}',{2} ,{3},'{4}')".format((id), str(name),(age),(tid),str(tname))
        print 'Query->',query
        cursor.execute(query)
        # conn.commit()


objs = hello()
objs.data()