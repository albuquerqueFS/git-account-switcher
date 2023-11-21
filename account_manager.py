import json

file_path = './accounts.json'

def add_account(account_name: str, name: str, email: str):
    account = {
        "account_name": account_name,
        "name": name,
        "email": email
    }
    accounts = []

    try:
        with open(file_path, 'r') as file:
            accounts = json.load(file)
    except FileNotFoundError:
        print("Saving new account")

    accounts.append(account)
    json_object = json.dumps(accounts, indent=4)
    with open('accounts.json', 'w') as outfile:
        outfile.write(json_object)

def get_account(account_name: str):
    try:
        with open(file_path, 'r') as file:
            accounts = json.load(file)
            for account in accounts:
                if account['account_name'] == account_name:
                    print('Account found')
                    return account
            print('Account not found')
            return False
    except FileNotFoundError:
        print('You don\'t have any accounts yet')
        return False

def get_accounts():
    try:
        with open(file_path, 'r') as file:
            accounts = json.load(file)

            if len(accounts) == 0:
                return False

            return accounts
    except FileNotFoundError:
        return False

def delete_account(account_name: str):
    accounts = []

    try:
        with open(file_path, 'r') as file:
            accounts = json.load(file)
    except FileNotFoundError:
        print("No accounts found")

    for account in accounts:
        if account['account_name'] == account_name:
            accounts.remove(account)
            print('Account deleted')
            break

    json_object = json.dumps(accounts, indent=4)
    with open('accounts.json', 'w') as outfile:
        outfile.write(json_object)