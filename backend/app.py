from flask import Flask, request, jsonify
import os
from flask_cors import CORS
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


app = Flask(__name__)
CORS(app)

print("hello from back")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        ans = data.get('answer')
        print(ans)
        print(len(ans))

        ans = ['11', '18', '5', '9', '16', '6', '16', '7', '2', '2', '4', '4', '5', '17', '2', '7', '17', '1', '2', '3', '19', '8', '3', '19', '2', '11', '16', '11', '3', '5', '1', '3', '18', '15', '6', '5', '18', '8', '1910', '18', '7', '16', '8', '18', '13', '11', '12', '11', '6', '3', '10', '16', '10', '9', '11', '0', '19', '13', '4', '2', '5', '13', '19', '13', '2', '1', '11', '10', '6', '18', '14', '5', '15', '3', '13', '19', '9', '16', '11', '10', '1', '16', '3', '8', '9', '15', '17', '18', '9', '16', '4', '13', '19', '11', '16', '16', '19', '17', '15', '1', '14', '17', '10', '7', '13', '11', '10', '2', '15', '2']
        ans = [0, 9, 13, 10, 10, 2, 4, 7, 6, 14, 15, 12, 8, 14, 16, 4, 9, 15, 8, 5, 11, 15, 3, 18, 18, 13, 18, 17, 10, 5, 19, 4, 3, 13, 10, 7, 16, 17, 3, 8, 3, 6, 12, 2, 12, 18, 9, 7, 1, 10, 7, 7, 7, 13, 3, 15, 2, 17, 12, 4, 19, 5, 2, 5, 11, 19, 1, 6, 5, 9, 2, 3, 17, 14, 1, 12, 7, 4, 0, 18, 2, 14, 1, 2, 10, 19, 18, 0, 3, 9, 0, 15, 15, 14, 3, 4, 2, 9, 11, 9, 6, 9, 19, 13, 15, 7, 10, 7, 2, 5]
        ans = [5, 17, 8, 4, 13, 19, 10, 8, 2, 7, 19, 8, 11, 17, 10, 17, 3, 4, 5, 19, 18, 6, 10, 11, 4, 18, 1, 10, 13, 17, 3, 15, 6, 12, 0, 19, 2, 7, 14, 4, 2, 8, 13, 13, 4, 1, 15, 3, 12, 12, 10, 10, 9, 19, 7, 9, 6, 19, 2, 17, 11, 3, 6, 17, 8, 1, 17, 9, 13, 19, 9, 14, 2, 10, 5, 1, 18, 14, 2, 9, 8, 5, 0, 1, 11, 13, 18, 13, 18, 14, 13, 10, 19, 15, 18, 13, 16, 17, 2, 0, 16, 18, 18, 11, 1, 0, 4, 18, 13, 10]
        result = predictProcess(ans)
        return jsonify({'message1': str(result[0][0]),
                        'message2': str(result[0][1]),
                        'message3': str(result[0][2]),
                        'message4': str(result[0][3]),
                        'message5': str(result[0][4]),
                        })
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': str(e), 'message':'An error occurred on the server.'}), 500 #return an error code and message.

def predictProcess(ans):
    print(ans)
    for i in range(len(ans)):
        ans[i] = int(ans[i])
    loaded_rf = joblib.load("my_random_forest.joblib")
    scaler = StandardScaler()
    Arr = scaler.fit_transform([ans])
    predicted_new = loaded_rf.predict(Arr)
    print(predicted_new)
    return predicted_new

# ['11', '18', '5', '9', '16', '6', '16', '7', '2', '2', '4', '4', '5', '17', '2', '7', '17', '1', '2', '3', '19', '8', '3', '19', '2', '11', '16', '11', '3', '5', '1', '3', '18', '15', '6', '5', '18', '8', '1910', '18', '7', '16', '8', '18', '13', '11', '12', '11', '6', '3', '10', '16', '10', '9', '11', '0', '19', '13', '4', '2', '5', '13', '19', '13', '2', '1', '11', '10', '6', '18', '14', '5', '15', '3', '13', '19', '9', '16', '11', '10', '1', '16', '3', '8', '9', '15', '17', '18', '9', '16', '4', '13', '19', '11', '16', '16', '19', '17', '15', '1', '14', '17', '10', '7', '13', '11', '10', '2', '15']

if __name__ == '__main__':
    app.run(debug=True)