############################################################

print("-"*30+"\tPython Shortcut LOC execution started\t"+"-"*30)
print("Create a shortcut for runnning a python code\n\t-\tPress Shift+Ctrl+P\n\t-\tOpen keyboard shorcuts\n\t-\tType \"Run python file\"\n\t-\tDouble click Keybinding\n\t-\tProvide ctrl+R as new shortcut")
print("-"*30+"\tPython Shortcut LOC execution ended\t"+"-"*30)

#############################################################

print("\n"+"-"*30+"\tEscape character LOC execution started\t"+"-"*30)
print("""For human readability,split the print content using triple quotes
      -\tMessage-1
      -\tMessage-2
      """)
print("-"*30+"\tEscape character LOC execution ended\t"+"-"*30)

#############################################################

print("\n"+"-"*30 +" f-string sample print execution started"+ "-"*30)
mob = "+49 (176) 123-4567"
print(f"\nContact Baraa at {mob}\n")
print(f"2 + 3 = {2+3}\n")
print(f"{{Use double curls to print curly braces as part of string}}\n")
print("-"*30 +" f-string sample print execution ended"+ "-"*30+"\n")

####################################################################
print("="*100)
print("String Transformations")
print("="*100)

print("\n"+"-"*20+"Challenge using replace() str method LOC execution started"+"-"*20)

print("\nMobile Number before replacing special characters is", mob)
print("\nMobile number after replacing special characters using replace() method is " , mob.replace("+","00").replace(" ","").replace("(","").replace(")","").replace("-",""))
print("\n"+"-"*20+"Challenge using replace() str method LOC execution ended"+"-"*20)

###################################################################

# "+" operator to concatenate 2 or more string values

folder_name = "D:\\Python_Learning\\mypoc"
file_name = "sample_file.csv"
full_file_path = folder_name + file_name
print(f"\nFull file path is {full_file_path}\n")

# Use split() method to split the string value into 2 or more

timestamp = "2025-06-07 16:59"
print(timestamp.split(" "))

ls_timestamp = timestamp.split(" ")
date = ls_timestamp[0]

print(date)

ls_date = date.split("-")
year = ls_date[0]
month = ls_date[1]
day = ls_date[2]

print (f"Today is {day} of {month}, {year}")

# Indexing and slicing 

text = "Python"

# Extract first character
print(text[0]) #First index starts from 0
print(text[-6]) # Last index starts from -1

# Extract first character
print(text[5])
print(text[-1])

# Extract "h"
print(text[3])

# Extract Year
print(date[0:4])
print(date[:4]) #If starting position is 0, start index can be ignored.

# Extract Month
print(date[5:7])

# Extract Day
print(date[8:])

# Whitespace cleanup
txt1 = " Python"
print(txt1.lstrip())

txt2 = "  Python   "
print(txt2.strip())

txt3 = " Data Engineering "
print(txt3.strip()) #strips whitespaces only at the start and end of the string

txt4 = "###Data ## Engineering##"
print(txt4.strip("#")) #strips special characters only at the start and end of the string

# Usecase of detecting leading or trailing spaces in a text
print(len(txt1))
print(len(txt1.strip()))

nr_of_spaces = len(txt1) - len(txt1.strip())
is_clean = len(txt1) == len(txt1.strip())

print(f"No of spaces : {nr_of_spaces}")
print(f"Is my data clean : {is_clean}")

# Case Conversions
new = "PYTHON programming"
print(new.lower())
print(new.upper())

challenge = "968-Maria, ( D@t@ Engineer ) ;; 27y  "
spl = challenge.replace(";;",",").replace("(","").replace(")","").split(",")

name = spl[0]
role = spl[1]
age = spl[2]

name = name[4:].lower()
role = role.replace("@","a").strip().lower()
age = age.replace("y","").strip()

print(f"name : {name} | role : {role} | age : {age}")

# Search
phone = "+91-987-654321"
print(phone.startswith("+91"))

email = "priyanka@gmail.com"
print(email.endswith("gmail.com"))
print("@" in email)

file = "backup.csv"
print(file.endswith(".csv"))

print(phone[phone.find("-")+1:]) #Dynamic way of printing phone number excluding country code

# Validation
country = "USA"
print(country.isalpha()) #Validate whether country contains only alphabets
print(phone.isnumeric()) #Validate whether phone number contains only number value






