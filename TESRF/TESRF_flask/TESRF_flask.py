from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

#Home
@app.route('/', methods = ['GET', 'POST'])
def home():
  if request.method == 'POST':
    return redirect(url_for('province'))
  return '''
    <h1>Welcome to the Elder Scrolls Character Creation Quiz!</h1>
    <br>
    <p>Welcome to the Elder Scrolls Character Creation Quiz! This project is my first venture into Python programming, and it features a recreated quiz inspired by the iconic 2003 Morrowind game developed by Bethesda. In this quiz, you'll embark on a journey to create your own character by answering a series of questions that will determine your race, birth sign, and class in the world of Tamriel. Your choices will influence your character's strengths in combat, magic, and stealth. Let the adventure begin!</p>
    <form method = "post">
      <input type = "submit" value = "Start Quiz">
    </form>
'''

@app.route('/quiz', methods = ['GET', 'POST'])
def province(): #province and rate
  if request.method == 'POST':
    choice = request.form['province']
    if choice == "1":
      player_race = "a Nord"
      player_province = "Skyrim"
    elif choice == "2":
      player_race = "a Dark Elf, also known as Dunmer"
      player_province = "Morrowind"
    elif choice == "3":
      player_race = "an Imperial"
      player_province = "Cyrodil"
    elif choice == "4":
      player_race = "a Breton"
      player_province = "High Rock"
    elif choice == "5":
      player_race = "a Redguard"
      player_province = "Hammerfell"
    elif choice == "6":
      player_race = "an Argonian"
      player_province = "Black Marsh"
    elif choice == "7":
      player_race = "a Wood Elf, also known as Bosmer"
      player_province = "Valenwood"
    elif choice == "8":
      player_race = "a High Elf, also known as Altmer"
      player_province = "Summerset Isle"
    elif choice == "9":
      player_race = "a Khajiit"
      player_province = "Elsweyr"
    elif choice == "10":
      player_race = "an Orc"
      player_province = "Orsinium"
    else:
      return "Invalid choice. Please try again."
    
    session['player_race'] = player_race
    session['player_province'] = player_province


    return redirect(url_for('birth_sign'))

  return '''
    <form method = "POST">
    <h2>From where in Tamriel do you hail?</h2>
      <label for = "province">Choose your province:</label>
      <select name = "province" id = "province">
        <option value = "0">Select a province</option>
        <option value = "1">Skyrim</option>
        <option value = "2">Morrowind</option>
        <option value = "3">Cyrodil</option>
        <option value = "4">High Rock</option>
        <option value = "5">Hammerfell</option>
        <option value = "6">Black Marsh</option>
        <option value = "7">Valenwood</option>
        <option value = "8">Summerset Isle</option>
        <option value = "9">Elsweyr</option>
        <option value = "10">Orsinium</option>
      </select>
      <input type = "submit" value = "Submit"/>
    </form>
  '''

#BirthSign
@app.route('/birth_sign', methods = ['GET', 'POST'])
def birth_sign():
  if request.method == 'POST':
    #Get day and month
    day = int(request.form['day'])
    month = int(request.form['month'])
    zodiac_sign = get_zodiac_sign(day, month)
    birth_sign = get_birth_sign(zodiac_sign)

    if zodiac_sign == "Invalid Date":
      return "Invalid date entered. Please try again."
    
    birth_sign = get_birth_sign(zodiac_sign)
    #return f"Your zodiac sign is {zodiac_sign} and your Tamriel birth sign is {birth_sign}."

    session['birth_sign'] = birth_sign

    return redirect(url_for('question_1'))

#If GET request, display the form to enter the birthday
  return '''
    <form method = "POST">
      <p>This is used to determine your birth sign in Tamriel</p>
      <label for = "month">Enter your birth month:</label>
      <input type = "number" name = "month" min = "1" max = "12" required>

      <label for = "day">Enter your birth day:</label>
      <input type = "number" name = "day" min = "1" max = "31" required>

      <input type = "submit" value = "Submit">
    </form>
    '''
    
def get_zodiac_sign(day, month):
  if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    return "Aries"
  elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    return "Taurus"
  elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    return "Gemini"
  elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    return "Cancer"
  elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    return "Leo"
  elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    return "Virgo"
  elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    return "Libra"
  elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    return "Scorpio"
  elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    return "Sagittarius"
  elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    return "Capricorn"
  elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    return "Aquarius"
  elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    return "Pisces"
  else:
    return "Invalid Date"

def get_birth_sign(zodiac_sign):
  if zodiac_sign == "Capricorn":
    return "Ritual"
  elif zodiac_sign == "Aquarius":
    return "Lover"
  elif zodiac_sign == "Pisces":
    return "Lord"
  elif zodiac_sign == "Aries":
    return "Mage"
  elif zodiac_sign == "Taurus":
    return "Shadow"
  elif zodiac_sign == "Gemini":
    return "Steed"
  elif zodiac_sign == "Cancer":
    return "Apprentice"
  elif zodiac_sign == "Leo":
    return "Warrior"
  elif zodiac_sign == "Virgo":
    return "Lady"
  elif zodiac_sign == "Libra":
    return "Tower"
  elif zodiac_sign == "Scorpio":
    return "Atronach"
  elif zodiac_sign == "Sagittarius":
    return "Thief"
  else:
    return "Invalid"

#Morrowind Questionnaire Section

#Question 1
@app.route('/question_1', methods = ['GET', 'POST'])
def question_1():
  if 'combat_points' not in session:
    session['combat_points'] = 0
  if 'magic_points' not in session:
    session['magic_points'] = 0
  if 'stealth_points' not in session:
    session['stealth_points'] = 0

  if request.method == 'POST':
    answer = request.form.get('answer')

  #Get the player's answer for question 1
    if answer == "1":
      session['combat_points'] += 1
    elif answer == "2":
      session['magic_points'] += 1
    elif answer == "3":
      session['stealth_points'] += 1
    else:
      return "Please select a valid option."
    
    return redirect(url_for('question_2'))

  return '''
    <form method = "POST">
      <h2>Question 1</h2>
      <p>On a clear day you chance upon a strange animal, its leg trapped in a hunter's clawsnare. Judging from the bleeding it will not survive long.</p>
      <p>What do you do?</p>
      <input type = "radio" name = "answer" value = "1">Draw your dagger, mercifully ending its life with a single thrust.<br>
      <input type = "radio" name = "answer" value = "2">Use herbs from your pack to put it to sleep.<br>
      <input type = "radio" name = "answer" value = "3">Do not interfere in the natural evolution of events, but rather take the opportunity to learn more about a strange animal you have never seen before.<br>
      <br>
      <input type = "submit" value = "Next Question">
    </form>
'''
  
#Question 2
@app.route('/question_2', methods = ['GET', 'POST'])
def question_2():
  if 'combat_points' not in session:
    session['combat_points'] = 0
  if 'magic_points' not in session:
    session['magic_points'] = 0
  if 'stealth_points' not in session:
    session['stealth_points'] = 0

  if request.method == 'POST':
    answer = request.form.get('answer')

    if answer == "1":
      session['combat_points'] += 1
    elif answer == "2":
      session['magic_points'] += 1
    elif answer == "3":
      session['stealth_points'] += 1
    else:
      return "Please select a valid option."
    
    return redirect(url_for('question_3'))

  return '''
    <form method = "POST">
      <h2>Question 2</h2>
      <p>One Summer afternoon your father gives you a choice of chores.</p>
      <p>What do you do?</p>
      <input type = "radio" name = "answer" value = "1">Work in the forge with him casting iron for a new plow.<br>
      <input type = "radio" name = "answer" value = "2">Gather herbs for your mother who is preparing dinner.<br>
      <input type = "radio" name = "answer" value = "3">Go catch fish at the stream using a net and line.<br>
      <br>
      <input type = "submit" value = "Next Question">
    </form>
'''

#Question 3
@app.route('/question_3', methods = ['GET', 'POST'])
def question_3():
  if 'combat_points' not in session:
    session['combat_points'] = 0
  if 'magic_points' not in session:
    session['magic_points'] = 0
  if 'stealth_points' not in session:
    session['stealth_points'] = 0

  if request.method == 'POST':
    answer = request.form.get('answer')

    if answer == "1":
      session['combat_points'] += 1
    elif answer == "2":
      session['magic_points'] += 1
    elif answer == "3":
      session['stealth_points'] += 1
    else:
      return "Please select a valid option."
    
    return redirect(url_for('question_4'))
  
  return '''
    <form method = "POST">
      <h2>Question 3</h2>
      <p>Your cousin has given you a very embarrassing nickname and, even worse, likes to call you it in front of your friends. You asked him to stop, but he finds it very amusing to watch you blush.</p>
      <p>What do you do?</p>
      <input type = "radio" name = "answer" value = "1">Beat up your cousin, then tell him that if he ever calls you that nickname again, you will bloody him worse than this time.<br>
      <input type = "radio" name = "answer" value = "2">Make up a story that makes your nickname a badge of honor instead of something humiliating.<br>
      <input type = "radio" name = "answer" value = "3">Make up an even more embarrassing nickname for him and use it constantly until he learns his lesson.<br>
      <br>
      <input type = "submit" value = "Next Question">
    </form>
'''

#Question 4
@app.route('/question_4', methods = ['GET', 'POST'])
def question_4():
  if 'combat_points' not in session:
    session['combat_points'] = 0
  if 'magic_points' not in session:
    session['magic_points'] = 0
  if 'stealth_points' not in session:
    session['stealth_points'] = 0
  
  if request.method == 'POST':
    answer = request.form.get('answer')

    if answer == "1":
      session['combat_points'] += 1
    elif answer == "2":
      session['magic_points'] += 1
    elif answer == "3":
      session['stealth_points'] += 1
    else:
      return "Please select a valid option."
    
    return redirect(url_for('question_5'))
  
  return '''
    <form method = "POST">
      <h2>Question 4</h2>
      <p>There is a lot of heated discussion at the local tavern over a group of people called 'Telepaths'. They have been hired by certain City-State kings. Rumor has it these Telepaths read a person's mind and tell their lord whether a follower is telling the truth or not.</p>
      <p>What is your opinion?</p>
      <input type = "radio" name = "answer" value = "1">This is a terrible practice. A person's thoughts are his own and no one, not even a king, has the right to make such an invasion into another human's mind.<br>
      <input type = "radio" name = "answer" value = "2">Loyal followers to the king have nothing to fear from a Telepath. It is important to have a method of finding assassins and spies before it is too late.<br>
      <input type = "radio" name = "answer" value = "3">In these times, it is a necessary evil. Although you do not necessarily like the idea, a Telepath could have certain advantages during a time of war or in finding someone innocent of a crime.<br>
      <br>
      <input type = "submit" value = "Next Question">
    </form>
'''

#Question 5
@app.route('/question_5', methods = ['GET', 'POST'])
def question_5():
  if 'combat_points' not in session:
    session['combat_points'] = 0
  if 'magic_points' not in session:
    session['magic_points'] = 0
  if 'stealth_points' not in session:
    session['stealth_points'] = 0
  
  if request.method == 'POST':
    answer = request.form.get('answer')

    if answer == "1":
      session['combat_points'] += 1
    elif answer == "2":
      session['magic_points'] += 1
    elif answer == "3":
      session['stealth_points'] += 1
    else:
      return "Please select a valid option."
  
    return redirect(url_for('question_6'))

  return """
    <form method = "POST">
    <h2>Question 5</h2>
    <p>Your mother sends you to the market with a list of goods to buy. After you finish you find that by mistake a shopkeeper has given you too much money back in exchange for one of the items.</p>
    <p>What do you do?</p>
    <input type = "radio" name = "answer" value = "1">Return to the store and give the shopkeeper his hard-earned money, explaining to him the mistake.<br>
    <input type = "radio" name = "answer" value = "2">Decide to put the extra money to good use and purchase items that would help your family.<br>
    <input type = "radio" name = "answer" value = "3">Pocket the extra money, knowing that shopkeepers in general tend to overcharge customers anyway.<br>
    <br>
    <input type = "submit" value = "Next Question">
  </form>
"""

#Question 6
@app.route('/question_6', methods = ['GET', 'POST'])
def question_6():
  if 'combat_points' not in session:
    session['combat_points'] = 0
  if 'magic_points' not in session:
    session['magic_points'] = 0
  if 'stealth_points' not in session:
    session['stealth_points'] = 0
  
  if request.method == 'POST':
    answer = request.form.get('answer')

    if answer == "1":
      session['combat_points'] += 1
    elif answer == "2":
      session['magic_points'] += 1
    elif answer == "3":
      session['stealth_points'] += 1
    else:
      return "Please select a valid option."
    
    return redirect(url_for('question_7'))
  
  return """
    <form method = "POST">
    <h2>Question 6</h2>
    <p>While in the market place you witness a thief cut a purse from a noble. Even as he does so, the noble notices and calls for the city guards. In his haste to get away, the thief drops the purse near you. Surprisingly no one seems to notice the bag of coins at your feet.</p>
    <p>What do you do?</p>
    <input type = "radio" name = "answer" value = "1">Pick up the bag and signal to the guard, knowing that the only honorable thing to do is return the money to its rightful owner.<br>
    <input type = "radio" name = "answer" value = "2">Leave the bag there, knowing that it is better not to get involved.<br>
    <input type = "radio" name = "answer" value = "3">Pick up the bag and pocket it, knowing that the extra windfall will help your family in times of trouble.<br>
    <br>
    <input type = "submit" value = "Next Question">
  </form>
  """

#Question 7
@app.route('/question_7', methods = ['GET', 'POST'])
def question_7():
  if 'combat_points' not in session:
    session['combat_points'] = 0
  if 'magic_points' not in session:
    session['magic_points'] = 0
  if 'stealth_points' not in session:
    session['stealth_points'] = 0

  if request.method == 'POST':
    answer = request.form.get('answer')

    if answer == "1":
      session['combat_points'] += 1
    elif answer == "2":
      session['magic_points'] += 1
    elif answer == "3":
      session['stealth_points'] += 1
    else:
      return "Please select a valid option."
  
    return redirect(url_for('question_8'))

  return """
  <form method = "POST">
  <h2>Question 7</h2>
  <p>Your father sends you on a task which you loathe, cleaning the stables. On the way there, pitchfork in hand, you run into your friend from the homestead near your own. He offers to do it for you, in return for a future favor of his choosing.</p>
  <p>What do you do?</p>
  <input type = "radio" name = "answer" value = "1">Decline his offer, knowing that your father expects you to do the work, and it is better not to be in debt.<br>
  <input type = "radio" name = "answer" value = "2">Ask him to help you, knowing that two people can do the job faster than one, and agree to help him with one task of his choosing in the future.<br>
  <input type = "radio" name = "answer" value = "3">Accept his offer, reasoning that as long as the stables are cleaned, it matters not who does the cleaning.<br>
  <br>
  <input type = "submit" value = "Next Question">
</form>
"""

#Question 8
@app.route('/question_8', methods = ['GET', 'POST'])
def question_8():
  if 'combat_points' not in session:
    session['combat_points'] = 0
  if 'magic_points' not in session:
    session['magic_points'] = 0
  if 'stealth_points' not in session:
    session['stealth_points'] = 0

  if request.method == 'POST':
    answer = request.form.get('answer')

    if answer == "1":
      session['combat_points'] += 1
    elif answer == "2":
      session['magic_points'] += 1
    elif answer == "3":
      session['stealth_points'] += 1
    else:
      return "Please select a valid option."
  
    return redirect(url_for('question_9'))

  return """
  <form method = "POST">
  <h2>Question 8</h2>
  <p>Your mother asks you to help fix the stove. While you are working, a very hot pipe slips its mooring and falls towards her.</p>
  <p>What do you do?</p>
  <input type = "radio" name = "answer" value = "1">Position yourself between the pipe and your mother.<br>
  <input type = "radio" name = "answer" value = "2">Grab the hot pipe and try to push it away.<br>
  <input type = "radio" name = "answer" value = "3">Push your mother out of the way.<br>
  <br>
  <input type = "submit" value = "Next Question">
</form>
"""

#Question 9
@app.route('/question_9', methods = ['GET', 'POST'])
def question_9():
  if 'combat_points' not in session:
    session['combat_points'] = 0
  if 'magic_points' not in session:
    session['magic_points'] = 0
  if 'stealth_points' not in session:
    session['stealth_points'] = 0

  if request.method == 'POST':
    answer = request.form.get('answer')

    if answer == "1":
      session['combat_points'] += 1
    elif answer == "2":
      session['magic_points'] += 1
    elif answer == "3":
      session['stealth_points'] += 1
    else:
      return "Please select a valid option."
  
    return redirect(url_for('question_10'))

  return """
  <form method = "POST">
  <h2>Question 9</h2>
  <p>While in town the baker gives you a sweetroll. Delighted, you take it into an alley to enjoy only to be intercepted by a gang of three other kids your age. The leader demands the sweetroll, or else he and his friends will beat you and take it.</p>
  <p>What do you do?</p>
  <input type = "radio" name = "answer" value = "1">Drop the sweetroll and step on it, then get ready for the fight.<br>
  <input type = "radio" name = "answer" value = "2">Give him the sweetroll now without argument, knowing that later this afternoon you will have all your friends with you and can come and take whatever he owes you.<br>
  <input type = "radio" name = "answer" value = "3">Act like you're going to give him the sweetroll, but at the last minute throw it in the air, hoping that they'll pay attention to it long enough for you to get a shot in on the leader.<br>
  <br>
  <input type = "submit" value = "Next Question">
</form>
"""

#Question 10
@app.route('/question_10', methods = ['GET', 'POST'])
def question_10():
  if 'combat_points' not in session:
    session['combat_points'] = 0
  if 'magic_points' not in session:
    session['magic_points'] = 0
  if 'stealth_points' not in session:
    session['stealth_points'] = 0

  if request.method == 'POST':
    answer = request.form.get('answer')

    if answer == "1":
      session['combat_points'] += 1
    elif answer == "2":
      session['magic_points'] += 1
    elif answer == "3":
      session['stealth_points'] += 1
    else:
      return "Please select a valid option."
  
    return redirect(url_for('result'))

  return """
  <form method = "POST">
  <h2>Question 10</h2>
  <p>Entering town you find that you are witness to a very well-dressed man running from a crowd. He screams to you for help. The crowd behind him seem very angry.</p>
  <p>What do you do?</p>
  <input type = "radio" name = "answer" value = "1">Rush to the town's aid immediately, despite your lack of knowledge of the circumstances.<br>
  <input type = "radio" name = "answer" value = "2">Stand aside and allow the man and the mob to pass, realizing it is probably best not to get involved.<br>
  <input type = "radio" name = "answer" value = "3">Rush to the man's aid immediately, despite your lack of knowledge of the circumstances.<br>
  <br>
  <input type = "submit" value = "Next Question">
</form>
"""

#Print Final Output


@app.route('/result', methods = ['GET', 'POST'])
def result():
  player_race = session.get('player_race')
  player_province = session.get('player_province')
  birth_sign = session.get('birth_sign')
  combat_points = session.get('combat_points')
  magic_points = session.get('magic_points', 0)
  stealth_points = session.get('stealth_points', 0)
  player_class = session.get('player_class', 0)

  if combat_points >= 7:
    player_class = "Warrior"
  elif magic_points >= 7:
    player_class = "Mage"
  elif stealth_points >= 7:
    player_class = "Thief"
  elif combat_points == 6 and magic_points == 4:
    player_class = "Knight"
  elif combat_points == 6 and magic_points == 3 and stealth_points == 1:
    player_class = "Barbarian"
  elif combat_points == 6 and magic_points == 1 and stealth_points == 3:
    player_class = "Crusader"
  elif combat_points == 5 and magic_points == 4 and stealth_points == 1:
    player_class = "Archer" #adjusted for points from original quiz
  elif combat_points == 5 and magic_points == 2 and stealth_points == 3:
    player_class = "Scout"
  elif combat_points == 4 and 0 <= magic_points <= 6 and 0 <= stealth_points <= 6:
    player_class = "Rogue"
  elif combat_points == 4 and magic_points == 2 and stealth_points == 4:
    player_class = "Bard" #not originally on the quiz due to logic error
  elif combat_points == 1 and magic_points == 4 and stealth_points == 5:
    player_class = "Nightblade" #not originally on the quiz due to a logic error
  elif combat_points == 3 and magic_points == 6 and stealth_points == 1:
    player_class = "Healer"
  elif 2 <= combat_points <= 3 and 5 <= magic_points <= 6 and 2 <= stealth_points <= 5:
    player_class = "Witchhunter"
  elif 1 <= combat_points <= 3 and 4 <= magic_points <= 6 and 3 <= stealth_points <= 6:
    player_class = "Spellsword"
  elif combat_points == 3 and magic_points == 1 and stealth_points == 6:
    player_class = "Agent"
  elif combat_points == 2 and magic_points == 6 and stealth_points == 2:
    player_class = "Sorcerer"
  elif combat_points == 2 and magic_points == 3 and stealth_points == 5:
    player_class = "Monk"
  elif combat_points == 2 and magic_points == 2 and stealth_points == 6:
    player_class = "Acrobat"
  elif 0 <= combat_points <= 1 and magic_points == 6 and 3 <= stealth_points <= 4:
    player_class = "Battlemage"
  elif combat_points == 1 and magic_points == 3 and stealth_points == 6:
    player_class = "Assassin"
  elif combat_points == 3 and magic_points == 2 and stealth_points == 5:
    player_class = "Pilgrim"
  else:
    player_class = "Custom class"

  return f"""
  You are {player_race}, from the province of {player_province}. Your class is {player_class} and you were born under the sign of the {birth_sign}.<br>
  <br><br>
  Race Description: {race_description[player_race]}
  <br><br>
  Class Description: {class_description[player_class]}
  <br><br>
  Birthsign Description: {birthsign_description[birth_sign]}
  <br><br>
  Thanks for joining the journey—check out the code on GitHub for more! <a href="https://github.com/hungkach/morrowind-quiz-flask">View on GitHub</a>
"""


#Race Descriptions
race_description = {
    "a Nord": "The citizens of Skyrim are aggressive and fearless in war, industrious and enterprising in trade and exploration. Strong, stubborn, and hardy, Nords are famous for their resistance to cold, even magical frost. Violence is an accepted and comfortable aspect of Nord culture; Nords of all classes are skilled with a variety of weapon and armor styles, and they cheerfully face battle with an ecstatic ferocity that shocks and appalls their enemies.",
    "a Dark Elf, also known as Dunmer": "In the Empire,\"Dark Elves\" is the common usage, but in their Morrowind homeland, they call themselves the \"Dunmer\". The dark-skinned, red-eyed Dark Elves combine powerful intellect with strong and agile physiques, producing superior warriors and sorcerers. On the battlefield, Dark Elves are noted for their skilled and balanced integration of swordsmen, marksmen, and war wizards. In character, they are grim, distrusting, and disdainful of other races.",
    "an Imperial": "The well-educated and well-spoken natives of Cyrodiil are known for the discipline and training of their citizen armies. Though physically less imposing than the other races, Imperials are shrewd diplomats and traders, and these traits, along with their remarkable skill and training as light infantry, have enabled them to subdue all the other nations and races, and to have erected the monument to peace and prosperity that comprises the Glorious Empire.",
    "a Breton": "Passionate and eccentric, poetic and flamboyant, intelligent and willful, the Bretons feel an inborn, instinctive bond with the mercurial forces of magic and the supernatural. Many great sorcerers have come out of their home province of High Rock, and in addition to their quick and perceptive grasp of spellcraft, enchantment, and alchemy, even the humblest of Bretons can boast a high resistance to destructive and dominating magical energies.",
    "a Redguard": "The most naturally talented warriors in Tamriel, the dark-skinned, wiry-haired Redguards of Hammerfell seem born to battle, though their pride and fierce independence of spirit makes them more suitable as scouts or skirmishers, or as free-ranging heroes and adventurers, than as rank-and-file soldiers. In addition to their cultural affinities for many weapon and armor styles, Redguards are also physically blessed with hardy constitutions and quickness of foot.",
    "an Argonian": "At home in water and on land, the Argonians of Black Marsh are well-suited to the treacherous swamps of their homeland, with natural immunities protecting them from disease and poison. The female life-phase is highly intelligent, and gifted in the magical arts. The more aggressive male phase has the traits of the hunter: stealth, speed, and agility. Argonians are reserved with strangers, yet fiercely loyal to those they accept as friends. Like the Khajiit, Argonians are limited to some headgear and no footwear.",
    "a Wood Elf, also known as Bosmer": "The Wood Elves are the various barbarian Elven clanfolk of the Western Valenwood forests. These country cousins of the High Elves and Dark Elves are nimble and quick in body and wit, and because of their curious natures and natural agility, Wood Elves are especially suitable as scouts, agents, and thieves. But most of all, the Wood Elves are known for their skills with bows; there are no finer archers in all of Tamriel.",
    "a High Elf, also known as Altmer": "The High Elves consider themselves the most civilized culture of Tamriel; the common tongue of the Empire, Tamrielic, is based on Altmer speech and writing, and most of the Empire's arts, crafts, and sciences derive from High Elven traditions. Deft, intelligent, and strong-willed, High Elves are often gifted in the arcane arts, and High Elves boast that their sublime physical natures make them far more resistant to disease than the \"lesser races.\"",
    "a Khajiit": "The Khajiit of Elsweyr can vary in appearance from nearly Elven to the cathay-raht \"jaguar men\" to the great Senche-Tiger. The most common breed found in Morrowind, the suthay-raht, is intelligent, quick, and agile. Khajiit of all breeds have a weakness for sweets, especially the drug known as skooma. Many Khajiit disdain weapons in favor of their natural claws. They make excellent thieves due to their natural agility and unmatched acrobatics ability.",
    "an Orc": "These sophisticated barbarian beast peoples of the Wrothgarian and Dragontail Mountains are noted for their unshakeable courage in war and their unflinching endurance of hardships. Orc warriors in heavy armor are among the finest front-line troops in the Empire. Most Imperial citizens regard Orc society as rough and cruel, but there is much to admire in their fierce tribal loyalties and generous equality of rank and respect among the sexes.",
}

#BirthSign Descriptions
birthsign_description = {
    "Warrior": "The Warrior is the first Guardian Constellation and he protects his charges during their Seasons. The Warrior's own season is Last Seed when his Strength is needed for the harvest. His Charges are the Lady, the Steed, and the Lord. Those born under the sign of the Warrior are skilled with weapons of all kinds, but prone to short tempers.",
    "Mage": "The Mage is a Guardian Constellation whose Season is Rain's Hand when magicka was first used by men. His Charges are the Apprentice, the Golem, and the Ritual. Those born under the Mage have more magicka and talent for all kinds of spellcasting, but are often arrogant and absent-minded.",
    "Thief": "The Thief is the last Guardian Constellation, and her Season is the darkest month of Evening Star. Her Charges are the Lover, the Shadow, and the Tower. Those born under the sign of the Thief are not typically thieves, though they take risks more often and only rarely come to harm. They will run out of luck eventually, however, and rarely live as long as those born under other signs.",
    "Serpent": "The Serpent wanders about in the sky and has no Season, though its motions are predictable to a degree. No characteristics are common to all who are born under the sign of the Serpent. Those born under this sign are the most blessed and the most cursed.",
    "Lady": "The Lady is one of the Warrior's Charges and her Season is Heartfire. Those born under the sign of the Lady are kind and tolerant.",
    "Steed": "The Steed is one of the Warrior's Charges, and her Season is Mid Year. Those born under the sign of the Steed are impatient and always hurrying from one place to another.",
    "Lord": "The Lord's Season is First Seed and he oversees all of Tamriel during the planting. Those born under the sign of the Lord are stronger and healthier than those born under other signs.",
    "Apprentice": "The Apprentice's Season is Sun's Height. Those born under the sign of the apprentice have a special affinity for magick of all kinds, but are more vulnerable to magick as well.",
    "Atronach": "The Atronach (often called the Golem) is one of the Mage's Charges. Its season is Sun's Dusk. Those born under this sign are natural sorcerers with deep reserves of magicka, but they cannot generate magicka of their own.",
    "Ritual": "The Ritual is one of the Mage's Charges and its Season is Morning Star. Those born under this sign have a variety of abilities depending on the aspects of the moons and the Divines.",
    "Lover": "The Lover is one of the Thief's Charges and her season is Sun's Dawn. Those born under the sign of the Lover are graceful and passionate.",
    "Shadow": "The Shadow's Season is Second Seed. The Shadow grants those born under her sign the ability to hide in shadows.",
    "Tower": "The Tower is one of the Thief's Charges and its Season is Frostfall. Those born under the sign of the Tower have a knack for finding gold and can open locks of all kinds.",
}

class_description = {
    "Acrobat": "Acrobat is a polite euphemism for agile burglars and second-story men. These thieves avoid detection by stealth, and rely on mobility and cunning to avoid capture.",
    "Agent": "Agents are operatives skilled in deception and avoidance, but trained in self-defense and the use of deadly force. Self-reliant and independent, agents devote themselves to personal goals, or to various patrons or causes.",
    "Archer": "Archers are fighters specializing in long-range combat and rapid movement. Opponents are kept at distance by ranged weapons and swift maneuver, and engaged in melee with sword and shield after the enemy is wounded and weary.",
    "Assassin": "Assassins are killers who rely on stealth and mobility to approach victims undetected. Execution is with ranged weapons or with short blades for close work. Assassins include ruthless murderers and principled agents of noble causes.",
    "Barbarian": "Barbarians are the proud, savage warrior elite of the plains nomads, mountain tribes, and sea reavers. They tend to be brutal and direct, lacking civilized graces, but they glory in heroic feats, and excel in fierce, frenzied single combat.",
    "Bard": "Bards are loremasters and storytellers. They crave adventure for the wisdom and insight to be gained, and must depend on sword, shield, spell and enchantment to preserve them from the perils of their educational experiences.",
    "Battlemage": "Battlemages are wizard-warriors, trained in both lethal spellcasting and heavily armored combat. They sacrifice mobility and versatility for the ability to supplement melee and ranged attacks with elemental damage and summoned creatures.",
    "Crusader": "Any heavily armored warrior with spellcasting powers and a good cause may call himself a Crusader. Crusaders do well by doing good. They hunt monsters and villains, making themselves rich by plunder as they rid the world of evil.",
    "Healer": "Healers are spellcasters who swear solemn oaths to heal the afflicted and cure the diseased. When threatened, they defend themselves with reason and disabling attacks and magic, relying on deadly force only in extremity.",
    "Knight": "Of noble birth, or distinguished in battle or tourney, knights are civilized warriors, schooled in letters and courtesy, governed by the codes of chivalry. In addition to the arts of war, knights study the lore of healing and enchantment.",
    "Mage": "Most mages claim to study magic for its intellectual rewards, but they also often profit from its practical applications. Varying widely in temperament and motivation, mages share but one thing in common - an avid love of spellcasting.",
    "Monk": "Monks are students of the ancient martial arts of hand-to-hand combat and unarmored self defense. Monks avoid detection by stealth, mobility, and agility, and are skilled with a variety of ranged and close-combat weapons.",
    "Nightblade": "Nightblades are spellcasters who use their magics to enhance mobility, concealment, and stealthy close combat. They have a sinister reputation, since many nightblades are thieves, enforcers, assassins, or covert agents.",
    "Pilgrim": "Pilgrims are travellers, seekers of truth and enlightenment. They fortify themselves for road and wilderness with arms, armor, and magic, and through wide experience of the world, they become shrewd in commerce and persuasion.",
    "Rogue": "Rogues are adventurers and opportunists with a gift for getting in and out of trouble. Relying variously on charm and dash, blades and business sense, they thrive on conflict and misfortune, trusting to their luck and cunning to survive.",
    "Scout": "Scouts rely on stealth to survey routes and opponents, using ranged weapons and skirmish tactics when forced to fight. By contrast with barbarians, in combat scouts tend to be cautious and methodical, rather than impulsive.",
    "Sorcerer": "Though spellcasters by vocation, sorcerers rely most on summonings and enchantments. They are greedy for magic scrolls, rings, armor and weapons, and commanding undead and Daedric servants gratifies their egos.",
    "Spellsword": "Spellswords are spellcasting specialists trained to support Imperial troops in skirmish and in battle. Veteran spellswords are prized as mercenaries, and well-suited for careers as adventurers and soldiers-of-fortune.",
    "Thief": "Thieves are pickpockets and pilferers. Unlike robbers, who kill and loot, thieves typically choose stealth and subterfuge over violence, and often entertain romantic notions of their charm and cleverness in their acquisitive activities.",
    "Warrior": "Warriors are the professional men-at-arms, soldiers, mercenaries, and adventurers of the Empire, trained with various weapons and armor styles, conditioned by long marches, and hardened by ambush, skirmish, and battle.",
    "Witchhunter": "Witchhunters are dedicated to rooting out and destroying the perverted practices of dark cults and profane sorcery. They train for martial, magical, and stealthy war against vampires, witches, warlocks, and necromancers.",
}

if __name__ == "__main__":
  app.run(debug=True)