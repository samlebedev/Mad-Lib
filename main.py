def sign_up():
  while True:
    db = open("database.txt","r")
    us = str(input('Create Username: '))
    pw = str(input('Create Password: '))
    pw1 = str(input('Confirm Password:'))
  
    d = []
    f = []
    for i in db:
      a,b = i.split(", ")
      b = b.strip()
      d.append(a)
      f.append(b)
    data = dict(zip(d, f))

    if pw1 != pw:
      print("Error! Passwords must match!")

    else:
      if len(pw)<8:
        print('Error! Password must have at least 8 characters.')

      elif us in d:
        print('Username already exists')

      elif us == "":
        print("You must create a username!")
        
      else:
        db = open("database.txt", "a")
        db.write(us+", "+pw+"\n")
        print("Success!")
        db.close()
        break
      
  with open(us+".txt","x") as file:
    file.write(us+", "+pw+"\n")
    file.write()
    


def sign_in():
  e = True
  while e == True:
    us = str(input('Username: '))
    pw = str(input('Password: '))
  
    db = open("database.txt", "r") 


    if not len(us or pw)<1:
      d = []
      f = []
      for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
      data = dict(zip(d, f))
    
      try:
        if data[us]:
          try:
            if pw == data[us]:
              print("Login Success!")
              print("Hi, "+us)
              e = False
            
            else:
              print("Password or Username invalid!")
              print("Try again(y or n)?")
              ans = input()
            
              while True:
                if ans == 'y':
                  us = sign_in()
                  e = False
                  break
                
                elif ans == 'n':
                  us = ''
                  e = False
                  break
                  
                else:
                  print("Error! Invalid response!")
                  print("Try again(y or n)")
                  ans = input()
              
          except:
            print("Username or Password invalid!")
            print("Try again(y or n)?")
            ans = input()
          
            while True:
              if ans == 'y':
                us = sign_in()
                e = False
                break
              
              elif ans == 'n':
                us = ''
                e = False
                break
                
              else:
                print("Error! Invalid response!")
                print("Try again(y or n)")
                ans = input()

        else:
          print("Username or Password doesn't exist!")
          print("Would you like to create an account(y or n)?")
          ans = input()
          while True:
            if ans == 'y':
              sign_up()
              us = sign_in()
              e = False
              break
            
            elif ans == 'n':
              us = ''
              e = False
              break
            
            else:
              print("Error! Invalid response!")
              print("Would you like to create an account(y or n)?")
              ans = input()

      except:
        print("Username or Password doesn't exist!")
        print("Would you like to create an account(y or n?")
        ans = input()
        if ans == 'y':
          sign_up()
          us = sign_in()
          e = False
          break
        
        elif ans == 'n':
          us = ''
          e = False
          break

    else:
      print("Please enter a value!")

  #return profile
  return us
  
def save(us, story):
  print("Do you want to save your Mad Lib? Press 'y ' for yes and 'n' for no." )
  ans = input()
  if ans == 'y':
    with open(us+".txt","a") as file:
      file.write("-------------------------------------------\n")
      # file.write(name)
      # file.write('\n')
      file.write(story)
      file.write("\n")

def love():
  prompts = [
    "Person",
    "Adjective",
    "Adjective 2",
    "Adjective 3",
    "Bodypart",
    "Number",
    "Noun",
    "Bodypart 2",
    "Verb",
    "Person 2"
  ] 
  answers = {}
  
  for prompt in prompts:
      answer = input(prompt + ": ")
      while not answer:
          print("Invalid input, try again.")
          answer = input(prompt + ": ")
      answers[prompt] = answer
  
  
  
 
  story = str(f"Dear {answers['Person']}, You are so {answers['Adjective']} and I think you are so {answers['Adjective 2']} !  I want to kiss your {answers['Bodypart']}  {answers['Number']} times! You make my {answers['Noun']} burn with desire! When I first saw you, I just looked at you and {answers['Verb']} in love. Will you go out with me? P.S. Don't let your {answers['Bodypart 2']} stop you, they're just {answers['Adjective 3']}./n Yours forever, {answers['Person 2']} <3")
  return story
  
def scary():
  prompts = [
    "Verb",
    "Noun", 
    "Adjective",
    "Place",
    "Person",
  ]

  
  answers = {}
  
  for prompt in prompts:
      answer = input(prompt + ": ")
      while not answer:
          print("Invalid input, try again.")
          answer = input(prompt + ": ")
      answers[prompt] = answer
  
  #story= str(f"Late one night {answers[]} was walking in the laboratory. It was a very {answers[]} night. And the {answers[]} had to be absolutely perfect! Suddenly, lightning struck. A {answers[]} sound came from the {answers[]}. I quickly grabbed a {answers[]}. I was shaking becasue I was so scared. The door slammed closed, and it was pitch black. I tried run away but something grabbed me and I screamed. The creature had leathery hands and crazy hair. )
  #
  #return story

def christmas():
  prompts = [
     "Adjective",
     "Noun",
     "Place",
  
  ]


  answers = {}

  for prompt in prompts:
      answer = input(prompt + ": ")
      while not answer:
          print("Invalid input, try again.")
          answer = input(prompt + ": ")
      answers[prompt] = answer
  story = str (f" test {answers['Noun']}")
  return story 

def wattpad():
  prompts = [
    "Celebrity",
    "Pronoun (he, she, they)",
    "Pronoun #2 (him, her, them)",
    "Person(parent)",
    "Color #1",
    "Length",
    "Color #2",
    "Food",
    "Adjective #1",
    "Verb",
    "Adjective #2",
    "Adjective #3",
    "Adjective #4",
    "Adjective #5",
    "Adverb",
    "Body part #1",
    "Body part #2",
  ] 
  
  answers = {}
  
  for prompt in prompts:
      answer = input(prompt + ": ")
      while not answer:
          print("Invalid input, try again.")
          answer = input(prompt + ": ")
      answers[prompt] = answer
  
  story = str (f"It was a warm summer day. I wake up to the sound   of my {answers['Person(parent)']} making us breakfast. Before coming downstairs I go into the bathroom and check the mirror. My  {answers['Length']} {answers['Color #1']} hair is up in a {answers['Adjective #1']} bun. My {answers['Color #2']} eyes look puffy and tired. After brushing my teeth I go downstairs to find my {answers['Person(parent)']} sitting at the table with {answers['Food']} on their plate. I sit down and my {answers['Person(parent)']} asks 'How was work yesterday?' I respond 'It was {answers['Adjective #2']}' I realize I am late for work and rush out the door. I work at the local cafe, although its {answers['Adjective #3']} it has a cozy ambience. My boss spots me and yells 'Y/n! This is the second day youve been late this week.' As a start my shift I feel a strong gaze in my direction. I try not to make it obvious but occasionally I peek over to try and see who is looking my way. I try not to let it distaract me thoughout my morning. After a while, I no longer see the {answers['Adjective #4']} figure in my peripheral vision. Suddenly I feel a {answers['Adjective #5']} tap on my {answers['Body part #1']} and I turn around. I see {answers['Pronoun #2 (him, her, them)']} {answers['Verb']} at me. This suprised me. But I tried to keep it cool.{answers['Pronoun (he, she, they)']}  leaned forward and asked me {answers['Adverb']} 'Can I get some napkins, y/n? ' I was shocked and my face was turning red. 'How do you know my name?' I felt my heart beat in my {answers['Body part #2']} . I could not beleive {answers['Celeberty']} was right in front of me.")
  return story

def doctor_who():
  prompts=[
     "Adjective",
     "Noun",
    
  ]


  answers={}
  for prompt in prompts:
      answer = input(prompt + ": ")
      while not answer:
          print("Invalid input, try again.")
          answer = input(prompt + ": ")
      answers[prompt] = answer
    
  story = (f" {answers['Noun']} ")
  return story 

def read_user_madlibs(us):
   with open(us+".txt","r") as file:
    for story in file:
      print(story)
  

# def home():
#   print("1. Sign in\n2. Sign up\n3. Guest")
#   choose = int(input())
#   if choose == 1:
#     us = sign_in()
#   elif choose == 2:
#     sign_up()
#     us = sign_in()
#   return choose, us

  
print(" WELCOME TO MADLIBS")
#print("WELCOME TO YOUR PERSONALIZED WATTPAD")

print("1. Sign in\n2. Sign up\n3. Guest")
choose = int(input())
if choose == 1:
  us = sign_in()
  if us == '':
    choose = 3
elif choose == 2:
  us = sign_up()
  if us == '':
    choose = 3

if choose == 1 or choose == 2:
  print("Would you like to see your created Mad Libs(y or n)?")
  a = input()
  if a == "y":
    read_user_madlibs(us)
  if a == 'n':
    pass
    
print("Would you like to create your own Mad Lib now(y or n?")
ans = input()

if ans == 'y':
  while(True):
    print("Type the number of the theme you want!")
    print("1. Love Letter\n2. Scary\n3. Christmas\n4. Your own Wattpad\n5. Doctor Who\n")
    choice = int(input())
    if choice == 1:
      lib = love()
      print(lib)
      # print("Great Job! What's the name of your Mad Lib?")
      # title = input()
      # print("What a great name!")
      
      if choose == 1 or choose == 2:
        save(us, lib)
    
    if choice == 2:
      lib = scary()
      print(lib)
      if choose == 1 or choose ==2:
        save(us, lib)
    
    if choice == 3:
      lib = christmas()
      print(lib)
      if choose == 1 or choose == 2:
        save(us, lib)
    if choice ==  4:
      lib = wattpad()
      print(lib)
      if choose == 1 or choose == 2:
        save(us, lib)

    if choice == 5:
      lib = doctor_who()
      print(lib)
      if choose == 1 or choose == 2:
        save(us, lib)
    
    if choice == 6:
      pass

    print()
    print('Do you want to keep going(y or n)?')
    go = input()
    
    if go == 'n':
      print("Thanks for using S&S Mad Libs!")
      break
    
elif ans == "n":
  print("Ok! Thank you!")


