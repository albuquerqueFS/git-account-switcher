import typer
import writter
import account_manager

app = typer.Typer()

@app.command()
def list():
    accounts = account_manager.get_accounts()

    if accounts:
        for account in accounts:
            print(f"{account['account_name']} - {account['name']} - {account['email']}")
    else:
        print('You don\'t have any accounts yet')

@app.command()
def switch(account_name: str):
    account_exists = account_manager.get_account(account_name)

    if account_exists:
        print(f'Switching to {account_name}')
        writter.switch_to_git_account(account_exists['name'], account_exists['email'])

@app.command()
def add():
    accounts = account_manager.get_accounts()

    if accounts is False:
        print('Welcome to git witch!')

    print('\nGive a name to this account (work/personal):')
    account_name = input()

    print('\nThe account email')
    email = input()

    print('\nThe account username')
    username = input()

    print('Generating new configuration as follows')
    print("""
        [user]
            emai = {0}
            name = {1}
            email = {2}
    """.format(email, username, email))

    account_manager.add_account(account_name, username, email)

@app.command()
def delete(account_name: str):
    account_exists = account_manager.get_account(account_name)

    if account_exists:
        account_manager.delete_account(account_name)

if __name__ == "__main__":
    app()
