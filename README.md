## Exam Project - Django Bank App

For Mandatory Assignment 1 and 2, we have designed and developed a banking system in Django.

### These are the requirements for our system:

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
