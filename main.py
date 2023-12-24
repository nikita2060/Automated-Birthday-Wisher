from datetime import datetime
from pathlib import Path  # Using pathlib is more preferred than using os module
import csv  # Reading file using csv module directly is more efficient than using pandas dataframes
from random import choice
import smtplib

MY_EMAIL = "learnwithpandeynikky@gmail.com" 
MY_PASSWORD = "phbkxvbtxgenipbl"
now = datetime.now()
today_tuple = (now.month, now.day)

with smtplib.SMTP("smtp.gmail.com") as connection:  # Instead of gmail , other mailing services like yahoo etc can also be used.
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)

    with open("birthdays.csv", "r") as birthday_file:
        csv_file = csv.reader(birthday_file)
        next(csv_file)  # It skips the header line so that month and day can be converted to int without string error
        for line in csv_file:
            try:
                name, email, year, month, day = line
                date_in_file = (int(month), int(day))

                if today_tuple == date_in_file:
                    folder_name = "letter_templates"
                    folder_path = Path(__file__).parent / folder_name
                    letter_list = list(folder_path.glob("*"))
                    wish_file = choice(letter_list)
                    file_path = Path(folder_path, wish_file)
                    with open(file_path, "r") as selected_wish:
                        file_contents = selected_wish.read()
                        final_file = file_contents.replace("[NAME]", name)

                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=email,
                        msg=f"Subject:Happy Birthday!\n\n{final_file}")

            except ValueError as e:
                print(f"Error Message : {str(e)}")
