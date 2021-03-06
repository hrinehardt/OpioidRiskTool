genderAnswer = None
famHistAnswer = None
personHistAnswer = None
ageAnswer = None
sxlAbuseAnswer = None
psychDxAnswer = None


def gender():
  print("Please enter your gender. ")
  choice = raw_input().lower()

  male = set(['male', 'm', 'man'])
  female = set(['female', 'f', 'woman'])

  if choice in male or female:
    genderAnswer = 'yes'
  elif choice in male or female:
    genderAnswer = 'no'
  else:
    print("Please respond with 'male' or 'female'")
    gender()


def famHist():
  print("Do you have a family history of substance abuse? ")
  choice = raw_input().lower()

  yes = set(['yes','y', 'ye', ''])
  no = set(['no','n', 'nope'])

  if choice in yes:
    famHistAnswer = 'yes'
  elif choice in no:
    famHistAnswer = 'no'
  else:
    print("Please respond with 'yes' or 'no'")
    famHist()


def personHist():
  print("Do you have a personal history of substance abuse? ")
  choice = raw_input().lower()

  yes = set(['yes','y', 'ye', ''])
  no = set(['no','n', 'nope'])

  if choice in yes:
    personHistAnswer = 'yes'
  elif choice in no:
    personHistAnswer = 'no'
  else:
    print("Please respond with 'yes' or 'no'")
    personHist()


def age():
  print("Are you between 16-45 years old? ")
  choice = raw_input().lower()

  yes = set(['yes','y', 'ye', ''])
  no = set(['no','n', 'nope'])

  if choice in yes:
    ageAnswer = 'yes'
  elif choice in no:
    ageAnswer = 'no'
  else:
    print("Please respond with 'yes' or 'no'")
    age()


def sxlAbuse():
  print("Do you have a history of preadolescent sexual abuse? ")
  choice = raw_input().lower()

  yes = set(['yes','y', 'ye', ''])
  no = set(['no','n', 'nope'])

  if choice in yes:
    sxlAbuseAnswer = 'yes'
  elif choice in no:
    sxlAbuseAnswer = 'no'
  else:
    print("Please respond with 'yes' or 'no'")
    sxlAbuse()


def psychDx():
  print("Do you have a diagnosed psychological disease? ")
  choice = raw_input().lower()

  yes = set(['yes','y', 'ye', ''])
  no = set(['no','n', 'nope'])

  if choice in yes:
    pyschDxAnswer = 'yes'
  elif choice in no:
    psychDxAnswer = 'no'
  else:
    print("Please respond with 'yes' or 'no'")
    psychDx()

def askYesNo(question, responseVariable):
  print(question)
  choice = raw_input().lower()

  yes = set(['yes','y', 'ye', ''])
  no = set(['no','n', 'nope'])

  if choice in yes:
    responseVariable = 'yes'
  elif choice in no:
    responseVariable = 'no'
  else:
    print("Please respond with 'yes' or 'no'")
    askYesNo(question, responseVariable)



gender()
famHist()
personHist()
age()
sxlAbuse()
psychDx()


print(genderAnswer)
print(famHistAnswer)
print(personHistAnswer)
print(ageAnswer)
print(sxlAbuseAnswer)
print(psychDxAnswer)


# Adds Risk scale
print "Risk:\n 0-3 - low \n 4-7 - moderate \n >= 8 - high"
