from bs4 import BeautifulSoup
import urllib2, json
import _mysql,sys
import MySQLdb


class api_read():
    def url_read(self):
        detail = []
        url = 'https://reqres.in/api/users?page=1'
        req = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
        con = urllib2.urlopen(req)
        con_read = con.read()
        print 'coneee:dsawdwfd', con_read
        data = json.loads(con_read)
        uu = data['data']
        print 'uu:', uu


        for i in uu:
            id = i['id']
            first_name = str(i['first_name'])
            print 'first_name:', first_name
            last_name = str(i['last_name'])
            print 'last_name:', last_name
            avatar = str(i['avatar'])
            s_dict = {'id': id, 'first_name': first_name, 'last_name': last_name, 'avatar': avatar}
            # s_dict = {'id': id, 'first_name': first_name, 'last_name': last_name}
            if s_dict is not detail:
                detail.append(s_dict)

            self.Read_data(detail)

    def Read_data(self,detail):
        try:
            print 'function call'
            connection = MySQLdb.connect(
                host="localhost",
                user="root",
                passwd="",
                db="hh"
)
            print 'connection:',connection
            # mycursor = connection.cursor()
            # print 'mycursor:',mycursor
            # # for a in detail:
            # #     print 'detail:',detail
            # #     print a
            # #     mycursor.execute(a)
            # # mycursor.execute("SELECT *  FROM api_data_tb")
            # # mycursor.execute(" INSERT INTO api_data_tb VALUES ('%s','%s','%s','%s') ", (first_name,last_name,avatar))
            # # mycursor.execute(" INSERT INTO api_data_tb VALUES  (id,first_name,last_name,avatar) ",)(id,first_name,last_name,avatar)
            # query = "INSERT INTO api_data_tb(id, first_name, last_name, avatar) VALUES ({0},'{1}','{2}','{3}')".format((id), str(first_name),str(last_name),str(avatar))
            # # row = mycursor.fetchall(query)
            # mycursor.execute(query)
            for s in detail:
                print detail
                id = s['id']
                print 'id:fgtfgf', id
                first_name = str(s['first_name'])
                print 'first_name:', first_name
                last_name = str(s['last_name'])
                print 'last_name:', last_name
                avatar = str(s['avatar'])
                print 'avatar:', avatar
            mycursor = connection.cursor()
            print mycursor
            # mycursor.execute("UPDATE urls SET state=%d,content='%s' WHERE url='%s'" (connection.escape_string('link')))

            sql = "INSERT INTO my(id, first_name, last_name, avatar) VALUES({0},'{1}','{2}' ,'{3}')".format((id), str(first_name),(last_name),str(avatar))
            # sql = "select * from ii"

            print 'sql:',sql
            print '---'*100

            # sql = "INSERT INTO api_data_tb (id,first_name,last_name) VALUES (%s, %s)"

            # val = (id,first_name,last_name,avatar)
            # val = ("1","George","Bluth","https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg")
            # val = (id,first_name,last_name)
            # print val
            # print 'val:',val
            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)

            connection.commit()

                # query = "INSERT INTO api_data_tb(id, first_name, last_name, avatar) VALUES({id},'{first_name}',{last_name} ,{avatar})".format(
            #     (id), str(first_name), (last_name), (avatar))
            # print 'query:',query
                # sql_insert_date_query = INSERT INTO api_data_tb('id', 'first_name', 'last_name', 'avatar') VALUES (%s,%s,%s,%s)

                # insertvalues = ('id', 'first_name', 'last_name', 'avatar')
                # a= INSERT INTO api_data_tb ('id', 'first_name', 'last_name', 'avatar')
                # VALUES (0, 'William', 'Shakespeare', 'm', '1961-10-25');

            # mycursor.execute(query)
                # # connection.commit()
                # print (mycursor.rowcount)
                # print(mycursor.rowcount, "was inserted.")
        except:
            # print 'jbjbj'
            print sys.exc_info()
            print '--ppp'*100



if __name__ == '__main__':
    link = 'https://reqres.in/api/users?page=1'
    oA = api_read()
    oA.url_read()