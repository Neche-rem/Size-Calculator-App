from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    image_size = float(data.get("image_size"))
    magnification = float(data.get("magnification"))

    if magnification == 0:
        return jsonify({"error": "Magnification cannot be zero"}), 400

    actual_size = image_size / magnification

    return jsonify({
        "actual_size": actual_size
    })

if __name__ == "__main__":
    app.run(debug=True)
