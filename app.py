from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html>
<head>
    <title>RCB Fan Portal</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #d4145a 0%, #000000 100%);
            color: white;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 40px;
            border-radius: 10px;
            max-width: 500px;
            margin: 0 auto;
        }
        input[type="text"] {
            padding: 10px;
            width: 80%;
            margin: 10px 0;
            border-radius: 5px;
            border: none;
        }
        input[type="submit"] {
            background: #fdb913;
            color: black;
            padding: 10px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }
        input[type="submit"]:hover {
            background: #d4145a;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏏 Welcome to RCB Fan Portal!</h1>
        <p>Predict the next match outcome and win prizes!</p>
        <form method="POST" action="/predict">
            <label>Enter your match prediction:</label><br>
            <input type="text" name="prediction" placeholder="e.g., RCB will win by 50 runs"><br><br>
            <input type="submit" value="Submit Prediction">
        </form>
    </div>
</body>
</html>'''

@app.route('/predict', methods=['POST'])
def predict():
    prediction = request.form.get('prediction', 'No prediction')
    
    # VULNERABLE CODE - DO NOT USE IN PRODUCTION
    template = f'''<!DOCTYPE html>
<html>
<head>
    <title>Your Prediction</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #d4145a 0%, #000000 100%);
            color: white;
            text-align: center;
            padding: 50px;
        }}
        .container {{
            background: rgba(0, 0, 0, 0.7);
            padding: 40px;
            border-radius: 10px;
            max-width: 500px;
            margin: 0 auto;
        }}
        a {{
            color: #fdb913;
            text-decoration: none;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h2>✅ Thanks for your prediction!</h2>
        <p>You predicted: {prediction}</p>
        <br>
        <a href="/">← Submit another prediction</a>
    </div>
</body>
</html>'''
    
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)