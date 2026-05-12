import sqlite3
import re

# creates a database file for the contact manager and a table for the contact info
conn = sqlite3.connect('contact_manager.db', isolation_level=None)
conn.execute('''CREATE TABLE IF NOT EXISTS contacts (name TEXT NOT NULL, phone_number TEXT, 
email_address TEXT, home_or_work_address TEXT, birthday TEXT) STRICT''')

# prompts user to input new contacts + info until user decides to quit
def create_contact():
    while True:
        print('Input the name of your new contact (or hit enter to quit):')
        contact_name = input()
        if contact_name == '':
            break
        print('Input any contact information for this person (or hit enter to skip):')
        contact_info = input()
        # Six different phone number formats accepted
        # XXXXXXXXXX, (XXX)-XXX-XXXX, XXX-XXX-XXXX, XXX XXX XXXX, (XXX) XXX-XXXX, and (XXX) XXX XXXX
        phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}|\(\d{3}\)-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4}|\d{10}|\d{3} \d{3} \d{4}|\(\d{3}\) \d{3} \d{4}')
        # converts the list of phone numbers into type string to be inputted into database
        contact_phone_nums = ','.join(phone_num_pattern_obj.findall(contact_info))
        email_pattern_obj = re.compile(r'[a-zA-z0-9._-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+')
        # converts list of emails into type string to be inputted into database
        contact_emails = ','.join(email_pattern_obj.findall(contact_info))
        print("Input the contact's birthdate - must be in the form MM/DD/YYYY (or hit enter to skip):")
        birthday_input = input()
        birthdate_pattern_obj = re.compile(r'\d{2}/\d{2}/\d{4}')
        if birthdate_pattern_obj.search(birthday_input) != None:
            contact_birthday = birthdate_pattern_obj.search(birthday_input).group()
        else:
            contact_birthday = ''
        print("Input the contact's home or work address (or hit enter to skip):")
        contact_address = input()
        conn.execute('INSERT INTO contacts VALUES (?, ?, ?, ?, ?)', [contact_name, contact_phone_nums,
        contact_emails, contact_address, contact_birthday])

# displays the current full list of contacts
def display_contacts():
    rows = conn.execute('SELECT * FROM contacts ORDER BY name').fetchall()
    for name, phone_num, email, address, birthdate in rows:
        print(f'Contact name: {name}')
        print(f'Phone number(s): {phone_num}')
        print(f'Email address(es): {email}')
        print(f'Home/work address: {address}')
        print(f'Birthday: {birthdate}\n')

# searches for an individual contact and displays its info, search is prompted continuously until user quits
def search_contacts():
    while True:
        print('Input the name of the contact you would like to search for (or hit enter to quit):')
        contact_name = input()
        if contact_name == '':
            break
        contact_entry = conn.execute('SELECT * FROM contacts WHERE name = ?', [contact_name]).fetchall()
        if contact_entry == []:
            print('Contact not found!')
        for name, phone_num, email, address, birthdate in contact_entry:
            print(f'Contact name: {name}')
            print(f'Phone number(s): {phone_num}')
            print(f'Email address(es): {email}')
            print(f'Home/work address: {address}')
            print(f'Birthday: {birthdate}\n')

# prompts user to remove a contact until user decides to quit
def remove_contacts():
    while True:
        print('Input the name of the contact you would like to remove (or hit enter to quit)')
        contact_name = input()
        if contact_name == '':
            break
        conn.execute('DELETE FROM contacts WHERE name = ?', [contact_name])

# prompts user to update (replace) certain information for a contact until user decides to quit
def update_info_in_contacts():
    while True:
        print('Input the name of the contact you would like to update (or hit enter to quit):')
        contact_name = input()
        if contact_name == '':
            break
        print('Input the info you would like to update (enter the word: name, email, phone number, birthdate, or address)')
        update_choice = input()
        if 'name' in update_choice.lower():
            new_name = input('Enter new contact name: ')
            conn.execute('UPDATE contacts SET name = ? WHERE name = ?', [new_name, contact_name])
        elif 'email' in update_choice.lower():
            new_email = input('Enter new contact email: ')
            conn.execute('UPDATE contacts SET email_address = ? WHERE name = ?', [new_email, contact_name])
        elif 'phone' in update_choice.lower():
            new_phone_num = input('Enter new contact phone number: ')
            conn.execute('UPDATE contacts SET phone_number = ? WHERE name = ?', [new_phone_num, contact_name])
        elif 'birth' in update_choice.lower():
            new_birthday = input('Enter new contact birthday: ')
            conn.execute('UPDATE contacts SET birthday = ? WHERE name = ?', [new_birthday, contact_name])
        elif 'address' in update_choice.lower():
            new_home_or_work = input('Enter new home or work address for contact: ')
            conn.execute('UPDATE contacts SET home_or_work_address = ? WHERE name = ?', [new_home_or_work, contact_name])

# prompts user to remove certain info for a contact until user decides to quit
def remove_info_in_contacts():
    while True:
        print('Input the name of the contact for which you would like to remove info (or hit enter to quit):')
        contact_name = input()
        if contact_name == '':
            break
        print('Input the info you would like to remove (enter the word: phone number, email, address, or birthday):')
        remove_choice = input()
        if 'phone' in remove_choice.lower():
            conn.execute('UPDATE contacts SET phone_number = ? WHERE name = ?', ['', contact_name])
        if 'email' in remove_choice.lower():
            conn.execute('UPDATE contacts SET email_address = ? WHERE name = ?', ['', contact_name])
        if 'birth' in remove_choice.lower():
            conn.execute('UPDATE contacts SET birthday = ? WHERE name = ?', ['', contact_name])
        if 'address' in remove_choice.lower():
            conn.execute('UPDATE contacts SET home_or_work_address = ? WHERE name = ?', ['', contact_name])

# main loop - program instructions
while True:
    print('''Welcome to your contact manager!
    To add a contact - print "add contact"
    To remove a contact - print "remove contact"
    To search for a contact - print "search"
    To display the full contact list - print "display"
    To update contact info - print "update info"
    To remove contact info - print "remove info"
    To quit - simply press enter\n''')
    input_choice = input()
    if input_choice == '':
        break
    elif 'add' in input_choice:
        create_contact()
    elif 'remove c' in input_choice:
        remove_contacts()
    elif 'search' in input_choice:
        search_contacts()
    elif 'display' in input_choice:
        display_contacts()
    elif 'update' in input_choice:
        update_info_in_contacts()
    elif 'remove i' in input_choice:
        remove_info_in_contacts()