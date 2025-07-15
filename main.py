from datetime import datetime
from pathlib import Path
import csv
import smtplib
from random import choice
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Constants and credentials
MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
BIRTHDAY_FILE = "birthdays.csv"
TEMPLATE_FOLDER = "letter_templates"
EMAIL_SUBJECT = "Subject:Happy Birthday!\n\n"

def get_today_date_tuple():
    """Returns today's (month, day) as a tuple."""
    today = datetime.now()
    return today.month, today.day

def load_birthdays(file_path):
    """Loads birthday records from a CSV file."""
    birthdays = []
    try:
        with open(file_path, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) != 5:
                    print(f"Skipping malformed row: {row}")
                    continue
                name, email, year, month, day = row
                birthdays.append({
                    "name": name.strip(),
                    "email": email.strip(),
                    "date": (int(month), int(day))
                })
    except Exception as e:
        print(f"Error reading birthday file: {e}")
    return birthdays

def pick_random_template(folder):
    """Randomly selects a letter template file."""
    try:
        templates = list(Path(folder).glob("*.txt"))
        return choice(templates) if templates else None
    except Exception as e:
        print(f"Error selecting template: {e}")
        return None

def personalize_template(template_path, name):
    """Replaces [NAME] placeholder with the actual name."""
    try:
        with open(template_path, "r") as file:
            content = file.read()
            return content.replace("[NAME]", name)
    except Exception as e:
        print(f"Error reading template: {e}")
        return ""

def send_email(recipient_email, message_body):
    """Sends the email using SMTP."""
    if not MY_EMAIL or not MY_PASSWORD:
        raise EnvironmentError("EMAIL or PASSWORD not set in .env")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=recipient_email,
                msg=EMAIL_SUBJECT + message_body
            )
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

def main():
    today = get_today_date_tuple()
    birthdays = load_birthdays(BIRTHDAY_FILE)

    for entry in birthdays:
        if entry["date"] == today:
            template = pick_random_template(TEMPLATE_FOLDER)
            if template:
                message = personalize_template(template, entry["name"])
                if message:
                    send_email(entry["email"], message)

if __name__ == "__main__":
    main()
