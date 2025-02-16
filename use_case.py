import logging
import re
from logger_config import setup_logging


def validate_first_name(name):
    """Validates the first name using regex."""
    pattern=r"^[A-Z][a-zA-Z]{2,}$"
    
    if re.fullmatch(pattern, name):
        message=f"Valid First Name: '{name}'"
        logging.info(message)
        print(message)
        return True
    else:
        message=f"Invalid First Name: '{name}' - It should start with a capital letter, have at least 3 characters, and contain only alphabets."
        logging.error(message)
        print(message)
        return False

def main():
    """Runs the user input loop until a valid name is entered."""
    setup_logging()
    
    while True:
        try:
            name=input("Enter first name: ").strip()
            if not name:
                raise ValueError("Input cannot be empty.")
            if validate_first_name(name):
                break
        except ValueError as e:
            logging.warning(f"Invalid input: {e}")
            print(e)
        except Exception as e:
            logging.critical(f"Unexpected error: {e}")
            print("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    main()
