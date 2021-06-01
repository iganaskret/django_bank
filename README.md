## Exam Project - Django Bank App

For our 6th sem. exam we have designed and developed a banking system in Django.

### Requirements for starting the project:

- Docker
- Google Authenticator

### Project setup:

Clone this git repository in an empty directory

```bash
https://gitlab.com/ksawery_karczewski/todo.git
```

Create a virtual environment

```bash
python3 -m venv py-env/bank
```

activate it

```bash
source py-env/bank/bin/activate
```

install requirements

```bash
pip install -r requirements.txt
```

and run it

```bash
python manage.py runserver
```

### Multi-factor authentication
As a safety measure for our users, we implemented a two-factor authentication system. 

This feature works together with an authenticator app, therefore it is required to install:

Google Authenticator

After creating an account in the bank app, in order to set up the two-factor authenticator, visit (while logged in):

```bash
http://127.0.0.1:8000/account/two_factor/setup/
```

Scan the QR code using your Google Authenticator app, save the account and now every time you will log in, it will generate a code that will be required in the bank app. 

### External transfers

In order to make an external transfer, copy the bank into a separate folder and run the copy on port 0.0.0.0:8003.

```bash
python3 manage.py runserver 0.0.0.0:8003
```

### Additional new features for the bank

1. Notifier

As our first additional functionality we have build a notifier for bank employees to see newly added users.

For our channel layer in notifier we used Redis (for backing store).

Start a Redis server on port 6379:

```bash
docker run -p 6379:6379 -d redis:5
```

Run this command to make sure that the redis image is build. It should be listed as redis:5 image, running on port 0.0.0.0:6379

```bash
docker container ls
```

Open these links in seperate browser windows.

```bash
http://127.0.0.1:8000/notifier/
```

```bash
http://127.0.0.1:8000/account/sign_up/
```

Provide a new user credential and click Sign Up. The new user username should should appear in the notifier tab with the creation time.

2. PDF download

The second functionality allows logged in users to download a PDF with their account movements. In order to convert HTML to PDF, we have used html2pdf converter.

After the log in, click on the SEE MOVEMENTS button. To save you movements as PDF click on the SAVE AS PDF.

### Group members

- Iga Marianna Naskret
- Codrina--Elena Acsinte
- Ksawery Karczewski

### 10 requirements for our system:

1. A customer can have any number of bank accounts
2. For future multi-factor authentication, we must record the customer's telephone number
3. The bank ranks its customers into three groups: basic, silver, and gold - the system must keep track of this information
4. Customers ranked silver and gold can loan money from the bank
5. Customers can make payments on their loans
6. Customers can transfer money from their accounts if the account balance is sufficient
7. Customers can view their accounts, accounts movements, and accounts balance
8. Bank employees can view all customers and accounts
9. Bank employees can create new customers and accounts and change customer rank
10. Use Python 3.7 or newer, Django 3.0 or newer
