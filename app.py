from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
  return "Welcome to the Flask CI/CD Demo! This is V2!"

@app.route("/new-deployment")
def new_deployment():
  return "New deployment from CI/CD"

@app.route("/info")
def info():
  user_agent = request.headers.get('User-Agent')
  return f"Your user agent is: {user_agent}"

@app.route("/cutecat")
def cutecat():
    return "Copy & paste this in your browser, i promise you will not be disappointed : https://i.pinimg.com/736x/15/4b/18/154b186e10acf78d53ddfa418aa08776.jpg"

if __name__ == "__main__":
  app.run(debug=True)
