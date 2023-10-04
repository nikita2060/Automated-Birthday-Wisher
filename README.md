# Automated-Birthday-Wisher

This Python script automates the process of sending birthday emails to people listed in a birthdays.csv file. It reads the CSV file, checks for birthdays matching the current date, and sends a birthday email to the respective recipients using Gmail's SMTP server.

## Prerequisites

Before running the script, make sure you have the following in place:

-A Gmail account with your email and password.

-A birthdays.csv file containing the list of birthdays in the following format:

#### _Name, Email, Year, Month, Day_

Make sure to include headers in the CSV file, and specify the recipient's name, email address, birth year, birth month, and birth day.
Example:

#### *Nikita Pandey, nikita@example.com, 2004, 02, 02*

## **Usage**

Clone or download this repository to your local machine.

Update the following variables in the script with your Gmail email address and password:


MY_EMAIL = "your_email@gmail.com"

MY_PASSWORD = "your_password"

Ensure you have a folder named letter_templates in the same directory as the script. 

Inside this folder, you can create birthday letter templates named as you like (e.g., letter1.txt, letter2.txt, etc.), and use [NAME] as a placeholder for the recipient's name.

## Run the script using a Python interpreter:

CODE:
_python birthday_email.py_


The script will read the birthdays.csv file, compare birthdays with the current date, and send birthday emails using Gmail's SMTP server.

Notes:

1. The script will skip the header line in the birthdays.csv file and handle errors related to invalid data.
2. Make sure to keep your Gmail password secure. 
3. It is recommended to use environment variables to store sensitive information.