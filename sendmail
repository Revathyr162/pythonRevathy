import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mail_slicer(email):
    # Split the email address into username and domain
    username, domain = email.split('@')
    return username, domain

def send_email(receiver_email, subject, message):
    # Sender and receiver email addresses
    sender_email = 'your_email@example.com'
    receiver_email = receiver_email

    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Connect to SMTP server
    with smtplib.SMTP('smtp.example.com', 587) as server:
        # Start TLS for security
        server.starttls()
        # Login to the server
        server.login(sender_email, 'your_password')
        # Send email
        server.sendmail(sender_email, receiver_email, msg.as_string())

def main():
    # Prompt user to enter email address
    email = input("Enter email address: ")
    username, domain = mail_slicer(email)
    print("Username:", username)
    print("Domain:", domain)

    # Send email to the sliced address
    subject = "Test Email"
    message = "This is a test email sent using Python."
    send_email(email, subject, message)
    print("Email sent successfully!")

if __name__ == "__main__":
    main()
