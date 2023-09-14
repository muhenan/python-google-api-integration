from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def handle_auth_response():
    code = request.args.get('code')
    # You can print the code for testing purposes
    print(f"Authorization Code: {code}") # code can only be used once
    with open('credentials/code.txt', 'w') as file:
        file.write(code)
    return 'Authorization code captured.'

if __name__ == '__main__':
    app.run(host='localhost', port=3000)

