# EmailSender

`EmailSender` is a Python class for sending emails with attachments using Gmail's SMTP server.

## Features

- Send emails via Gmail's SMTP server.
- Include a subject and body content.
- Attach multiple files to the email.

## Requirements

- Python 3.x
- `smtplib` and `email` modules (included in Python standard library)

## Installation

No additional installation is required as all necessary modules are included in Python's standard library.

## Usage

### Input Parameters

- `subject` (str): The subject of the email.
- `content` (str): The body content of the email.
- `files` (list): A list of file paths to attach to the email.
- `sending_info` (dict): A dictionary containing email sending information:
  - `from_address`: Sender's email address.
  - `from_gmail_password`: Sender's Google account application password.
  - `to_address`: List of recipient email addresses.

### Example

```python
sending_info = {
    'from_address': 'your_email@gmail.com',
    'from_gmail_password': 'your_application_password',
    'to_address': ['recipient1@example.com', 'recipient2@example.com']
}

subject = 'Test Email'
content = 'This is a test email with attachments.'
files = ['/path/to/file1.txt', '/path/to/file2.pdf']

EmailWithAttachments(subject, content, files, sending_info)
```

Replace `'your_email@gmail.com'` and `'your_application_password'` with your actual email address and application password, and update the recipients and file paths accordingly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This version provides a concise overview of the class, its features, usage instructions, and an example without including the full source code.# Gmail-Sender
