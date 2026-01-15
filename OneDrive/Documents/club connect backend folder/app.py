from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/events")
def events():
    data = [
        {"name": "Cricket Tournament", "date": "20 Feb", "place": "Sports Ground"},
        {"name": "Freshers Party", "date": "25 Feb", "place": "Auditorium"},
        {"name": "Cultural Fest", "date": "5 Mar", "place": "Open Stage"},
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

