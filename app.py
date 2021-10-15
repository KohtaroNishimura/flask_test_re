from flask import *
import sqlite3
app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/intro")
def intro():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("select * from name")
    user_info = c.fetchall()
    c.close

    print(user_info)






    return render_template("intro.html" , userlist = user_info)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)