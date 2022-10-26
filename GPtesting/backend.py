import mysql.connector
from ProjectTestingRun.config import USER, HOST, PASSWORD
# from ProjectTestingRun.frontend import userZone

class ZoneNotFoundError(Exception):
    pass

userZone = 2
def connect_to_db():
    connection = mysql.connector.connect(
        host = 'HOST',
        user = 'USER',
        password = 'PASSWORD',
        port = '3306',
        database = 'regulationtoolbox')
    return connection

def get_activity_from_db(userZone):
    connection = None
    result = []
    try:
        db_connection = connect_to_db()
        cur = db_connection.cursor()
        query = "SELECT r.activityName FROM activity_type AS a JOIN regulation_toolbox AS r ON a.act_type_ID=r.activityID WHERE r.activityID = {};".format(userZone)
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    except Exception:
        raise ZoneNotFoundError
    finally:
        if db_connection:
            db_connection.close()

