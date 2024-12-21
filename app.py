from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__, static_folder="frontend/static", template_folder="frontend/templates")

def query_database(query):
    try:
        connection = sqlite3.connect("chatbot.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name, price FROM products WHERE name LIKE ?", (f"%{query}%",))
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if connection:
            connection.close()

@app.route("/")
def index():
    template_path = os.path.join(app.template_folder, "index.html")
    print(f"Looking for template: {template_path}")
    if not os.path.exists(template_path):
        print("Error: Template not found.")
        return "Template not found", 404
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chatbot():
    user_query = request.json.get("query", "").strip()
    if not user_query:
        return jsonify({"response": "Please provide a valid query."})

    results = query_database(user_query)
    if results:
        response = "\n".join([f"{name} - ${price}" for name, price in results])
    else:
        response = "Sorry, no products found."

    return jsonify({"response": response})

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error occurred.", "details": str(e)}), 500

if __name__ == "__main__":
    db_path = os.path.abspath("chatbot.db")
    print(f"Using database at: {db_path}")
    app.run(debug=True)
