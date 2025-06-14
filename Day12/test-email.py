import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "nickymaharjan2003@gmail.com"
receiver_email = "nick"
password = "your_password"  # Or use app-specific password
smtp_server = "smtp.example.com"  # e.g., smtp.gmail.com
port = 587  # For starttls

# Read HTML file
with open('your_file.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Your HTML Email"

# Attach HTML content
msg.attach(MIMEText(html_content, 'html'))

# Send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()