'''Given:

raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "
Clean the values and display:

Name: Sagar Thapa
City: Kathmandu
Age: 27
Email: sagar@mail.com
Status: Adult
“Use a ternary expression for the adult status.”'''


raw_name = " sAgar THAPA "
raw_city = " kATHMANDU "
raw_age = " 27 "
raw_email = " SAGAR@MAIL.COM "


name = raw_age.strip().title()
city = raw_city.strip().title()
age = int(raw_age.strip())
email = raw_email.strip().lower()

status = "Adult" if age>=18 else "Miner"

# Display
print("Name:", name)
print("City:", city)
print("Age:0", age)
print("Email:", email)
print("Status:", status)
