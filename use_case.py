import re
import logging

logging.basicConfig(filename='UC1_log_file.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_first_name(name):
    logging.debug(f"Received input for validation: '{name}'")
    if len(name)<3 and name[0].isupper():
        message=(f"Invalid First Name: '{name}' - It should have atleast 3 characters.")
        logging.error(message)
        print(message)
    elif len(name)>=3 and not name[0].isupper():
        message=(f"Invalid First Name: '{name}' - The first letter should be capital.")
        logging.error(message)
        print(message)
    elif len(name)<3 and not name[0].isupper():
        message=(f"Invalid First Name: '{name}' - The first letter should be capital and it should also have atleast 3 characters.")
        logging.critical(message)
        print(message)
    else:
        message=(f"Valid First Name: '{name}'")
        logging.info(message)
        print(message)

name=input("Enter first name: ")
validate_first_name(name)


