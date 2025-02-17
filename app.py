from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('random_forest_model.pkl')  # Load your trained model

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = [
            data['timeSpentOnPage'],
            data['averageMouseSpeed'],
            data['averageFieldTime'],
            data['averageFieldInterval'],
            data['mouseJitterCount'],
            data['mouseTremorCount'],
            data['averageMouseAngleChange'],
            data['backspaceCount'],
            data['repeatedKeyCount'],
            data['xAxisVariance']
        ]
        prediction = model.predict([features])[0]
        return jsonify({'prediction': 'human' if prediction == 1 else 'bot'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
