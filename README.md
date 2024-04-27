# BlockchainBets

1. **Project Setup**:
   - Created a new Flask project directory.
   - Set up the directory structure with Python files for server-side logic and HTML templates for the frontend.

2. **User Registration**:
   - Implemented a registration form using Flask-WTF for form validation.
   - Added fields for username, password, Pi Coin wallet address, first name, last name, and country.
   - Validated user input, including ensuring unique usernames, matching wallet addresses, and allowed countries for online gambling.

3. **User Authentication**:
   - Implemented user authentication using session management in Flask.
   - Added login and logout routes to handle user authentication.
   - Hashed and stored user passwords securely using `generate_password_hash` from Werkzeug.

4. **Integration with Pi Coin SDK**:
   - Integrated the Pi Coin SDK into the Flask application to interact with the Pi blockchain.
   - Verified Pi Coin wallet addresses during user registration.
   - Retrieved the user's Pi Coin balance from the Pi blockchain to display in the user interface.

5. **Frontend Development**:
   - Designed and developed the frontend of the application using HTML and CSS.
   - Created the `index.html` template to display user information, Pi Coin balance, and the lottery game.
   - Designed the `register.html` template for the user registration form.

6. **Error Handling and Security Enhancements**:
   - Implemented error handling for 404 and 500 errors using Flask error handlers.
   - Added security headers, including `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`, and Content Security Policy (CSP).
   - Ensured input validation and error message handling in both server-side and client-side code.

7. **Testing and Deployment**:
   - Tested the application locally to ensure all functionalities work as expected.
   - Deployed the application to a production environment, such as a web server or cloud platform.

**Summary**:
We built a secure and transparent online casino platform, BlockchainBets, using Flask and Pi Coin SDK. Users can register, authenticate, and enjoy various casino games powered by blockchain technology. The frontend provides a user-friendly interface, while the backend ensures security, error handling, and integration with the Pi blockchain.
