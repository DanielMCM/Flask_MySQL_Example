import mysql.connector

def create_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="phpmyadmin",
            password="P@ssword"
        )

        mycursor = mydb.cursor()
        
        mycursor.execute("SHOW DATABASES")

        if ('exercise',) in mycursor:
          pass
        else:
            mycursor.execute("CREATE DATABASE exercise")

        mycursor.execute("USE exercise")
        mycursor.execute("SHOW TABLES")

        if ('contact',) in mycursor:
            pass
        else:
            mycursor.execute("CREATE TABLE contact (contactid INT NOT NULL AUTO_INCREMENT, \
                                                    firstname VARCHAR(255) NOT NULL, \
                                                    lastname VARCHAR(255)  NOT NULL,  \
                                                    address VARCHAR(255),   \
                                                    email VARCHAR(255) NOT NULL,     \
                                                    phone VARCHAR(255),     \
                                                    PRIMARY KEY (contactid))")
        mydb.close()
    except:
        pass

def create_stored_procedure():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="phpmyadmin",
            password="P@ssword"
        )

        mycursor = mydb.cursor()
        mycursor.execute("USE exercise")

        mycursor.execute("CREATE DEFINER=`phpmyadmin`@`localhost` PROCEDURE `sp_createContact` (\
                                        IN p_firstname VARCHAR(255),\
                                        IN p_lastname VARCHAR(255),\
                                        IN p_address VARCHAR(255),\
                                        IN p_email VARCHAR(255),\
                                        IN p_phone VARCHAR(255) \
                                    )\
                                    BEGIN \
                                        \
                                            insert into contact\
                                            ( \
                                                firstname, \
                                                lastname, \
                                                address,\
                                                email,\
                                                phone\
                                            )\
                                            values \
                                            (\
                                                p_firstname, \
                                                p_lastname, \
                                                p_address,\
                                                p_email,\
                                                p_phone\
                                            );\
                    \
                                    END;")

    except:
        pass

if __name__ == "__main__":

    create_database()
    create_stored_procedure()