from flask import Flask,render_template,request,jsonify
from flask.ext.script import Manager
from flask.ext.mail import Mail,Message
from config import Config
from TDB import TDB

## create app with script encapsulation
app = Flask(__name__)
manager = Manager(app)
db = TDB(Config.DB_CONFIG)
## mail config
for key,val in Config.MAIL_CONFIG.iteritems():
    app.config[key] = val
mail = Mail(app)

## app url
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback',methods=['POST'])
def feedback():
    json = request.json
    msg = Message(json.get('subject'),
                  body = json.get('body'),
                  sender="kxqiu@chinkun.cn",
                  recipients=["kxqiu@chinkun.cn"])
    mail.send(msg)
    result = {
        'success':True,
    }
    return jsonify(result)

## register script command
@manager.command
def test():
    pass

if __name__ == '__main__':
    manager.run()
