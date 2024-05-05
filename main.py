from flask import Flask, render_template, request, redirect, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from pi_network import PiNetwork

app = Flask(__name__)
app.secret_key = 'SAIU3MHM7O4LAW4GSZY7T7QZS6FQTGCMDQHOR7SBHGJVKZD3MLQRWZVR'

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    pi_wallet_address = StringField('Pi Coin Wallet Address', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_pi_wallet_address(form, field):
        pi_network = PiNetwork()
        pi_network.initialize()
        try:
            balance = pi_network.get_balance(field.data)
            if balance <= 0:
                raise ValidationError('Invalid Pi Coin wallet address')
        except Exception as e:
            raise ValidationError('Error validating Pi Coin wallet address')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect('/login')
    else:
        pi_network = PiNetwork()
        try:
            pi_network.initialize()
            pi_balance = pi_network.get_balance()
            return render_template('index.html', username=session['username'], pi_balance=pi_balance)
        except Exception as e:
            error_message = str(e)
            return render_template('error.html', error_message=error_message)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        flash('Registration successful', 'success')
        return redirect('/')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            session['username'] = form.username.data
            flash('Login successful', 'success')
            return redirect('/')
        else:
            flash('Invalid username or password', 'error')
            return redirect('/login')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)