from .entities.User import User



class ModelUser:
    def login(db,user):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT id, username, password, fullname FROM user 
            WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2],user.password),row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
