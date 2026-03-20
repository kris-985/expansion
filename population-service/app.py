from flask import Flask, request, jsonify
from services import get_population, predict_population

app = Flask(__name__)

# 1. Past population
@app.route("/population/past")
def past_population():
    country = request.args.get("country")
    year = request.args.get("year")

    if not country or not year:
        return jsonify({"error": "country and year are required"}), 400

    try:
        result = get_population(country, int(year))
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 2. Future prediction
@app.route("/population/future")
def future_population():
    country = request.args.get("country")
    year = request.args.get("year")

    if not country or not year:
        return jsonify({"error": "country and year are required"}), 400

    try:
        result = predict_population(country, int(year))
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)