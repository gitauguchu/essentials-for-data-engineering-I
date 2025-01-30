#Search
import re

text = "Python is awesome. Python is powerful"
pattern = r"Python"

match = re.search(pattern, text)

if match:
    print(f"Pattern found: {match.group()}")
    print(f"Starting position: {match.start()}")
    print(f"Ending position: {match.end()}")
else:
    print("Pattern not found")


#Pattern Matching
#Literal characters
text = "The quick brown fox jumps over the lazy dog"
pattern = r"quick"
"""The r before the string denotes a raw string which treats backslashes as literal characters"""

match = re.search(pattern, text)
if match:
    print(f"Found: {match.group()}")
else:
    print("Match not found")

#Character classes
text = "The quick brown fox jumps over the lazy dog"
pattern = r"[aeiou]"

matches = re.findall(pattern, text)
print(f"Vowels found: {matches}")

#Ranges
text = "The quick brown fox jumps over the lazy dog"
pattern = r"[a-m]"

matches = re.findall(pattern, text)
print(f"Match found: {matches}")

#Negation
#You can negate a character class to match any character not in the set
text = "The quick brown fox jumps over the lazy dog"
pattern = r"[^aeiou]"
#The caret has to appear before the first character in the character class

matches = re.findall(pattern, text)
print(f"Non-vowels found: {''.join(matches)}")

#Start and end anchors
text = "The quick brown fox"
pattern1 = r"^The"
pattern2 = r"^fox$"
"""^ Checks the beginning of the string and $ checks the end of the string"""

match1 = re.search(pattern1, text)
match2 = re.search(pattern2, text)

print(f"Starts with 'The': {bool(match1)}")
print(f"Ends with 'fox': {bool(match2)}")

#Wildcard
text = "The quick brown fox jumps over the lazy dog"
pattern = r"b..wn"
#The . serves as a powerful wildcard and represents any single character other than newline characters

match = re.search(pattern, text)
if match:
    print(f"Found: {match.group()}")
else:
    print("Not found")

#Word boundaries
text = "eat eaten eating"
pattern = r"\beat\b"
"""\b matches a word boundary, that is, beginning or end of a word"""

matches = re.findall(pattern, text)
print(f"Whole word 'eat' found {len(matches)} times")


#Special characters and metacharacters
#Escape character (\)
text = "What is your favorite color?"
pattern = r"What is your favorite color\?"
"""The \ is used to escape the metacharacter"""

match = re.search(pattern, text)
print(f"Exact match: {bool(match)}")

#Alternation(|)
text = "Do you prefer coffee or tea?"
pattern = r"coffee|tea"
"""| acts like an OR operator, matching either the expression before or after it"""

match = re.findall(pattern, text)
print(f"Beverages found: {match}")

#Quantifiers
text = "The quick brown fox jumps over the lazy dog"
patterns = [
    r"\w+", #Words (1 or more word characters)
    r"\d*", #Numbers (0 or more digits)
    r"colou?r", #Optional 'u' in color or colour
    r"\b\w{5}\b", #5 letter words
]

for i, pattern in enumerate(patterns, 1):
    matches = re.findall(pattern, text)
    print(f"{i}. Pattern '{pattern}': {matches}")

#Special character classes
text = "Hello123 World! 456"

pattern = [
    r"\d+", #One or more digits
    r"\D+", #One or more non digits
    r"\w+", #One or more word characters
    r"\W+", #One or more non-word characters
]

for i, pattern in enumerate(patterns, 1):
    matches = re.findall(pattern, text)
    print(f"{i}. Pattern '{pattern}': {matches}")

#Lookahead and lookbehind assertions
text = "I have $10 and €20"

patterns = [
    r"\d+(?=\s*dollars)", #Number followed by "dollars"
    r"(?<=\$)\d+", #Number preceeded by "$"
    r"\d+(?!\s*euros)", #Number not followed by euros
    r"(?<!\€)\d+", #Number not preceeded by "€"
]

for i, pattern in enumerate(patterns, 1):
    matches = re.findall(pattern, text)
    print(f"{i}. Pattern '{pattern}': {matches}")


#Grouping and capturing
#Basic grouping with parentheses()
text = "hahaha heeheehee"
pattern = r"(ha){3}" #Match 'ha' exactly three times

matches = re.findall(pattern, text)
print(f"Matches: {matches}")

#Capturing groups
text = "John Doe (john@example.com)"
pattern = r"(\w+)\s(\w+)\s\((\w+@\w+\.\w+)\)"

match = re.search(pattern, text)
if match:
    print(f"Full name: {match.group(1)} {match.group(2)}")
    print(f"Email: {match.group(3)}")

#Named groups
text = "John Doe (john@example.com)"
pattern = r"(?P<first_name>\w+)\s(?P<last_name>\w+)\s\((?P<email>\w+@\w+\.\w+)\)"

match = re.search(pattern, text)
if match:
    print(f"First name: {match.group('first_name')}")
    print(f"Last name: {match.group('last_name')}")
    print(f"Email: {match.group('email')}")

#Non-capturing groups
text = "The color is either red or blue"
pattern = r"(?:red|blue)"

matches = re.findall(pattern, text)
print(f"Colors found: {matches}")