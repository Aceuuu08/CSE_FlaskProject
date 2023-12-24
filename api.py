from flask import Flask, make_response, jsonify, request, render_template, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345678"
app.config["MYSQL_DB"] = "cse"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["SECRET_KEY"] = "89f8e8012829949cc95557c64485fbdf"

mysql = MySQL(app)

users = {'username': 'password'}

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

@app.route("/player", methods=["GET"])
def get_player():
    data = data_fetch("""select * from player""")
    return make_response(jsonify(data), 200)


@app.route("/player/<int:id>", methods=["GET"])
def get_player_by_id(id):
    data = data_fetch("""SELECT * FROM player where player_id = {}""".format(id))
    return make_response(jsonify(data), 200)


@app.route("/player", methods=["POST"])
def add_actor():
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    gender = info["gender"]
    address = info["address"]
    other_details = info["other_details"]
    current_game = info["current_game"]
    current_team = info["current_team"]

    cur.execute(
        """
        INSERT INTO player 
        (first_name, last_name, gender, address, other_details, current_game, current_team) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (first_name, last_name, gender, address, other_details, current_game, current_team),
    )
    mysql.connection.commit()
    print("row(s) affected: {}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()

    return make_response(
        jsonify(
            {"message": "player added successfully", "rows_affected": rows_affected}
        ),
        201,
    )


@app.route("/player/<int:id>", methods=["PUT"])
def update_actor(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    gender = info["gender"]
    address = info["address"]
    other_details = info["other_details"]
    current_game = info["current_game"]
    current_team = info["current_team"]

    cur.execute(
        """
        UPDATE player 
        SET first_name = %s, last_name = %s, gender = %s, address = %s, other_details = %s, 
        current_game = %s, current_team = %s 
        WHERE player_id = %s
        """,
        (first_name, last_name, gender, address, other_details, current_game, current_team, id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()

    return make_response(
        jsonify(
            {"message": "player updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )



@app.route("/player/<int:id>", methods=["DELETE"])
def delete_actor(id):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM player WHERE player_id = %s """, (id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()

    return make_response(
        jsonify(
            {"message": "player deleted successfully", "rows_affected": rows_affected}
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)
