import os
import smtplib
from email.mime.multipart import MIMEMultipart  # For creating a multipart email message
from email.mime.text import MIMEText  # For creating text/plain or text/html email content
from email.mime.base import MIMEBase  # Base class for email attachments
from email import encoders  # For encoding attachments

class EmailSender:
    def __init__(self, subject, content, files, sending_info):
        """
        Initialize the EmailSender class.
        
        Parameters:
        subject (str): The subject of the email.
        content (str): The body content of the email.
        files (list): A list of file paths to attach to the email.
        sending_info (dict): A dictionary containing email sending information, including 'from_address', 
                             'from_gmail_password', and 'to_address'.
        """
        self.mail = MIMEMultipart()
        self.mail['From'] = sending_info['from_address']  # Sender's email address
        self.gmail_password = sending_info['from_gmail_password']  # Sender's Google account application password
        self.to_address = sending_info['to_address']  # List of recipient email addresses
        self.mail['To'] = ', '.join(self.to_address)  # Join recipient emails into a single string
        self.subject = subject
        self.content = content
        self.files = files 

        self.write_content()  # Call method to write the email content
        self.attach_files()  # Call method to attach files to the email
        self.send_email()  # Call method to send the email

    def write_content(self):
        """
        Write the subject and body content of the email.
        """
        self.mail['Subject'] = self.subject
        self.mail.attach(MIMEText(self.content))  # Attach the email body content

    def attach_files(self):
        """
        Attach files to the email.
        """
        for file in self.files:
            filename = os.path.basename(file)  # Get the base name of the file
            with open(file, 'rb') as fp:  # Open the file in binary read mode
                add_file = MIMEBase('application', "octet-stream")  # Create a MIMEBase object
                add_file.set_payload(fp.read())  # Set the payload to the file's content
            encoders.encode_base64(add_file)  # Encode the file's payload using base64
            add_file.add_header('Content-Disposition', 'attachment', filename=filename)  # Add the necessary headers
            self.mail.attach(add_file)  # Attach the file to the email

    def send_email(self):
        """
        Send the email using Gmail's SMTP server.
        """
        smtpserver = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # Connect to Gmail's SMTP server using SSL
        smtpserver.ehlo()  # Identify yourself to the server
        smtpserver.login(self.mail['From'], self.gmail_password)  # Login to the SMTP server
        smtpserver.sendmail(self.mail['From'], self.to_address, self.mail.as_string())  # Send the email
        smtpserver.quit()  # Disconnect from the server
