import os

base_path = os.path.expanduser('~')
gitconfig_path = base_path + '/.gitconfig'

def process_gitconfig(name, email):
    print('Reading gitconfig')
    file = open(gitconfig_path, 'r')
    lines = file.readlines()

    original_lines = []
    mutated_lines = []

    print('Processing gitconfig...')
    for line in lines:
        if '[user]' in line:
            original_lines = lines[0:lines.index(line)]
            mutated_lines = lines[lines.index(line):lines.index(line)+4]
            for credential in mutated_lines:
                if 'name' in credential:
                    splitted = credential.split(' = ')
                    splitted[1] = name
                    mutated_lines[mutated_lines.index(credential)] = splitted[0] + ' = ' + splitted[1] + '\n'
                if 'emai' in credential:
                    splitted = credential.split(' = ')
                    splitted[1] = email
                    mutated_lines[mutated_lines.index(credential)] = splitted[0] + ' = ' + splitted[1] + '\n'

    return { "original_lines": original_lines, "mutated_lines": mutated_lines}

def generate(original_lines, mutated_lines):
    print('Generating new gitconfig')
    new_text = ''

    for x in original_lines:
        new_text += x
    for x in mutated_lines:
        new_text += x

    text_file = open(gitconfig_path, "w")
    text_file.write(new_text)
    text_file.close()

def switch_to_git_account(name, email):
    processed_data = process_gitconfig(name, email)
    generate(processed_data["original_lines"], processed_data["mutated_lines"])
