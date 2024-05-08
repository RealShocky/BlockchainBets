### Change Log - January 7, 2023

#### Added
- Implemented registration and login functionality using Flask and Flask-WTF.
- Integrated Pi Network module for wallet management and balance retrieval.
- Added form validation for registration and login forms.
- Implemented logic for user registration, including username availability check, password hashing, and wallet address validation.
- Created routes for registration, login, logout, and homepage.
- Added logic for user login, including password verification.
- Implemented user logout functionality.
- Added route for purchasing tickets and logic for purchasing random tickets.
- Implemented error handling for 404 and 500 errors.
- Added security headers to HTTP responses.
- Created welcome message and server start message with network information.

#### Updated
- Improved error handling and logging for failed Pi Network wallet connections.
- Enhanced logging to include more detailed error messages.

#### Removed
- Removed unnecessary print statements and debug messages.

#### Fixed
- Fixed formatting issues in templates and HTML files.
- Resolved issues with incorrect attribute names and method calls in Pi Network integration.
- Fixed inconsistencies in route logic and form handling.

#### Known Issues
- Users may encounter issues with Pi Network wallet connection. Further investigation and troubleshooting are required to resolve this issue.
