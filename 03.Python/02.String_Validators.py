# Input Format

# A single line containing a string .



# Output Format

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
# In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
# In the third line, print True if  has any digits. Otherwise, print False. 
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.


S = "qA2"
# True
# True
# True
# True
# True

has_any_numberic_character = False
has_any_alphabetical_character = False
has_any_digit_character = False
has_any_lowercase_character = False
has_any_uppercase_character = False


for item in S:
    str_item = str(item)
    if str_item.isalnum() and has_any_numberic_character == False:
        has_any_numberic_character = True
    if str_item.isalpha() and has_any_alphabetical_character == False:
        has_any_alphabetical_character = True
    if str_item.isdigit() and has_any_digit_character == False :
        has_any_digit_character = True
    if str_item.islower() and has_any_lowercase_character == False:
        has_any_lowercase_character = True
    if str_item.isupper() and has_any_uppercase_character == False:
        has_any_uppercase_character = True
print(has_any_numberic_character)
print(has_any_alphabetical_character)
print(has_any_digit_character)
print(has_any_lowercase_character)
print(has_any_uppercase_character)
    

       
