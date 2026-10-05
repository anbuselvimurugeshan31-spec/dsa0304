import re

# Sample text
text = "My email is student123@gmail.com and my phone number is 9876543210."

# 1. Search for an email address
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
email_match = re.search(email_pattern, text)

if email_match:
    print("Email found:", email_match.group())
else:
    print("Email not found")

# 2. Search for a 10-digit phone number
phone_pattern = r'\b\d{10}\b'
phone_match = re.search(phone_pattern, text)

if phone_match:
    print("Phone number found:", phone_match.group())
else:
    print("Phone number not found")

# 3. Match a pattern at the beginning of a string
start_text = "Python is a powerful language"
match_result = re.match(r'Python', start_text)

if match_result:
    print("Matched at the beginning:", match_result.group())
else:
    print("No match at the beginning")

# 4. Find all words starting with 'p' or 'P'
sentence = "Python programming provides powerful packages"
words = re.findall(r'\b[Pp]\w+', sentence)

print("Words starting with P/p:", words)
