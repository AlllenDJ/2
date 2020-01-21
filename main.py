from flask import Flask, render_template

app = Flask(__name__)

@app.route('/chat')
def chat():
  return render_template('chat.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 5222, threaded = True, debug = True)