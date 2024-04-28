from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

# Import the Pi Coin SDK
# Replace "pi_coin_sdk" with the actual name of the Pi Coin SDK package
import pi_coin_sdk

app = Flask(__name__)

# Dummy database to store user information
users = []

# Initialize Pi Coin SDK
pi_sdk = pi_coin_sdk.PiCoinSDK()

# List of countries where online gambling is allowed
allowed_countries = ['US', 'UK', 'Canada', 'Australia']  # Add more countries as needed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        wallet_address = request.form['wallet_address']
        verify_wallet_address = request.form['verify_wallet_address']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        country = request.form['country']
        
        # Check if username is already taken
        if any(user['username'] == username for user in users):
            return 'Username is already taken!', 400
        
        # Check if wallet address and verify wallet address match
        if wallet_address != verify_wallet_address:
            return 'Wallet addresses do not match!', 400
        
        # Verify wallet address using Pi Coin SDK
        if not pi_sdk.verify_wallet(wallet_address):
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
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
