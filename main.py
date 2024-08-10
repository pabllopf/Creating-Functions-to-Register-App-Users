# Re-run this cell and examine the docstring of each function
from python_functions import validate_name, validate_email, validate_password, top_level_domains

print("validate_name\n")
print(validate_name.__doc__)
print("--------------------\n")

print("validate_email\n")
print(validate_email.__doc__) 
print("--------------------\n")

print("validate_password\n")
print(validate_password.__doc__)

# The top level domains variable is used in validate_email to approve only certain email domains
print(top_level_domains)

def validate_user(name, email, password):
    """Validate user input by calling validation functions.
    
    Args:
        name (str): The user's name.
        email (str): The user's email address.
        password (str): The user's password.
        
    Returns:
        bool: True if all validations pass.
        
    Raises:
        ValueError: If any of the validations fail.
    """
    # Validate name
    if not validate_name(name):
        raise ValueError("Invalid name. The name must be greater than 2 characters and a string.")
    
    # Validate email
    if not validate_email(email):
        raise ValueError("Invalid email. Please provide a valid email address.")
    
    # Validate password
    if not validate_password(password):
        raise ValueError("Invalid password. The password must be at least 8 characters long, contain a mix of letters, numbers, and symbols.")
    
    # If all checks pass
    return True

def register_user(name, email, password):
    """Register a user by validating input and creating a user dictionary.
    
    Args:
        name (str): The user's name.
        email (str): The user's email address.
        password (str): The user's password.
        
    Returns:
        dict or bool: A dictionary with user details if registration is successful; otherwise, False.
    """
    
    # Validate user input
    if(validate_user(name, email, password)):
        # Create user dictionary
        user = {
            'name': name,
            'email': email,
            'password': password
        }
        return user
    
    return False
