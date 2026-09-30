from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <body color="lightblue" style="background-color: lightblue; padding: 20px; border-radius: 10px; width: 300px; margin: auto; text-align: center;">
            <form action="/greet" method="POST" style="background-color: lightblue; padding: 20px; border-radius: 10px; width: 300px; margin: auto; text-align: center;">
                Enter your name: <input type="text" name="username">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    user_input = request.form['username']
    return f"Hello {user_input}, Welcome to this app for Docker demonstration. Please consider Following me on GitHub and LinkedIn. Thank you for your support!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)