import random

playerOne = {} #dicionario para aytribuir status do playerOne USE ESTE VERSÃO FINAL
#playerOne = {'Name': 'Teste', 'hp': 5000, 'mp': 1000, 'level': 50, 'exp': 0, 'attackPower': 150, 'magicPower': 250, 'exp_next_level': 100}  #dicionario para testes
magicTypes = ['Fire', 'Ice', 'Thunder']
items = {'Potion': 3, 'Ether': 2}
weapons = [] #list for keep the weapons
encounters = 0  #the limit to end the game is 16
bossBeat = 0    #the limit to end the game is 2
base_hp = None
base_mp = None


def mainMenu():
  print("=" * 40)
  print(f'=============== Unfair =================')
  print("=" * 40)
  print(f'Main Menu')
  print(f'1. New Game')
  if bossBeat >= 2:
    print('0. New Game+')
  print(f'2. Quit')
  print()
  print("=" * 40)
  print(f'Demo - Version 1.3')
  print("=" * 40)
  print()

  try:
    userChoice = int(input(f'Enter your choice: '))
  except ValueError:
    print(f'Just type the number of the option that you want!\n')
    return mainMenu()

  if userChoice == 1:
    return newGame()
  if userChoice == 2:
    return print(f'You exited the game!')
  if userChoice == 0:
    print(f'In this mode you can start a new game with all your status, items and weapon\n.')
    print(f'Do you want to continue?')
    print(f'1. Yes')
    print(f'2. No')

    try:
      ngpChoice = int(input('Set your choice: '))
    except ValueError:
      print(f'Just set the number of the option that you want')
      return mainMenu()

    if ngpChoice == 1:
      newgamePlus()
    else:
      return mainMenu()


def newGame():
  global base_hp
  global base_mp

  print(f'The world is cruel...')
  print(f'The world is empty...')
  print(f'The world is dark...')
  print(f'There is evil and unjustice...')
  print(f'But...')
  print(f'Someone has to do something about that.')
  print(f'Your journey starts here.\n')

  playerName = input(f'Enter your name: ')
  playerOne.update({'Name':playerName, 'hp':500, 'level': 1, 'exp': 0, 'mp':100, 'attackPower':30, 'magicPower': 45, 'exp_next_level':100})
  weapons.append('old sword')
  print(f'{playerName}: Ahrr...Ahrrr...Ahrrr..')
  print(f'{playerName}: Where am i?')
  print(f'{playerName}: This place is so dark and gloomy.')
  print(f'{playerName}: Its looks like a cave.')
  print(f'{playerName}: Theres something here! A sword and some items:\n')
  print(f'Your HP is {playerOne.get("hp")} and your MP is {playerOne.get("mp")}\n')
  print(f'You have got this items:\n')

  for key, value in items.items():
    print(key, value)

  print()
  print(f'{playerName}: I need get out of here.\nWait!')
  print(f'{playerName}: There is plaque here, is write "Cave of Despair"\n')

  base_hp = playerOne['hp']
  base_mp = playerOne['mp']

  while True:
    print(f'{playerName}:Should i enter the cave?')
    print(f'1. Yes')
    print(f'2. No')
    print()

    try:
      userChoice = int(input(f'Enter your choice: '))
    except ValueError:
      print(f'Just insert the number of the option that you want.')
      continue

    print()

    if userChoice == 1:
      return combat()
    elif userChoice == 2:
      print(f'{playerName}: I Dont have choice, i have yo enter!\n')
    else:
      print(f'Invalid choice\n')

def newgamePlus():
  global encounters
  global base_hp
  global base_mp

  encounters = 0

  print(f'The world is cruel...')
  print(f'The world is empty...')
  print(f'The world is dark...')
  print(f'There is evil and unjustice...')
  print(f'But...')
  print(f'Someone has to do something about that.')
  print(f'Your journey starts here.\n')

  playerName = input(f'Enter your name: ')
  print(f'{playerName}: Ahrr...Ahrrr...Ahrrr..')
  print(f'{playerName}: Where am i?')
  print(f'{playerName}: This place is so dark and gloomy.')
  print(f'{playerName}: Its looks like a cave.')
  print(f'{playerName}: Theres something here! A sword and some items:\n')
  print(f'Your HP is {playerOne.get("hp")} and your MP is {playerOne.get("mp")}\n')
  print(f'You have got this items:\n')

  for key, value in items.items():
    print(key, value)

  print()
  print(f'{playerName}: I need get out of here.\nWait!')
  print(f'{playerName}: There is plaque here, is write "Cave of Despair"\n')

  base_hp = playerOne['hp']
  base_mp = playerOne['mp']

  while True:
    print(f'{playerName}:Should i enter the cave?')
    print(f'1. Yes')
    print(f'2. No')
    print()

    try:
      userChoice = int(input(f'Enter your choice: '))
    except ValueError:
      print(f'Just insert the number of the option that you want.')
      continue

    print()

    if userChoice == 1:
      return combat()
    elif userChoice == 2:
      print(f'{playerName}: I Dont have a choice, i have yo enter!\n')
    else:
      print(f'Invalid choice\n')


def combat():
  global encounters
  global base_hp
  global base_mp

  enemy = {'Name': 'Goblin', 'hp': 100}
  encounters += 1
  battle_exp = 0

  if encounters == 1: #condition to skip the talk for the next battles
    print()
    print(f'{playerOne.get("Name")}: This place smells like shit!')
    print(f'{playerOne.get("Name")}: Theres blood in everywhere!')
    print(f'{playerOne.get("Name")}: Ahhh!\nTheres someone here\n')
    print(f'{enemy.get("Name")}: Rssss.rssssrsss...')
    print(f'{playerOne.get("Name")}: My God! What the fuck is this?')
    print(f'{enemy.get("Name")}: Ahhhh!!!')
    print()
    print(f'FIGHT FOR YOUR LIFE!')
    print(f'You have encountered a {enemy.get("Name")}\n')
    print()
  else:
    print(f'You have encountered a {enemy.get("Name")}\n')

  while True:
    if playerOne['hp'] <= 0:
      print(f'You have died!\nGame over!\n')
      return mainMenu()
    elif enemy['hp'] <= 0:
      print(f'You have defeated the {enemy.get("Name")}')
      print()
      battle_exp = 50
      playerOne['exp'] += battle_exp
      print(f'You won {battle_exp} exp for this battle.\n')
      print()
      return levelProgression()

    print(f'1 - Attack')
    print(f'2 - Magic')
    print(f'3 - item')
    print(f'4 - Run')
    print()

    try:
      userChoice = int(input(f'Enter your choice: '))
    except ValueError:
      print(f'Just type the number of the option that you want!\n')
      continue


    if userChoice == 1:
      hitPlayer = playerOne['attackPower']
      enemy['hp'] -= hitPlayer
      print(f'You hit the {enemy.get("Name")} for {hitPlayer} damage')
      print(f'The {enemy.get("Name")} hp is {enemy.get("hp")}')
      print()
    elif userChoice == 2:
      if playerOne['mp'] > 0:
        print(f'1 - Fire')
        print(f'2 - Ice')
        print(f'3 - Thunder')
        print()

        magicChoice = int(input(f'Enter your choice: '))

        if magicChoice == 1:
          playerOne['mp'] -= 5
          magicHit = playerOne['magicPower']
          magicHit += 5
          enemy['hp'] -= magicHit
          print(f'Fire')
          print(f'Your magic hit the {enemy.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {enemy.get("Name")} hp is {enemy.get("hp")}')
          print()
        elif magicChoice == 2:
          playerOne['mp'] -= 5
          magicHit = playerOne['magicPower']
          magicHit += 5
          enemy['hp'] -= magicHit
          print(f'Ice')
          print(f'Your magic hit the {enemy.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {enemy.get("Name")} hp is {enemy.get("hp")}')
          print()
        elif magicChoice == 3:
          playerOne['mp'] -= 10
          magicHit = playerOne['magicPower']
          magicHit += 10
          enemy['hp'] -= magicHit
          print(f'Thunder')
          print(f'Your magic hit the {enemy.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {enemy.get("Name")} hp is {enemy.get("hp")}')
          print()
      else:
        print(f'You dont have enough MP to use magic!')
        print()
    elif userChoice == 3:
      print(f'You have this items:\n')

      for key, value in items.items():
        print(f'{key} x {value}')

      try:
        itemChoice = input(f'Enter your choice: ')
      except ValueError:
        print(f'Just write down the name the item that you want!\n')
        continue

      if itemChoice == 'Potion':
        if itemChoice in items:
          if items[itemChoice] > 0:
            if playerOne['hp'] < base_hp:
              items[itemChoice] -= 1
              playerOne['hp'] += 100
            else:
              print(f'Your HP is already full!\n')
          else:
            print(f'You dont have any more Potions')
      elif itemChoice == 'Ether':
        if itemChoice in items:
          if items[itemChoice] > 0:
            if playerOne['mp'] < base_mp:
              items[itemChoice] -= 1
              playerOne['mp'] += 50
              print(f'Your MP is {playerOne.get("mp")}\n')
            else:
              print(f'Your MP is already full!\n')
          else:
            print(f'You dont have any more Ethers')
      else:
        print(f'Invalid choice')

    elif userChoice == 4:
      print(f'You ran away from this battle.')
      return posBattle()
    else:
      print(f'Invalid choice')


    if enemy['hp'] > 0:
      if enemy['hp'] != 0 and enemy['hp'] <= 20:
        print(f'Lets play Head and Tails!\n')
        coin = random.randrange(0, 2, 1)
        if coin == 0:
          print(f'Heads!\n')
          enemy['hp'] += 20
          print(f'The {enemy.get("Name")} hp is {enemy.get("hp")}')
        else:
          print(f'Tails!\n')
          criticalHit = 50
          playerOne['hp'] -= criticalHit
          print(f'The {enemy.get("Name")} hit you for {criticalHit} damage')
          print(f'Your hp is {playerOne.get("hp")}')

      enemyHit = random.randrange(0, 25, 1)
      playerOne['hp'] -= enemyHit
      print(f'The {enemy.get("Name")} hit you for {enemyHit} damage')
      print(f'Your hp is {playerOne.get("hp")}')

def combat2():
  global encounters
  global base_hp
  global base_mp

  enemy = {'Name': 'Undead', 'hp': 250}
  encounters += 1
  battle_exp = 0

  if encounters == 7: #condition to skip the talk for the next battles
    print()
    print(f'{playerOne.get("Name")}: This place is different. But still dark.')
    print(f'{playerOne.get("Name")}: There are a person over there!')
    print(f'{playerOne.get("Name")}: Hi! Are you lost here too?')
    print(f'{enemy.get("Name")}: Haaaaa....Haaaaa...')
    print(f'{playerOne.get("Name")}: Are you okay dude?')
    print(f'{enemy.get("Name")}: Haaaaa....Haaaaa...')
    print(f'{playerOne.get("Name")}: Wait! This is person is deade')
    print(f'{enemy.get("Name")}: Haaaaa....Haaaaa...')
    print(f'{playerOne.get("Name")}: Stop to try to hit me!')
    print(f'{playerOne.get("Name")}: Stop motherfucker!')
    print(f'{enemy.get("Name")}: Haaaaa....Haaaaa...')
    print(f'{playerOne.get("Name")}: I have no choice. I have to kill this thing!')
    print()
    print(f'FIGHT FOR YOUR LIFE!')
    print(f'You have encountered a {enemy.get("Name")}\n')
    print()
  else:
    print(f'You have encountered a {enemy.get("Name")}\n')

  while True:
    if playerOne['hp'] <= 0:
      print(f'You have died!\nGame over!\n')
      return mainMenu()
    elif enemy['hp'] <= 0:
      print(f'You have defeated the {enemy.get("Name")}')
      print()
      battle_exp = 150
      playerOne['exp'] += battle_exp
      print(f'You won {battle_exp} exp for this battle.\n')
      print()
      return levelProgression()

    print(f'1 - Attack')
    print(f'2 - Magic')
    print(f'3 - item')
    print(f'4 - Run')
    print()

    try:
      userChoice = int(input(f'Enter your choice: '))
    except ValueError:
      print(f'Just type the number of the option that you want!\n')
      continue


    if userChoice == 1:
      hitPlayer = playerOne['attackPower']
      enemy['hp'] -= hitPlayer
      print(f'You hit the {enemy.get("Name")} for {hitPlayer} damage')
      print(f'The {enemy.get("Name")} hp is {enemy.get("hp")}')
      print()
    elif userChoice == 2:
      if playerOne['mp'] > 0:
        print(f'1 - Fire')
        print(f'2 - Ice')
        print(f'3 - Thunder')
        print()

        magicChoice = int(input(f'Enter your choice: '))

        if magicChoice == 1:
          playerOne['mp'] -= 5
          magicHit = playerOne['magicPower']
          magicHit += 5
          enemy['hp'] -= magicHit
          print(f'Fire')
          print(f'Your magic hit the {enemy.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {enemy.get("Name")} hp is {enemy.get("hp")}')
          print()
        elif magicChoice == 2:
          playerOne['mp'] -= 5
          magicHit = playerOne['magicPower']
          magicHit += 5
          enemy['hp'] -= magicHit
          print(f'Ice')
          print(f'Your magic hit the {enemy.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {enemy.get("Name")} hp is {enemy.get("hp")}')
          print()
        elif magicChoice == 3:
          playerOne['mp'] -= 10
          magicHit = playerOne['magicPower']
          magicHit += 10
          enemy['hp'] -= magicHit
          print(f'Thunder')
          print(f'Your magic hit the {enemy.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {enemy.get("Name")} hp is {enemy.get("hp")}')
          print()
      else:
        print(f'You dont have enough MP to use magic!')
        print()
    elif userChoice == 3:
      print(f'You have this items:\n')

      for key, value in items.items():
        print(f'{key} x {value}')

      try:
        itemChoice = input(f'Enter your choice: ')
      except ValueError:
        print(f'Just write down the name the item that you want!\n')
        continue

      if itemChoice == 'Potion':
        if itemChoice in items:
          if items[itemChoice] > 0:
            if playerOne['hp'] < base_hp:
              items[itemChoice] -= 1
              playerOne['hp'] += 100
            else:
              print(f'Your HP is already full!\n')
          else:
            print(f'You dont have any more Potions')
      elif itemChoice == 'Ether':
        if itemChoice in items:
          if items[itemChoice] > 0:
            if playerOne['mp'] < base_mp:
              items[itemChoice] -= 1
              playerOne['mp'] += 50
              print(f'Your MP is {playerOne.get("mp")}\n')
            else:
              print(f'Your MP is already full!\n')
          else:
            print(f'You dont have any more Ethers')
      else:
        print(f'Invalid choice')

    elif userChoice == 4:
      print(f'You ran away from this battle.')
      return posBattle()
    else:
      print(f'Invalid choice')


    if enemy['hp'] > 0:
      if enemy['hp'] != 0 and enemy['hp'] <= 50:
        print(f'Lets play Head and Tails!\n')
        coin = random.randrange(0, 2, 1)
        if coin == 0:
          print(f'Heads!\n')
          enemy['hp'] += 30
          print(f'The {enemy.get("Name")} hp is {enemy.get("hp")}')
        else:
          print(f'Tails!\n')
          criticalHit = 100
          playerOne['hp'] -= criticalHit
          print(f'The {enemy.get("Name")} hit you for {criticalHit} damage')
          print(f'Your hp is {playerOne.get("hp")}')

      enemyHit = random.randrange(0, 50, 5)
      playerOne['hp'] -= enemyHit
      print(f'The {enemy.get("Name")} hit you for {enemyHit} damage')
      print(f'Your hp is {playerOne.get("hp")}')

def bossBattle():
  global encounters
  global bossBeat
  global base_hp
  global base_mp

  battle_exp = 0
  boss = {'Name': 'King Goblin', 'hp': 500}

  print(f'You have encountered a {boss.get("Name")}')
  print()

  while True:
    if playerOne['hp'] <= 0:
      print(f'You have died!\nGame over!\n')
      return mainMenu()
    elif boss['hp'] <= 0:
      print(f'You have defeated the {boss.get("Name")}')
      print()
      encounters += 1
      bossBeat += 1
      battle_exp = 300
      playerOne['exp'] += battle_exp
      print(f'You won {battle_exp} exp for this battle.\n')
      print()
      return levelProgression()

    print(f'1 - Attack')
    print(f'2 - Magic')
    print(f'3 - item')
    print(f'4 - Run')
    print()

    try:
      userChoice = int(input(f'Enter your choice: '))
    except ValueError:
      print(f'Just type the number of the option that you want!\n')
      continue

    if userChoice == 1:
      hitPlayer = playerOne['attackPower']
      boss['hp'] -= hitPlayer
      print(f'You hit the {boss.get("Name")} for {hitPlayer} damage')
      print(f'The {boss.get("Name")} hp is {boss.get("hp")}')
      print()
    elif userChoice == 2:
      if playerOne['mp'] > 0:
        print(f'1 - Fire')
        print(f'2 - Ice')
        print(f'3 - Thunder')
        print()

        try:
          magicChoice = int(input(f'Enter your choice: '))
        except ValueError:
          print(f'Just type the number of the option that you want!\n')
          continue

        if magicChoice == 1:
          playerOne['mp'] -= 5
          magicHit = playerOne['magicPower']
          magicHit += 5
          boss['hp'] -= magicHit
          print(f'Fire')
          print(f'Your magic hit the {boss.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {boss.get("Name")} hp is {boss.get("hp")}')
          print()
        elif magicChoice == 2:
          playerOne['mp'] -= 5
          magicHit = playerOne['magicPower']
          magicHit += 5
          boss['hp'] -= magicHit
          print(f'Ice')
          print(f'Your magic hit the {boss.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {boss.get("Name")} hp is {boss.get("hp")}')
          print()
        elif magicChoice == 3:
          playerOne['mp'] -= 10
          magicHit = playerOne['magicPower']
          magicHit += 10
          boss['hp'] -= magicHit
          print(f'Thunder')
          print(f'Your magic hit the {boss.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {boss.get("Name")} hp is {boss.get("hp")}')
          print()
      else:
        print(f'You dont have enough MP to use magic!')
        print()
    elif userChoice == 3:
      print(f'You have this items:\n')

      for key, value in items.items():
        print(f'{key} x {value}')

      try:
        itemChoice = input(f'Enter your choice: ')
      except ValueError:
        print(f'Just write down the name the item that you want!\n')
        continue

      if itemChoice == 'Potion':
        if itemChoice in items:
          if items[itemChoice] > 0:
            if playerOne['hp'] < base_hp:
              items[itemChoice] -= 1
              playerOne['hp'] += 100
            else:
              print(f'Your HP is already full!\n')
          else:
            print(f'You dont have any more Potions')
      elif itemChoice == 'Ether':
        if itemChoice in items:
          if items[itemChoice] > 0:
            if playerOne['mp'] < base_mp:
              items[itemChoice] -= 1
              playerOne['mp'] += 50
              print(f'Your MP is {playerOne.get("mp")}\n')
            else:
              print(f'Your MP is already full!\n')
          else:
            print(f'You dont have any more Ethers')
      else:
        print(f'Invalid choice')

    elif userChoice == 4:
      print(f'You can not ran away from this battle!')
    else:
      print(f'Invalid choice')


    if boss['hp'] <= 100:
      print(f'Lets play Head and Tails')
      coin = random.randrange(0, 2, 1)
      if coin == 0:
        print(f'Heads!\n')
        boss['hp'] += 55
        print(f'The {boss.get("Name")} hp is {boss.get("hp")}')
      else:
        print(f'Tails!\n')
        criticalHit = 200
        playerOne['hp'] -= criticalHit
        print(f'The {boss.get("Name")} hit you for {criticalHit} damage')
        print(f'Your hp is {playerOne.get("hp")}')
    else:
      bossHit = random.randrange(0, 100, 10)
      playerOne['hp'] -= bossHit
      print(f'The {boss.get("Name")} hit you for {bossHit} damage')
      print(f'Your hp is {playerOne.get("hp")}')

def bossBattle2():
  global encounters
  global bossBeat
  global base_hp
  global base_mp

  battle_exp = 0
  boss = {'Name': 'Reaper', 'hp': 1000}

  print(f'You have encountered a {boss.get("Name")}')
  print()

  while True:
    if playerOne['hp'] <= 0:
      print(f'You have died!\nGame over!\n')
      return mainMenu()
    elif boss['hp'] <= 0:
      print(f'You have defeated the {boss.get("Name")}')
      print()
      encounters += 1
      bossBeat += 1
      battle_exp = 1000
      playerOne['exp'] += battle_exp
      print(f'You won {battle_exp} exp for this battle.\n')
      print()
      return levelProgression()

    print(f'1 - Attack')
    print(f'2 - Magic')
    print(f'3 - item')
    print(f'4 - Run')
    print()

    try:
      userChoice = int(input(f'Enter your choice: '))
    except ValueError:
      print(f'Just type the number of the option that you want!\n')
      continue

    if userChoice == 1:
      hitPlayer = playerOne['attackPower']
      boss['hp'] -= hitPlayer
      print(f'You hit the {boss.get("Name")} for {hitPlayer} damage')
      print(f'The {boss.get("Name")} hp is {boss.get("hp")}')
      print()
    elif userChoice == 2:
      if playerOne['mp'] > 0:
        print(f'1 - Fire')
        print(f'2 - Ice')
        print(f'3 - Thunder')
        print()

        try:
          magicChoice = int(input(f'Enter your choice: '))
        except ValueError:
          print(f'Just type the number of the option that you want!\n')
          continue

        if magicChoice == 1:
          playerOne['mp'] -= 5
          magicHit = playerOne['magicPower']
          magicHit += 5
          boss['hp'] -= magicHit
          print(f'Fire')
          print(f'Your magic hit the {boss.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {boss.get("Name")} hp is {boss.get("hp")}')
          print()
        elif magicChoice == 2:
          playerOne['mp'] -= 5
          magicHit = playerOne['magicPower']
          magicHit += 5
          boss['hp'] -= magicHit
          print(f'Ice')
          print(f'Your magic hit the {boss.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {boss.get("Name")} hp is {boss.get("hp")}')
          print()
        elif magicChoice == 3:
          playerOne['mp'] -= 10
          magicHit = playerOne['magicPower']
          magicHit += 10
          boss['hp'] -= magicHit
          print(f'Thunder')
          print(f'Your magic hit the {boss.get("Name")} for {magicHit} damage')
          print(f'Your MP is {playerOne.get("mp")}')
          print(f'The {boss.get("Name")} hp is {boss.get("hp")}')
          print()
      else:
        print(f'You dont have enough MP to use magic!')
        print()
    elif userChoice == 3:
      print(f'You have this items:\n')

      for key, value in items.items():
        print(f'{key} x {value}')

      try:
        itemChoice = input(f'Enter your choice: ')
      except ValueError:
        print(f'Just write down the name the item that you want!\n')
        continue

      if itemChoice == 'Potion':
        if itemChoice in items:
          if items[itemChoice] > 0:
            if playerOne['hp'] < base_hp:
              items[itemChoice] -= 1
              playerOne['hp'] += 100
            else:
              print(f'Your HP is already full!\n')
          else:
            print(f'You dont have any more Potions')
      elif itemChoice == 'Ether':
        if itemChoice in items:
          if items[itemChoice] > 0:
            if playerOne['mp'] < base_mp:
              items[itemChoice] -= 1
              playerOne['mp'] += 50
              print(f'Your MP is {playerOne.get("mp")}\n')
            else:
              print(f'Your MP is already full!\n')
          else:
            print(f'You dont have any more Ethers')
      else:
        print(f'Invalid choice')

    elif userChoice == 4:
      print(f'You can not ran away from this battle!')
    else:
      print(f'Invalid choice')


    if boss['hp'] <= 200:
      print(f'Lets play Head and Tails')
      coin = random.randrange(0, 2, 1)
      if coin == 0:
        print(f'Heads!\n')
        boss['hp'] += 80
        print(f'The {boss.get("Name")} hp is {boss.get("hp")}')
      else:
        print(f'Tails!\n')
        criticalHit = 300
        playerOne['hp'] -= criticalHit
        print(f'The {boss.get("Name")} hit you for {criticalHit} damage')
        print(f'Your hp is {playerOne.get("hp")}')
    else:
      bossHit = random.randrange(0, 200, 50)
      playerOne['hp'] -= bossHit
      print(f'The {boss.get("Name")} hit you for {bossHit} damage')
      print(f'Your hp is {playerOne.get("hp")}')


def posBattle():

  while True:
    print("=" * 40)
    print(f'PosBattle Menu')
    print()
    print(f'1. Check Status')
    print(f'2. New Battle')
    print(f'3. Play Heads and Tails - XD')
    print(f'4. Weapons')
    print(f'5. Items')
    print(f'6. Exit')
    print()
    print(f'You have encountered {encounters} enemies')
    print()

    try:
      userChoice = int(input(f'Enter your choice: '))
    except ValueError:
      print(f'Just type the number of the option that you want!\n')
      continue

    if userChoice == 1:
      print(f'Character name: {playerOne.get("Name")}')
      print(f'Your HP is {playerOne.get("hp")}')
      print(f'Your MP is {playerOne.get("mp")}')
      print(f'Your level is {playerOne.get("level")}')
      print(f'Your attack power is: {playerOne.get("attackPower")}')
      print(f'Your magic power is: {playerOne.get("magicPower")}')
      print(f'Your exp is {playerOne.get("exp")}')
    elif userChoice == 2:
      if encounters == 6:
        return bossBattle()
      elif encounters > 6 and encounters < 14:
        return combat2()
      elif encounters == 15:
        return bossBattle2()
      elif encounters >= 16:
        return endGame()
      else:
        return combat()
    elif userChoice == 3:
      print(f'Lets play head and tails')
      coin = random.randrange(0, 4, 1)
      if coin == 0:
        playerOne['hp'] -= 50
        print(f'You lost 50 hp XD\n')
        return posBattle()
      else:
        playerOne['hp'] -= 100
        items['Potion'] -= 1
        print(f'You gained 100 hp and lost a Potion XD\n')
        return posBattle()
    elif userChoice == 4:
      return weaponsProgression()
    elif userChoice == 5:
      return itemsMenu()
    elif userChoice == 6:
      return mainMenu()
    else:
      print(f'Invalid choice')
      return posBattle()

def levelProgression():
  global base_hp
  global base_mp

  while playerOne['exp'] >= playerOne['exp_next_level']:  #to use IF condition if you dont want break the game
    playerOne['exp'] -= playerOne['exp_next_level'] #remove form playOne exp key the value and prepare for a next level
    playerOne['hp'] = base_hp + 100
    base_hp = playerOne['hp']
    playerOne['level'] += 1
    playerOne['mp'] = base_mp + 10
    base_mp = playerOne['mp']
    playerOne['attackPower'] += 5
    playerOne['magicPower'] += 5
    playerOne['exp_next_level'] = int(playerOne['exp_next_level'] * 1.5) #multiple the value of exp_next_level by 1.5 for the next level
    print(f'You have leveled up to level {playerOne.get("level")}')
    print()
    print(f'Your news status\n')
    print(f'Your hp is {playerOne.get("hp")}')
    print(f'Your MP is {playerOne.get("mp")}\n')

  return rewards() #reurn for posBattle menu, it must have to be out from while loop

def rewards():
  global encounters

  if encounters == 3:
    items['Potion'] += 2
    items['Ether'] += 1
    print(f'You earned:\n2 x Potions\n1 x Ether\n')
    return posBattle()
  elif encounters == 6:
    items['Potion'] += 2
    print(f'You earned:\n2 x Potions\n')
    return posBattle()
  elif encounters == 7:
    items['Potion'] += 3
    weapons.append('short sword')
    print(f'You earned:\n2 x Potions\n1 x short sword\n')
    return posBattle()
  elif encounters == 10:
    items['Potion'] += 2
    items['Ether'] += 1
    print(f'You earned:\n2 x Potions\n1 x Ether\n')
    return posBattle()
  elif encounters == 13:
    items['Potion'] += 2
    weapons.append('long sword')
    print(f'You earned:\n2 x Potions\n1 x long sword\n')
    return posBattle()
  elif encounters == 16:
    items['Potion'] += 5
    items['Ether'] += 3
    weapons.append('katana')
    print(f'You earned:\n5 x Potions\n3 x Ether\n1 x katana\n')
    return posBattle()
  else:
    print(f'You earned none reward for this battle!\n')
    return posBattle()

def weaponsProgression():
  global attackPower

  print(f'You have this weapons:\n')

  for i in weapons:
    print(i)

  print()

  try:
    weaponChoice = input('Set the Name of the Weapon that you want to equip: ')
  except ValueError:
    print(f'Just set the name of the weapon that you want!\n')

  if weaponChoice == 'old sword':
    playerOne['attackPower'] += 5
    print(f'You eqiped the old sword.\nYour new attack power is {playerOne.get("attackPower")}\n')
    return posBattle()
  elif weaponChoice == 'short sword':
    playerOne['attackPower'] += 10
    print(f'You eqiped the short sword.\nYour new attack power is {playerOne.get("attackPower")}\n')
    return posBattle()
  elif weaponChoice == 'long sword':
    playerOne['attackPower'] += 15
    print(f'You eqiped the long sword.\nYour new attack power is {playerOne.get("attackPower")}\n')
    return posBattle()
  elif weaponChoice == 'katana':
    playerOne['attackPower'] += 30
    print(f'You eqiped the katana.\nYour new attack power is {playerOne.get("attackPower")}\n')
    return posBattle()
  else:
    print('Invalid choice')
    return weaponsProgression()

def itemsMenu():
    global base_hp
    global base_mp

    while True:
      for key, value in items.items():
        print(f'{key} x {value}')
      print()
      try:
        itemChoice = input(f'Enter your choice, set "exit" to leave this menu": ')
      except ValueError:
         print(f'Just write down the name the item that you want!\n')
         continue

      if itemChoice == 'Potion':
        if itemChoice in items:
          if items[itemChoice] > 0:
            if playerOne['hp'] < base_hp:
              items[itemChoice] -= 1
              playerOne['hp'] += 100
              print(f'Your MP is {playerOne.get("hp")}\n')
            else:
              print(f'Your HP is already full!\n')
          else:
            print(f'You dont have any more Potions')
      elif itemChoice == 'Ether':
        if itemChoice in items:
          if items[itemChoice] > 0:
            if playerOne['mp'] < base_mp:
              items[itemChoice] -= 1
              playerOne['mp'] += 50
              print(f'Your MP is {playerOne.get("mp")}\n')
            else:
              print(f'Your MP is already full!\n')
          else:
            print(f'You dont have any more Ethers')
      elif itemChoice == 'exit':
        return posBattle()
      else:
        print(f'Invalid choice')

def endGame():
  print(f'{playerOne.get("Name")}: Finally a managed to get out from that creepy mountain.')
  print(f'{playerOne.get("Name")}: Maybe am i free?')
  print(f'Mysterious voice: Hahaha!!!')
  print(f'{playerOne.get("Name")}: What???')
  print(f'{playerOne.get("Name")}: Whos said that?')
  print(f'Mysterious voice: No! You not free.')
  print(f'{playerOne.get("Name")}: Who fuck are you?')
  print(f'Mysterious voice: Me? I just a man, who want to have fun.')
  print(f'{playerOne.get("Name")}: What the fuck are talking about?')
  print(f'Mysterious voice: Whats the problem? Dont you like to have fun?')
  print(f'Mysterious voice: Because, i do!')
  print(f'{playerOne.get("Name")}: No!!!Go fuck yourself and get out of my way!!!')
  print(f'Mysterious voice: Why are you so angry?')
  print(f'Mysterious voice: Okay. Lets play Heads and Tails.')
  print(f'Mysterious voice: If you win, i am not gonna bother you anymore.\nBut if a win...')
  print(f'{playerOne.get("Name")}: Shut up!!!')
  print(f'Mysterious voice: Too late. I chose Tails.')
  coin = random.randrange(0, 10, 1)
  if coin == 0:
    print(f'Heads!\nI think you win. :(\n')
  elif coin == 1:
    print(f'Tails!\nI think you lose.\n')
  else:
    print(f'Tails!\nI think you lose.\n')

  print(f'Mysterious voice: Well, its seems that we are gonna have so much fun together.')
  print(f'{playerOne.get("Name")}: ......')
  print(f'Mysterious voice: Well, And i just wanna HAVE FUN!!!\nAnd the game just begun.')
  print(f'Mysterious voice: HAHAHAHA!!!!')
  print(f'Mysterious voice: HAHAHAHA!!!!')
  print(f'Mysterious voice: HAHAHAHA!!!!')
  print(f'Mysterious voice: HAHAHAHA!!!!')
  print()
  print()
  print()
  print(f'Congratulations you finshed this demo!')
  print()
  print()
  print()
  print(f'Story Written by Jhonathan Borges')
  print()
  print()
  print()
  print(f'Programing by Jhonathan Borges')
  print()
  print()
  print()
  print(f'Directed by Jhonathan Borges')
  print()
  print()
  print()
  print(f'Thanks for playing!\n')
  print()
  print()
  print()
  print(f'Now you can play the New Game+ from Main Menu.')
  return mainMenu()


mainMenu()

















