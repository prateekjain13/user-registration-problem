# User-Registration-Problem
This project implements a User Registration System in Python with input validation for names, email, mobile number, and password using regular expressions (regex). It also includes logging to tarck validation attempts.

Features: 

1) Name Validation: Ensures first and last names start with a capital letter and have at least 3 characters.

2) Email Validation: Supports emails in the format abc.xyz@bl.co.in.

3) Mobile Number Validation: Must follow the format 91 9919819801 (country code + 10-digit number).

4) Password Validation:

	At least 8 characters long

	At least 1 uppercase letter

	At least 1 numeric digit

	At least 1 special character

5) Logging: All validation attempts (success or failure) are logged into separate log files.


Logging Details: 

1) Logs are stored in separate log file (user_registration.log).

2) Each log contains:

	Timestamp

	Log Level (INFO, ERROR, CRITICAL)

	Validation Messages
