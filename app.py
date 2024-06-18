super_dmg = 50
punch_coin_reward = 10
kick_coin_reward = 20


print(f'''
/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/

WARNING!!!

Please watch put for spaces at the 
end of your inputs as this will 
lead to unexpected errors! 

/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/
      ''')




dev_tools = '''
/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-//*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/

Version: 1.0.5 (earlier access)

Patch Notes (18.06.24; 21:34):

    + 'defend' function added to player
    +  mayor bug fixes
    +  balancing 
    +  nerfed onehit to 25% Instead of 30%
    +  nerfed onehit to -50HP instead of -100%
    +  changed 'onehit' name to 'super'
    +  'kick' function added to player
    +  added draw! (fixed win + loose at the same time)
    +  Nerfed kick (no spamming possible)
    +  minor bug fixes

Extra Notes:

    -  still some bugs (will be fixed soon)

/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-//*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/
'''

punch_counter = 0  #counts punches

import random

class Player():

    def __init__ (self, hp, dmg, coins):

        self.hp = hp            #health points
        self.dmg = dmg          #damage per hit
        self.coins = coins      #coins at beginning


        
    def take_punch(self, dmg):

        self.hp -= dmg
        return self.hp



    def punch(self, enemy):
        enemy.take_punch(self.dmg)
        print(f'''
              
------------------------------
Player punch's! Enemy takes {self.dmg} damage.''')
        
      
    def kick(self, enemy):
        enemy.take_kick(self.dmg)
        print(f'''
              
------------------------------
Player kick's! Enemy takes {self.dmg * 2} damage.''')
        
        
    def super(self, dmg):
        self.hp -= super_dmg
        
        print(f'''
------------------------------
Enemy uses super! Player takes {super_dmg} damage.
------------------------------
            ''')

        

    def defend(self):
        pass


        









class Enemy(Player):

    def __init__ (self, hp, dmg, coins):

        super().__init__(hp, dmg, coins)  #super = child of parent (takes hp + dmg from parent)


    def punch(self, player):
        player.take_punch(self.dmg)
        print(f'''

------------------------------
Enemy punch's! {player.__class__.__name__} takes {self.dmg} damage.''')

    def take_punch(self, dmg):
        self.hp -= dmg
        
        
    def take_kick(self, dmg):
        self.hp -= dmg * 2
        







class Shop():
    
    def __init__(self, sps, hps, vcs):
        self.sps = sps  #sps = S trength  P otion  S upply
        self.hps = hps  #hps = H ealth    P otion  S upply
        self.vcs = vcs  #vcs = V ision    C ard    S upply


    def buy_strength_potion(self, sps):
        pass
    
    
    def buy_health_potion(self, hps):
        pass
    

    def buy_vision_card(self, vcs):     #vc reveals "var: next_random_for_enemy"    (still need to remove commas and display action name instead of random number)
        pass                            











player = Player(100, 10, 20)
enemy = Enemy(100, 10, 20)








while enemy.hp > 0 and player.hp > 0:
    a = input()
    b = random.random()
    next_random_for_enemy = random.random()
    

    if a == "info:ver/upd/patn:tools":
        print(dev_tools)


    if b >= 0.25 and a != "defend" and a != "stats" and a != "tutorial" and a != "info:ver/upd/patn:tools" and a != "":
        enemy.punch(player)
        print(f'''
Player's health after punch: {player.hp}
------------------------------''')
        
    if b < 0.25 and a == "defend":
        pass


    if b < 0.25 and a != "defend" and a != "stats" and a != "tutorial" and a != "info:ver/upd/patn:tools" and a != "":
        player.super(enemy.dmg)

    if a == "punch":
        player.punch(enemy)
        punch_counter += 1
        player.coins += punch_coin_reward
        print(f'''
Enemy's health after punch: {enemy.hp}
------------------------------''')
        

    if a == "defend":
        player.defend()
        print(f'''
Player's health after defending: {player.hp}
------------------------------''')
        
        
    if a == "stats":
        print(f''' 
------------------------------
Player HP: {player.hp} DMG: {player.dmg}  Coins: {player.coins}
Enemy HP: {enemy.hp}   DMG: {enemy.dmg}   Coins: {enemy.coins}

Punch Counter: {punch_counter}      
------------------------------''')
        
        
    if a == "tutorial":
        print(f'''
------------------------------------------------------------
The goal of the game is to 
defeat the enemy! The Enemy has
a 30% Chance to hit you with their
super attack which will kill you instantly.
The only way to block this is to use "defend". You can use 
"kick" to kick your opponent. This deals 2x more damage.
(Requires 3 punches to be done before).

Controls:
    + Enter "punch" to punch the opponent
    + Enter "stats" to view your HP and your enemies HP
    + Enter "tutorial" to view this page again
    + Enter "defend" to defend against any attack
    + Enter "info:ver/upd/patn:tools" to view game version
    + Enter "kick" to kick you opponent (2x damage) 
------------------------------------------------------------              
              ''')
     
     
    if a == "kick" and punch_counter < 3:
        print(f'''
------------------------------
You can not kick yet!
------------------------------
''')
       
     
     
        
    if a == "kick" and punch_counter >= 3:
        player.kick(enemy)
        player.coins += kick_coin_reward
        punch_counter -= 1
        print(f'''
Enemy's health after kick: {enemy.hp}
------------------------------''') 
        
        
        
        
    if enemy.hp <= 0 and player.hp > 0:
        print('''
          
******************************
            you win
******************************''')
        
        

    if player.hp <= 0 and enemy.hp > 0:
        print('''
          
******************************
           you loose
******************************''')
        
    
    if player.hp <= 0 and enemy.hp <= 0:
        print(f'''
******************************
  You both die! Nobody wins
******************************

''')
        