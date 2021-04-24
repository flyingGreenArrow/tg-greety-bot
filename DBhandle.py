# each single request open single connection 
import psycopg2
import config
import os


DATABASE_URL = os.environ['DATABASE_URL']


class DBhandle:
    
    def __init__(self):
        self.connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        self.cursor = self.connection.cursor()
        
    def setup(self):
        with self.connection:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS 'usersinfo' 
                                    ('id' int(11) NOT NULL AUTO_INCREMENT,
                                    'first_name' varchar(255) utf8_bin NOT NULL,  
                                    'chat_id' REAL NOT NULL, 
                                    'user_id' TEXT utf8_bin NULL, 
                                    'message_text' TEXT utf8_bin NOT NULL),
                                    PRIMARY KEY ('id')''')
                                # ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin 
                                    # AUTO_INCREMENT=1
            self.close()
    
    def simpleRecording(self, data):
        with self.connection:
            query = "INSERT INTO 'usersinfo' ('first_name', 'chat_id', 'message_text') VALUES (%s, %s, %s)"
            self.cursor.execute(query, data)
            self.connection.commit()
            self.close()
    
    def recording(self, data):
        with self.connection:
            self.cursor.executemany("INSERT INTO 'usersinfo' VALUES (?, ?, ?, ?)", data)
            self.connection.commit()
            self.close()
        
    def get_user_info(self):
        with self.connection:
            x = self.cursor.execute("SELECT * FROM 'usersinfo'").fetchall()
            self.close()
        return x

        
    def clear_db(self):
        with self.connection:
            return self.cursor.execute("DELETE * FROM 'usersinfo'")
    
    def close(self):
        self.connection.close()