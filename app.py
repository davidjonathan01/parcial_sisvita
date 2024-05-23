from flask import Flask
from utils.db import db
#from services.contact import contacts
from services.hist_eval_ansiedad import hist_eval_ansiedad_routes
from services.exp_psi_estudiante import exp_psi_estudiante_routes
from services.test_ansiedad import test_ansiedad_routes
from services.estudiante import estudiante_routes
from services.eval_ansiedad import eval_ansiedad_routes
from functions.realizar_test_ansiedad import cus
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

#SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(test_ansiedad_routes)
app.register_blueprint(estudiante_routes)
app.register_blueprint(exp_psi_estudiante_routes)
app.register_blueprint(eval_ansiedad_routes)
app.register_blueprint(hist_eval_ansiedad_routes)
app.register_blueprint(cus, url_prefix='/cus')




with app.app_context():
    db.create_all

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True,port=5000)