from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_NAME = "journal.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            );
        """)
init_db()

@app.route('/entries', methods=['GET'])
def get_entries():
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute("SELECT id, content FROM entries").fetchall()
    return jsonify([{'id': row[0], 'content': row[1]} for row in rows])

@app.route('/entries', methods=['POST'])
def add_entry():
    data = request.get_json()
    content = data.get('content')
    if not content:
        return jsonify({'error': 'Content is required'}), 400

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO entries (content) VALUES (?)", (content,))
        conn.commit()
    return jsonify({'message': 'Entry added successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
