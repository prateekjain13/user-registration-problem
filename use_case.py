import re
import logging

logging.basicConfig(filename='UC7_log_file.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_name(name,name_type):
    logging.debug(f"Received input for {name_type} validation: '{name}'")
    if len(name)<3 and name[0].isupper():
        message=f"Invalid {name_type}: '{name}' - Your name should have at least 3 characters."
        logging.error(message)
        print(message)
    elif len(name)>=3 and not name[0].isupper():
        message=f"Invalid {name_type}: '{name}' - The first letter should be capital."
        logging.error(message)
        print(message)
    elif len(name)<3 and not name[0].isupper():
        message=f"Invalid {name_type}: '{name}' - The first letter should be capital and it should have at least 3 characters."
        logging.critical(message)
        print(message)
    else:
        message=f"Valid {name_type}: '{name}'"
        logging.info(message)
        print(message)

def validate_email(email):
    logging.debug(f"Received input for Email validation: '{email}'")
    pattern=r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$'
    if re.fullmatch(pattern,email):
        message=f"Valid Email: '{email}'"
        logging.info(message)
        print(message)
    else:
        message=f"Invalid Email: '{email}' - Your email should follow the pattern abc.xyz@bl.co.in"
        logging.error(message)
        print(message)

def validate_mobile(mobile):
    logging.debug(f"Received input for Mobile validation: '{mobile}'")
    pattern=r'^[0-9]{2} [0-9]{10}$'
    if re.fullmatch(pattern,mobile):
        message=f"Valid Mobile Number: '{mobile}'"
        logging.info(message)
        print(message)
    else:
        message=f"Invalid Mobile Number: '{mobile}' - Your mobile number should follow the pattern '91 9919819801'"
        logging.error(message)
        print(message)

def validate_password(password):
    logging.debug(f"Received input for Password validation: '{password}'")
    pattern=r'^(?=.*[A-Z])(?=.*\d).{8,}$'
    if not re.fullmatch(pattern, password):
        message=f"Invalid Password: '{password}' - Your password should have at least 8 characters, at least 1 uppercase letter, and at least 1 numeric digit."
        logging.error(message)
        print(message)
    else:
        message=f"Valid Password"
        logging.info(message)
        print(message)

first_name=input("Enter first name: ")
validate_name(first_name,"First Name")

last_name=input("Enter last name: ")
validate_name(last_name,"Last Name")

email=input("Enter email: ")
validate_email(email)

mobile=input("Enter mobile number: ")
validate_mobile(mobile)

password=input("Enter password: ")
validate_password(password)
