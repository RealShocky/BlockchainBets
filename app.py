from flask import Flask, render_template, request, redirect, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import random

# Import the Pi Network module
from pi_network import PiNetwork

app = Flask(__name__)
app.secret_key = ''

# Dummy database to store user information
users = []

# Initialize Pi Network
pi_network = PiNetwork()
try:
    pi_network.initialize(wallet_private_key="", network=" ")
    pi_network.get_account_info("dummy_account_id")  # Dummy call to check if connection is successful
    connection_successful = True
except Exception as e:
    connection_successful = False
    print("Failed to connect to the Pi Network wallet. Please check your wallet configuration.")
    print(f"Error message: {str(e)}")

# List of countries where online gambling is allowed
allowed_countries = ['US', 'UK', 'Canada', 'Australia']  # Add more countries as needed

# Prize pool amount and next drawing date
prize_pool = 10
next_drawing = datetime.datetime.now() + datetime.timedelta(days=(6 - datetime.datetime.now().weekday()) % 7 + 1, hours=18)  # Next Sunday 6:00 PM

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    wallet_address = StringField('Pi Coin Wallet Address', validators=[DataRequired()])
    verify_wallet_address = StringField('Verify Pi Coin Wallet Address', validators=[DataRequired(), EqualTo('wallet_address', message='Wallet addresses must match')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    country = SelectField('Country', choices=[('US', 'United States'), ('UK', 'United Kingdom'), ('Canada', 'Canada'), ('Australia', 'Australia')], validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route('/')
def index():
    current_user = session.get('username')
    current_user_pi_balance = None
    if current_user:
        # Retrieve the user's Pi Coin balance from the Pi Network module
        try:
            current_user_pi_balance = pi_network.get_balance(current_user)  # Assuming username is the wallet address
        except Exception as e:
            error_message = str(e)
            return render_template('error.html', error_message=error_message)
    return render_template('index.html', current_user=current_user, current_user_pi_balance=current_user_pi_balance, prize_pool=prize_pool, next_drawing=next_drawing)

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
            flash('Username is already taken!', 'error')
            return redirect('/register')
        
        # Verify wallet address using Pi Network module
        try:
            balance = pi_network.get_balance(wallet_address)
            if balance <= 0:
                flash('Invalid Pi Coin wallet address!', 'error')
                return redirect('/register')
        except Exception as e:
            flash('Error validating Pi Coin wallet address!', 'error')
            return redirect('/register')
        
        # Check if online gambling is allowed in the chosen country
        if country not in allowed_countries:
            flash('Online gambling is not allowed in your country!', 'error')
            return redirect('/register')
        
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
        
        flash('Registration successful', 'success')
        print(f"User {username} registered successfully")
        return redirect('/')
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # Check if the username exists in the database
        user = next((user for user in users if user['username'] == username), None)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            flash('Login successful', 'success')
            print(f"User {username} logged in successfully")
            return redirect('/')
        else:
            flash('Invalid username or password', 'error')
            return redirect('/login')
    
    flash('Invalid username or password', 'error')
    return redirect('/login')

@app.route('/logout')
def logout():
    current_user = session.get('username')
    session.pop('username', None)
    flash('You have been logged out', 'info')
    if current_user:
        print(f"User {current_user} logged out")
    return redirect('/login')

@app.route('/buy_ticket', methods=['POST'])
def buy_ticket():
    current_user = session.get('username')
    if not current_user:
        flash('You must be logged in to buy a ticket', 'error')
        return redirect('/login')
    
    # Get the selected ticket numbers from the form
    ticket_numbers = request.form.getlist('ticket_numbers')

    # Validate the ticket numbers
    if len(ticket_numbers) != 3:
        flash('You must select exactly 3 ticket numbers', 'error')
        return redirect('/')

    # Convert the ticket numbers to integers
    try:
        ticket_numbers = [int(num) for num in ticket_numbers]
    except ValueError:
        flash('Invalid ticket numbers', 'error')
        return redirect('/')

    # Check if all ticket numbers are between 0 and 9
    if not all(0 <= num <= 9 for num in ticket_numbers):
        flash('Ticket numbers must be between 0 and 9', 'error')
        return redirect('/')

    # Logic to deduct Pi Coins from the user's balance and purchase the ticket goes here
    # This would involve deducting the appropriate amount of Pi Coins from the user's balance,
    # generating a unique ticket ID, and storing the ticket information in a database or blockchain

    flash('Ticket purchased successfully!', 'success')
    print(f"User {current_user} purchased a ticket with numbers: {ticket_numbers}")
    return redirect('/')

@app.route('/buy_random_ticket', methods=['POST'])
def buy_random_ticket():
    current_user = session.get('username')
    if not current_user:
        flash('You must be logged in to buy a ticket', 'error')
        return redirect('/login')

    # Generate a random ticket with 3 random numbers between 0 and 9
    ticket_numbers = [random.randint(0, 9) for _ in range(3)]

    # Logic to deduct Pi Coins from the user's balance and purchase the ticket goes here
    # This would involve deducting the appropriate amount of Pi Coins from the user's balance,
    # generating a unique ticket ID, and storing the ticket information in a database or blockchain

    flash('Random ticket purchased successfully!', 'success')
    print(f"User {current_user} purchased a random ticket")
    return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error_message='Page not found'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error_message='Internal server error'), 500

@app.after_request
def add_security_headers(response):
    if request.path not in ['/', '/register', '/login', '/logout']:
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        
        # Content Security Policy (CSP)
        csp_policy = "default-src 'self'; script-src 'self' https://cdn.example.com; style-src 'self' https://cdn.example.com"
        response.headers['Content-Security-Policy'] = csp_policy
    
    return response

if __name__ == '__main__':
    print("Welcome to BlockchainBets!")
    if connection_successful:
        print("Successfully connected to the Pi Network wallet.")
    else:
        print("Failed to connect to the Pi Network wallet. Please check your wallet configuration.")
    print("Running on Network: Pi Network")
    print("If you encounter any issues, please contact support.")
    app.run(debug=True)