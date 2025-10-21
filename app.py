from flask import Flask, request, render_template_string, make_response
import base64
import re

app = Flask(__name__)

# Real flag (hidden in code)
REAL_FLAG = "Fl4g-X{c00k13_hunt3r_pbks_ch4mp10n_2025}"
# Fake flag for flag.txt
FAKE_FLAG = "PBKS{n1c3_try_but_keep_l00k1ng_d33p3r}"
# Secret PIN
SECRET_PIN = "shikhar45"

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html>
<head>
    <title>Punjab Kings Fan Portal</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        html, body {
            height: 100%;
            width: 100%;
        }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #DD1F2D 0%, #9E1B32 100%);
            background-attachment: fixed;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 40px;
            border-radius: 10px;
            max-width: 500px;
            width: 90%;
        }
        h1 {
            margin-bottom: 10px;
        }
        p {
            margin-bottom: 20px;
        }
        input[type="text"] {
            padding: 10px;
            width: 100%;
            margin: 10px 0;
            border-radius: 5px;
            border: none;
        }
        input[type="submit"] {
            background: #C0C0C0;
            color: #DD1F2D;
            padding: 10px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            margin-top: 10px;
        }
        input[type="submit"]:hover {
            background: #DD1F2D;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏏 Welcome to Punjab Kings Fan Portal!</h1>
        <p>Predict the next match outcome and win prizes!</p>
        <form method="POST" action="/predict">
            <label>Enter your match prediction:</label><br>
            <input type="text" name="prediction" placeholder="e.g., PBKS will win by 50 runs"><br>
            <input type="submit" value="Submit Prediction">
        </form>
    </div>
</body>
</html>'''

@app.route('/predict', methods=['POST'])
def predict():
    prediction = request.form.get('prediction', 'No prediction')
    
    # Check if user entered the secret PIN
    if prediction.strip() == SECRET_PIN:
        template = '''<!DOCTYPE html>
<html>
<head>
    <title>FLAG FOUND!</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        html, body {
            height: 100%;
            width: 100%;
        }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #DD1F2D 0%, #9E1B32 100%);
            background-attachment: fixed;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 40px;
            border-radius: 10px;
            max-width: 600px;
            width: 90%;
            text-align: center;
        }
        h2 {
            margin-bottom: 15px;
        }
        .flag {
            background: #C0C0C0;
            color: #DD1F2D;
            padding: 20px;
            border-radius: 5px;
            font-size: 20px;
            font-weight: bold;
            margin: 20px 0;
            word-wrap: break-word;
            word-break: break-all;
        }
        a {
            color: #C0C0C0;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🎉 CONGRATULATIONS! 🎉</h2>
        <p>You've discovered the secret!</p>
        <div class="flag">''' + REAL_FLAG + '''</div>
        <a href="/">← Return to Home</a>
    </div>
</body>
</html>'''
        return template
    
    # Check for simple SSTI math expressions like {{7*7}}
    math_pattern = r'{{\s*(\d+)\s*\*\s*(\d+)\s*}}'
    match = re.search(math_pattern, prediction)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        result = num1 * num2
        
        template = '''<!DOCTYPE html>
<html>
<head>
    <title>Your Prediction</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        html, body {
            height: 100%;
            width: 100%;
        }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #DD1F2D 0%, #9E1B32 100%);
            background-attachment: fixed;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 40px;
            border-radius: 10px;
            max-width: 500px;
            width: 90%;
            text-align: center;
        }
        h2 {
            margin-bottom: 15px;
        }
        p {
            margin: 10px 0;
        }
        a {
            color: #C0C0C0;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>✅ Thanks for your prediction!</h2>
        <p>You predicted: ''' + str(result) + '''</p>
        <a href="/">← Submit another prediction</a>
    </div>
</body>
</html>'''
        return template
    
   
    file_indicators = ['flag.txt', 'open(', '.read()', '__globals__', '__builtins__', 'application', 'config']
    if any(indicator in prediction for indicator in file_indicators):
        template = '''<!DOCTYPE html>
<html>
<head>
    <title>Your Prediction</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        html, body {
            height: 100%;
            width: 100%;
        }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #DD1F2D 0%, #9E1B32 100%);
            background-attachment: fixed;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 40px;
            border-radius: 10px;
            max-width: 600px;
            width: 90%;
            text-align: center;
        }
        h2 {
            margin-bottom: 15px;
        }
        .flag {
            background: #C0C0C0;
            color: #DD1F2D;
            padding: 15px;
            border-radius: 5px;
            font-weight: bold;
            margin: 20px 0;
            word-wrap: break-word;
            word-break: break-all;
        }
        a {
            color: #C0C0C0;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🤔 Nice try!</h2>
        <p>You found something!</p>
        <div class="flag">''' + FAKE_FLAG + '''</div>
        <p><small>Hint: Sometimes things aren't what they seem... explore more!</small></p>
        <a href="/">← Submit another prediction</a>
    </div>
</body>
</html>'''
        return template
    
    
    template = '''<!DOCTYPE html>
<html>
<head>
    <title>Your Prediction</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        html, body {
            height: 100%;
            width: 100%;
        }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #DD1F2D 0%, #9E1B32 100%);
            background-attachment: fixed;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 40px;
            border-radius: 10px;
            max-width: 500px;
            width: 90%;
            text-align: center;
        }
        h2 {
            margin-bottom: 15px;
        }
        p {
            margin: 10px 0;
            word-wrap: break-word;
        }
        a {
            color: #C0C0C0;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>✅ Thanks for your prediction!</h2>
        <p>You predicted: ''' + prediction + '''</p>
        <a href="/">← Submit another prediction</a>
    </div>
</body>
</html>'''
    
    return template

@app.route('/server')
def server():
    html = '''<!DOCTYPE html>
<html>
<head>
    <title>PBKS Server Stats</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        html, body {
            height: 100%;
            width: 100%;
        }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #DD1F2D 0%, #9E1B32 100%);
            background-attachment: fixed;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 40px;
            border-radius: 10px;
            max-width: 700px;
            width: 90%;
        }
        h1 {
            margin-bottom: 10px;
        }
        p {
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #C0C0C0;
        }
        th {
            background: #DD1F2D;
            color: white;
        }
        a {
            color: #C0C0C0;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 PBKS Server Statistics</h1>
        <p>Server performance metrics and information</p>
        
        <table>
            <tr>
                <th>Metric</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Server Status</td>
                <td>🟢 Online</td>
            </tr>
            <tr>
                <td>Total Predictions</td>
                <td>2,145</td>
            </tr>
            <tr>
                <td>Active Users</td>
                <td>312</td>
            </tr>
            <tr>
                <td>Server Uptime</td>
                <td>99.7%</td>
            </tr>
            <tr>
                <td>Last Match</td>
                <td>PBKS vs CSK - PBKS Won! 🎉</td>
            </tr>
            <tr>
                <td>Team's Message</td>
                <td>"True Punjab Kings fans know — when the match ends, the memories stay cached."</td>
            </tr>
        </table>
        
        <a href="/">← Back to Home</a>
    </div>
</body>
</html>'''
    
    
    response = make_response(html)
    
   
    encoded_secret = base64.b64encode(SECRET_PIN.encode()).decode()
    
   
    response.set_cookie('pbks_secret', encoded_secret, httponly=False)
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
