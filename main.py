import email_carrier

if __name__=='__main__':
    sending_info = {
        'from_address': 'your mail address',
        'from_gmail_password': 'your gamil password',
        'to_address': ['address1', 'address2', 'address3']
    }
    subject = 'YOUR SUBJECT'
    content = 'YOUR CONTENT'
    files = ['file1', 'file2', 'file3']
    email_carrier.EmailSender(subject, content, files, sending_info)