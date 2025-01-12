from flask import Flask, request, render_template
from flask import redirect, url_for
from models import db, User
from forms import UserForm
import os
from file_handler import FileHandler

app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
google_maps_key = os.environ.get('GOOGLE_MAPS_KEY')
# Initialize the database with the app
db.init_app(app)

# Create the database tables (run this once)
# with app.app_context():
#     db.create_all()

firstname_handler = FileHandler('firstnames.txt')
lastname_handler = FileHandler('lastnames.txt')


@app.route('/users', methods=['GET'],endpoint='list_users')
def list_users():
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Adjust as needed
    
    # Use the paginate method provided by Flask-SQLAlchemy
    pagination = User.query.paginate(page=page, per_page=per_page, error_out=False)
    
    return render_template('users/index.html', users=pagination)

@app.route('/users/<int:user_id>', methods=['GET'],endpoint='show_user')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

@app.route('/users/create', methods=['GET'],endpoint='new_user')
def create_user():
    form = UserForm()
    firstnames = firstname_handler.get_names()
    lastnames = lastname_handler.get_names()
    return render_template('users/create.html', 
                           form=form, firstnames=firstnames, lastnames=lastnames, google_maps_key=google_maps_key)

@app.route('/users', methods=['POST'],endpoint="register")
def save_user():
    form = UserForm(request.form)
    if not form.validate():
        return render_template('users/create.html', form=form)
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    nin = request.form['nin']
    phone_no = request.form['phone_no']
    next_of_kin = request.form['next_of_kin_firstname'] + ' ' + request.form['next_of_kin_lastname']
    next_of_kin_phone_no = request.form['next_of_kin_phone_no']
    district = request.form['district']
    subcounty = request.form['subcounty']
    parish = request.form['parish']
    village = request.form['village']
    residence = request.form['residence']
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    user = User(firstname=firstname, lastname=lastname, nin=nin, phone_no=phone_no, next_of_kin=next_of_kin, next_of_kin_phone_no=next_of_kin_phone_no, district=district, subcounty=subcounty, parish=parish, village=village, residence=residence, latitude=latitude, longitude=longitude)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('list_users'))

@app.route('/', methods=['GET'],endpoint='dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True,port=6500)
