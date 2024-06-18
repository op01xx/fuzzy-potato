from colorama import Fore, Back, Style 

super_dmg = 50
punch_coin_reward = 10
kick_coin_reward = 20
while_counter = 0
sps_available = False
hps_available = False
vcs_available = False
sps_price = 30
hps_price = 50
vcs_price = 100
shop_active = False



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

Version: 1.0.8 (earlier access)

Patch Notes (18.06.24; 22:56):

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
    +  added colors to terminal
    +  fixed major bugs
    +  added Shop (unfinished)

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
        
        print( Fore.YELLOW  + f'''
------------------------------
Enemy uses super! Player takes {super_dmg} damage.
------------------------------
            ''')
        print( Style.RESET_ALL)

        

    def defend(self):
        pass
    
    
    def sps_use(self):
        self.dmg += 5
        sps_available = False
        
    def hps_use(self):
        self.hp += 30
        sps_available = False
        
    def vcs_use(self):
        if next_random_for_enemy < 0.25:
            reveal = "super"
        
        else: 
            reveal = "normal"
        
        
        print( Fore.BLUE  +f'''
------------------------------
           {reveal}
------------------------------
                  ''')
        print( Style.RESET_ALL)


        









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
        if player.coins >= 30:
            player.coins -= sps_price
            sps_available = True
        else:  
            print(Fore.RED  + f'''
------------------------------
     Not enough Coins! 🪙
------------------------------               
                  ''')
            print( Style.RESET_ALL)
    
    
    def buy_health_potion(self, hps):
        if player.coins >= 50:
            player.coins -= hps_price
            hps_available = True
        else:  
            print(Fore.RED  + f'''
------------------------------
     Not enough Coins! 🪙
------------------------------               
                  ''')
            print( Style.RESET_ALL)
    

    def buy_vision_card(self, vcs):     #vc reveals "var: next_random_for_enemy"    (still need to remove commas and display action name instead of random number)
        if player.coins >= 100:
            player.coins -= vcs_price
            vcs_available = True
        else:  
            print(Fore.RED  + f'''
------------------------------
     Not enough Coins! 🪙
------------------------------               
                  ''')
            print( Style.RESET_ALL)                            











player = Player(100, 10, 20)
enemy = Enemy(100, 10, 20)
shop = Shop(1, 1, 1)








while enemy.hp > 0 and player.hp > 0:
    a = input()
    if while_counter == 0:
        b = random.random()
        next_random_for_enemy = b
        
    b = next_random_for_enemy

    if a == "kick" and punch_counter < 3:
        kick_ok = False
    
    else:
        kick_ok = True


    if a == "info:ver/upd/patn:tools":
        print(dev_tools)


    if b >= 0.25 and next_random_for_enemy >= 0.25 and a != "defend" and a != "stats" and a != "tutorial" and a != "info:ver/upd/patn:tools" and a != "" and kick_ok == True and a != "shop":
        enemy.punch(player)
        print(f'''
Player's health after punch: {player.hp}
------------------------------''')
        
    if b < 0.25 and next_random_for_enemy < 0.25 and a == "defend":
        exit


    if b < 0.25 and next_random_for_enemy < 0.25 and a != "defend" and a != "stats" and a != "tutorial" and a != "info:ver/upd/patn:tools" and a != "" and kick_ok == True and a != "shop":
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
a 25% Chance to hit you with their
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
    + Enter "shop" to open the shop
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
        print( Fore.GREEN + '''
          
******************************
            you win
******************************''')
        print(Style.RESET_ALL)
        
        

    if player.hp <= 0 and enemy.hp > 0:
        print( Fore.RED + '''
          
******************************
           you loose
******************************''')
        print(Style.RESET_ALL)
        
    
    if player.hp <= 0 and enemy.hp <= 0:
        print(f'''
******************************
  You both die! Nobody wins
******************************

''')
        
      
    next_random_for_enemy = random.random()
      
        
    if a == "shop":
        shop_active = True
        print(f'''
++++++++++++++++++++++++++++++++++
               SHOP        
               ¯¯¯¯
    Your Balance: {player.coins}🪙
    
  Items:  strength 🫙   (30🪙 )
          health 🫙     (50🪙 )
          vision 🎴     (100🪙 )
          
++++++++++++++++++++++++++++++++++
              ''')
        
        while shop_active == True:
            c = input()
            
            if c == "strength":
                shop.buy_strength_potion(1)
                
            if c == "health":
                shop.buy_health_potion(1)
                
            if c == "vision":
                shop.buy_vision_card(1)
                
            if c == "exit":
                shop_active = False
               
    
        
    
    while_counter += 1
    
        