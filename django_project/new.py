import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

print(AWS_ACCESS_KEY_ID)
print(EMAIL_HOST_USER)
print(EMAIL_HOST_PASSWORD)
