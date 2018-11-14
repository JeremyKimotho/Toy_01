from functools import reduce

print('\n')
print('''
  
  ______                                __   ____         ___       ____                      
 /_  __/________ _____  ____  ___  ____/ /  /  _/___     /   |     / __ \____  ____  ____ ___ 
  / / / ___/ __ `/ __ \/ __ \/ _ \/ __  /   / // __ \   / /| |    / /_/ / __ \/ __ \/ __ `__ 
 / / / /  / /_/ / /_/ / /_/ /  __/ /_/ /  _/ // / / /  / ___ |   / _, _/ /_/ / /_/ / / / / / /
/_/ /_/   \__,_/ .___/ .___/\___/\__,_/  /___/_/ /_/  /_/  |_|  /_/ |_|\____/\____/_/ /_/ /_/ 
              /_/   /_/                                                                       
''')
print('\n')
print('Imagine you\'re in an empty room. There are windows and a bed but nothing else.')
print('\n')
print('Someone comes in and tells you, "You can leave now, or you can choose to stay. If you choose to stay, I\'ll give you a dollar, and everyday you stay I\'ll double the amount you have."')
print('\n')
print('In this hypothetical situation, how many days would you stay?')

answer=int(input())

if answer>=0 :
  starter = 1
  daysCounter = 1
  totalEarned = []
  while daysCounter<=answer:
      totalEarned.append(starter)
      daysCounter+=1
      starter*=2
  totals = reduce(lambda a,b : a + b,totalEarned)
  print('\n')
  print('''

  
    ____                           ________          _         
   / __ )_________ __   _____     / ____/ /_  ____  (_)_______ 
  / __  / ___/ __ `/ | / / _ \   / /   / __ \/ __ \/ / ___/ _ 
 / /_/ / /  / /_/ /| |/ /  __/  / /___/ / / / /_/ / / /__/  __/
/_____/_/   \__,_/ |___/\___/   \____/_/ /_/\____/_/\___/\___/ 
                                                               

                                                               
  ''')
  print(f"If you were to stay for {answer} days, you would earn ${totals}")
  print('\n')
else:
  print('\n')
  print('''
    ____  __                                                                          __             
   / __ \/ /__  ____ _________     __  __________     ____ _   ____  __  ______ ___  / /_  ___  _____
  / /_/ / / _ \/ __ `/ ___/ _ \   / / / / ___/ _ \   / __ `/  / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/
 / ____/ /  __/ /_/ (__  )  __/  / /_/ (__  )  __/  / /_/ /  / / / / /_/ / / / / / / /_/ /  __/ /    
/_/   /_/\___/\__,_/____/\___/   \__,_/____/\___/   \__,_/  /_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                                     
                                                                                                     
  ''')
  print('\n')