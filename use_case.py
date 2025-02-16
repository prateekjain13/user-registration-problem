import logging
import re
from logger_config import setup_logging


def validate_name(name, name_type):
    """Validates name using regex."""
    pattern=r"^[A-Z][a-zA-Z]{2,}$"
    
    if re.fullmatch(pattern, name):
        message=f"Valid {name_type}: '{name}'"
        logging.info(message)
        print(message)
        return True
    else:
        message=f"Invalid {name_type}: '{name}' - It should start with a capital letter, have at least 3 characters, and contain only alphabets."
        logging.error(message)
        print(message)
        return False

def validate_email(email):
    """Validates an email using regex."""
    pattern=r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$'
    
    if re.fullmatch(pattern, email):
        message=f"Valid Email: '{email}'"
        logging.info(message)
        print(message)
        return True
    else:
        message=f"Invalid Email: '{email}' - Your email should follow the pattern abc.xyz@bl.co.in"
        logging.error(message)
        print(message)
        return False

def validate_mobile(mobile):
    """Validates a mobile number using regex."""
    pattern=r'^[0-9]{2} [0-9]{10}$'
    
    if re.fullmatch(pattern, mobile):
        message=f"Valid Mobile Number: '{mobile}'"
        logging.info(message)
        print(message)
        return True
    else:
        message=f"Invalid Mobile Number: '{mobile}' - It should follow the pattern '91 9919819801'"
        logging.error(message)
        print(message)
        return False

def validate_password(password):
    """Validates a password with at least 8 characters."""
    pattern=r'^.{8,}$'
    
    if re.fullmatch(pattern, password):
        message="Valid Password"
        logging.info(message)
        print(message)
        return True
    else:
        message=f"Invalid Password: '{password}' - It should have at least 8 characters."
        logging.error(message)
        print(message)
        return False

def main():
    """Runs input validation until valid details are entered."""
    setup_logging()
    
    while True:
        first_name=input("Enter first name: ").strip()
        if validate_name(first_name, "First Name"):
            break
    
    while True:
        last_name=input("Enter last name: ").strip()
        if validate_name(last_name, "Last Name"):
            break
    
    while True:
        email=input("Enter email: ").strip()
        if validate_email(email):
            break
    
    while True:
        mobile=input("Enter mobile number: ").strip()
        if validate_mobile(mobile):
            break

    while True:
        password=input("Enter password: ").strip()
        if validate_password(password):
            break

if __name__ == "__main__":
    main()




