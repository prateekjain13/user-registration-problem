import re
import logging

logging.basicConfig(filename='UC3_log_file.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_name(name,name_type):
    logging.debug(f"Received input for {name_type} validation: '{name}'")
    if len(name)<3 and name[0].isupper():
        message=(f"Invalid {name_type}: '{name}' - It should have at least 3 characters.")
        logging.error(message)
        print(message)
    elif len(name)>=3 and not name[0].isupper():
        message=(f"Invalid {name_type}: '{name}' - The first letter should be capital.")
        logging.error(message)
        print(message)
    elif len(name)<3 and not name[0].isupper():
        message=(f"Invalid {name_type}: '{name}' - The first letter should be capital and it should also have at least 3 characters.")
        logging.critical(message)
        print(message)
    else:
        message=(f"Valid {name_type}: '{name}'")
        logging.info(message)
        print(message)
        
def validate_email(email):
    logging.debug(f"Received input for Email validation: '{email}'")
    pattern=r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$'
    if re.fullmatch(pattern,email):
        message=(f"Valid Email: '{email}'")
        logging.info(message)
        print(message)
    else:
        message=(f"Invalid Email: '{email}' - Your email should follow the pattern abc.xyz@bl.co.in")
        logging.error(message)
        print(message)



first_name=input("Enter first name: ")
validate_name(first_name,"first name")

last_name=input("Enter last name: ")
validate_name(last_name,"last name")

email=input("Enter email: ")
validate_email(email)
