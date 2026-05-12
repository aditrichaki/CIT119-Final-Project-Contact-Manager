# CIT119-Final-Project-Contact-Manager

Description:
This program functions as a simple contact manager. Users can add contact entries with a name, multiple phone numbers and email addresses, a birthdate, and a home
or work address. Users can also update specific information for an already-existing contact, remove contacts, search for specific contacts, and display the full
contact list. 

Program instructions:
    To add a contact - print "add contact"
        The user will be prompted for a contact name (required), contact info such as a phone number or email address (can include multiple), a birthdate, and an
        address for location. All information besides the name are optional to input.
    To remove a contact - print "remove contact"
        The user will be prompted for a contact name, and the program will remove the associated contact entry with all its info.
    To search for a contact - print "search"
        The user will be prompted for a contact name. If no entry with that name exists, the user will be notified and asked to enter another name. If a named
        contact does exist, its details will be displayed.
    To display the full contact list - print "display"
        The full created contact list at that moment will be displayed. 
    To update contact info - print "update info"
        The user will be prompted for a contact name, the specific type of information to be updated (email, birthdate, etc.), and the new information. If an
        entry for the inputted name exists, the old information will be replaced with the new.
    To remove contact info - print "remove info"
        The user will be prompted for a contact name and the specific type of information to be removed (email, birthdate, etc.). If a contact with that name
        exists, the specific information will be deleted, although the column will remain in the database.
    To quit - simply press enter

Reflection:
While writing this program, I learned a lot about being careful with syntax due to the usage of regular expressions to match phone numbers and email addresses.
It was very easy for one small missed backslash or parentheses to fully mess up the functionality of the program, and it was tricky to write the program to pick
up email addresses and phone numbers without them getting mangled together due to the fact that the user could enter them together on the same line. The usage of
a database with strict types for columns meant that I had to be mindful about what type I was actually inputting into a column. Some type conversions from list to
string using .join() was needed in order to enter information extracted by regex into the database table, and it was a solution that took a long time for me to figure out. Overall, a lot of debugging was needed for this program to function due to the large room for syntax errors. If I were to expand this program further, I would add more specialized functions such as "starring" contacts and forming groups of contacts, which I would probably do by creating a new table for the groups which would reference the contacts in the 'contacts' table. 
