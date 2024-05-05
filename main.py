from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, EqualTo

# Import the Pi Network module
import pi_network

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Dummy database to store user information
users = []

# Initialize Pi Network
#pi_network.initialize()

# List of countries where online gambling is allowed
allowed_countries = ['US', 'UK', 'Canada', 'Australia']  # Add more countries as needed

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    wallet_address = StringField('Pi Coin Wallet Address', validators=[DataRequired()])
    verify_wallet_address = StringField('Verify Pi Coin Wallet Address', validators=[DataRequired(), EqualTo('wallet_address', message='Wallet addresses must match')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    country = SelectField('Country', choices=[('US', 'United States'), ('UK', 'United Kingdom'), ('Canada', 'Canada'), ('Australia', 'Australia')], validators=[DataRequired()])

@app.route('/')
def index():
    current_user = session.get('username')
    current_user_pi_balance = None
    if current_user:
        # Retrieve the user's Pi Coin balance from the Pi Network module
        current_user_pi_balance = pi_network.get_balance(current_user)  # Assuming username is the wallet address
    return render_template('index.html', current_user=current_user, current_user_pi_balance=current_user_pi_balance)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        wallet_address = form.wallet_address.data
        verify_wallet_address = form.verify_wallet_address.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        country = form.country.data
        
        # Check if username is already taken
        if any(user['username'] == username for user in users):
            return 'Username is already taken!', 400
        
        # Verify wallet address using Pi Network module
        if not pi_network.verify_wallet(wallet_address):
            return 'Invalid wallet address!', 400
        
        # Check if online gambling is allowed in the chosen country
        if country not in allowed_countries:
            return 'Online gambling is not allowed in your country!', 400
        
        # Hash the password before storing it
        hashed_password = generate_password_hash(password)
        
        # Store the user information in the database
        users.append({
            'username': username,
            'password': hashed_password,
            'wallet_address': wallet_address,
            'first_name': first_name,
            'last_name': last_name,
            'country': country
        })
        
        return redirect(url_for('index'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the username exists in the database
    user = next((user for user in users if user['username'] == username), None)
    if user and check_password_hash(user['password'], password):
        session['username'] = username
        return redirect(url_for('index'))
    else:
        return 'Invalid username or password', 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error_message='Page not found'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error_message='Internal server error'), 500

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    
    # Content Security Policy (CSP)
    csp_policy = "default-src 'self'; script-src 'self' https://cdn.example.com; style-src 'self' https://cdn.example.com"
    response.headers['Content-Security-Policy'] = csp_policy
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
