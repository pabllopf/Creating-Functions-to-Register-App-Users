![image](https://github.com/user-attachments/assets/7b31247f-4345-4398-b201-dbbec81e0845)


# Creating-Functions-to-Register-App-Users
Define functions to catch errors when new users register for an app!

# Description: 
You are a junior developer working on a registration system for a mobile app at a small startup. The product managers have asked you to improve the current sign-up flow by integrating reusable Python functions that validate user input entered into the form.

Your task is to integrate these validation functions to approve or reject sign-up attempts before account creation. Together, these existing validation functions and the new registration functions you will build will significantly improve the robustness and quality of the sign-up process, enhancing onboarding for thousands of app users.

# Project Instructions
Create a validate_user() function, using some helper validation functions to validate user input.

The function should take in the parameters: name, email and password.
The function should call each of the helper validation functions and raise a ValueError with a descriptive error message if any of the inputs fail validation.
If all of the checks pass, the function should return a Boolean value of True.
Now that you've validated that all the user details are correct, you want to allow users to register to the app. Create a register_user() function that registers the user if all checks pass.

The function should take in the parameters: name, email and password.
The function should call validate_user() to ensure that the user input is valid.
If all checks pass, the function should create a dictionary with the keys: name, email, password.
The function should return the new user dictionary, or the boolean value of False.

