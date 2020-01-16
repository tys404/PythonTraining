# name = input("Name: ")
# surname = input("Surname: ")
# birthDate = input("Date of birth (dd-mm-rrrr): ")
# city = input("City: ")

name = "Richard"
surname = "Feynman"
birthDate = "11-05-1918"
city = "Los Angeles"

nameAndSurnameLen = len(f"{name} {surname}")
birthDateLen = len(f"{birthDate}")
cityLen = len(f"{city}")

maxLen = max([nameAndSurnameLen, birthDateLen, cityLen])
sufixLen = 20
lineLen = sufixLen + maxLen

nameAndSurnameSpace = ""
for _ in range(maxLen - nameAndSurnameLen):
    nameAndSurnameSpace += " "

birthDateSpace = ""
for _ in range(maxLen - birthDateLen):
    birthDateSpace += " "

citySpace = ""
for _ in range(maxLen - cityLen):
    citySpace += " "

line = ""
for _ in range(lineLen):
    line += "-"

initials = f"{name[0]}.{surname[0]}."

print(f"      {line}")
print(f"     | Name and surname: {name} {surname} {nameAndSurnameSpace}|")
print(f"{initials} | Birth date:       {birthDate} {birthDateSpace}|")
print(f"     | City:             {city} {citySpace}|")
print(f"      {line}")


