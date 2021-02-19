import sqlite3
import os
class DB:
    def __init__(self):
        self.conn=sqlite3.connect("{}/Tbot.db".format(os.environ["HOME"]))
        self.curr=self.conn.cursor()
        self.curr.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables=["chat_ids","password","api_key"]
        results=self.curr.fetchall()
        db_tables=[ res[0] for res in results ]
        for table in tables:
            if table not in db_tables:
                self.curr.execute("CREATE TABLE {}({} text)".format(table,table))
                self.conn.commit()

    def __del__(self):
        self.conn.close()

    def get_chat_ids(self):
        self.curr.execute("select chat_ids from chat_ids;")
        results=self.curr.fetchall()
        chat_ids=[]
        for row in results:
            chat_ids.append(row[0])
        return chat_ids
        
    def put_chat_id(self,chat_id):
        if not str(chat_id) in self.get_chat_ids():
            self.curr.execute("INSERT INTO chat_ids values('{}');".format(chat_id))
            self.conn.commit()

    def del_chat_id(self,chat_id):
        self.curr.execute("DELETE FROM chat_ids where chat_ids='{}';".format(chat_id))
        self.conn.commit()

    def set_pwd(self,pwd):
        self.curr.execute("DELETE FROM password;")
        self.curr.execute("INSERT INTO password values(?);",(pwd,))
        self.conn.commit()
    
    def get_pwd(self):
        self.curr.execute("select password from password;")
        return self.curr.fetchall()[0][0]
    
    def set_api(self,api_key):
        self.curr.execute("DELETE FROM api_key;")
        self.curr.execute("INSERT INTO api_key values(?);",(api_key,))
        self.conn.commit()
    
    def get_api_key(self):
        self.curr.execute("SELECT * from api_key;")
        results=self.curr.fetchall()
        return results[0][0]