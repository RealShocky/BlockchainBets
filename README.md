# BlockchainBets

**Description:**

BlockchainBets is an innovative online casino platform that leverages blockchain technology to offer a secure and transparent gambling experience. Our platform is powered by the Pi blockchain, allowing users to engage in various games of chance while utilizing Pi Coins, a digital currency built on top of the blockchain.

**Key Features:**

1. **Secure and Transparent:** With blockchain technology, BlockchainBets ensures that all transactions and game outcomes are transparent and verifiable. Each transaction is recorded on the immutable Pi blockchain, providing users with a high level of security and trust.

2. **Pi Coin Integration:** Users can participate in games using Pi Coins, a cryptocurrency native to the Pi blockchain. Pi Coins can be earned by participating in the Pi network's consensus mechanism or purchased from cryptocurrency exchanges.

3. **Variety of Games:** BlockchainBets offers a wide range of casino games, including slot machines, poker, blackjack, roulette, and more. Each game is designed to provide an exciting and entertaining gambling experience for users.

4. **User-Friendly Interface:** Our platform features a user-friendly interface that allows players to easily navigate between different games, view their account balance, and track their transaction history.

5. **Registration and Authentication:** Users can create an account on BlockchainBets by providing basic information such as username, password, Pi Coin wallet address, first name, last name, and country. The registration process is straightforward and ensures the security of user accounts.

6. **Integration with Pi Coin SDK:** BlockchainBets integrates with the Pi Coin SDK to interact with the Pi blockchain. This allows us to verify user wallet addresses, retrieve Pi Coin balances, and facilitate secure transactions on the platform.

7. **Responsible Gambling:** We promote responsible gambling practices and provide resources for users to set limits on their spending, take breaks from gambling, and seek help if needed. Our platform encourages a safe and enjoyable gambling experience for all users.

**Mission:**

Our mission at BlockchainBets is to revolutionize the online gambling industry by harnessing the power of blockchain technology. We strive to provide a secure, transparent, and entertaining platform for users to engage in casino games while promoting responsible gambling practices.

**Vision:**

Our vision is to become the leading online casino platform powered by Here's a detailed changelog of the coding process we went through:

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
We built a secure and transparent online casino platform, BlockchainBets, using Flask and Pi Coin SDK. Users can register, authenticate, and enjoy various casino games powered by blockchain technology. The frontend provides a user-friendly interface, while the backend ensures security, error handling, and integration with the Pi blockchain.blockchain technology. We aim to attract a global user base and establish BlockchainBets as a trusted and reputable brand in the online gambling industry.

With BlockchainBets, users can enjoy the thrill of gambling with confidence, knowing that their transactions are secure, their data is protected, and their gaming experience is fair and transparent. Join us today and experience the future of online gambling with BlockchainBets!


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
