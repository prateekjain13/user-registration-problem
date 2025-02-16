import logging
import re
from logger_config import setup_logging


def validate_name(name, name_type):
    """Validates a name using regex."""
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

def main():
    """Runs input validation until valid details are entered."""
    setup_logging()
    
    while True:
        first_name=input("Enter first name: ").strip()
        if validate_name(first_name, "first name"):
            break
    
    while True:
        last_name=input("Enter last name: ").strip()
        if validate_name(last_name, "last name"):
            break
    
    while True:
        email=input("Enter email: ").strip()
        if validate_email(email):
            break

if __name__ == "__main__":
    main()
