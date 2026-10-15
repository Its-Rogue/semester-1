# Week 1.3, Session 2: Email Extractor

raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com", "UserB@yahoo.com", "admin@site.com"]


# set comprehension to extract a clean, unique set of lowercase email addresses

unique_emails = {value.lower() for value in raw_emails}


# print the clean set of email addressed

print(unique_emails)

# Optional - consider the case where some of the emails are not valid (i.e., without the @ in the email address).
raw_emails2 = ["UserA@gmail.com", "SYSTEM_ALERT", "usera@gmail.com", "admin@site.com", "UserB@yahoo.com"]
# write another set comprehension for this case to extract a clean, unique set of valid, lowercase email addresses

unique_emails2 = {value.lower() for value in raw_emails2 if '@' in value}

print(unique_emails2)