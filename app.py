from colorama import Fore, Back, Style 

super_dmg = 50
punch_coin_reward = 10
kick_coin_reward = 20
while_counter = 0
sps_price = 30
hps_price = 50
vcs_price = 100
shop_active = False
health_potion_buff = 30
strength_potion_buff = 5
restart_first_fight = False



print(f'''
/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/

WARNING!!!

Please watch put for spaces at the 
end of your inputs as this will 
lead to unexpected errors! Please 
make sure to only use potions/card
outside of the shop!

/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/
      ''')




dev_tools = '''
/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-//*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/

Version: 1.0.13 (earlier access)

Patch Notes (20.06.24; 13:19):

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
    +  added Shop 
    +  added potions/cards
    +  added more colors
    +  improved "stats"
    +  improved Warning
    +  'respawn' added
    +  fixed bug in 'stats'
    +  fixed coins bug
    +  respawn after draw fixed

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
        self.dmg += strength_potion_buff
        start_shop.sps -= 1
        
    def hps_use(self):
        self.hp += health_potion_buff
        start_shop.hps -= 1
        
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
        start_shop.vcs -= 1
        
    
    def respawn(self):
        self.hp = 100
        self.dmg = 10
        self.coins = 20
        start_shop.player_respawn()
        start_enemy.player_respawn()


        









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
        
    def player_respawn(self):
        self.hp = 100
        self.dmg = 10
        self.coins = 20
        
        







class Shop():
    
    def __init__(self, sps, hps, vcs):
        self.sps = sps  #sps = S trength  P otion  S upply
        self.hps = hps  #hps = H ealth    P otion  S upply
        self.vcs = vcs  #vcs = V ision    C ard    S upply


    def buy_strength_potion(self, sps):
        if player.coins >= sps_price:
            player.coins -= sps_price
            self.sps += 1
            print(Fore.GREEN  + f'''
------------------------------
       Potion bought! ✅
------------------------------               
                  ''')
            print( Style.RESET_ALL)
            return self.sps
        else:  
            print(Fore.RED  + f'''
------------------------------
     Not enough Coins! 🪙
------------------------------               
                  ''')
            print( Style.RESET_ALL)
    
    
    def buy_health_potion(self, hps):
        if player.coins >= hps_price:
            player.coins -= hps_price
            self.hps += 1
            print(Fore.GREEN  + f'''
------------------------------
       Potion bought! ✅
------------------------------               
                  ''')
            print( Style.RESET_ALL)
            return self.hps
        
        else:  
            print(Fore.RED  + f'''
------------------------------
     Not enough Coins! 🪙
------------------------------               
                  ''')
            print( Style.RESET_ALL)
    

    def buy_vision_card(self, vcs):     #vc reveals "var: next_random_for_enemy"    (still need to remove commas and display action name instead of random number)
        if player.coins >= vcs_price:
            player.coins -= vcs_price
            self.vcs += 1
            print(Fore.GREEN  + f'''
------------------------------
        Card bought! ✅
------------------------------               
                  ''')
            print( Style.RESET_ALL)  
            return self.vcs
        else:  
            print(Fore.RED  + f'''
------------------------------
     Not enough Coins! 🪙
------------------------------               
                  ''')
            print( Style.RESET_ALL)   
            
    
    def player_respawn(self):
        self.sps = 0
        self.hps = 0
        self.vcs = 0
                                 











player = Player(100, 10, 20)
start_enemy = Enemy(100, 10, 20)
start_shop = Shop(0, 0, 0)








while start_enemy.hp > 0 and player.hp > 0 or restart_first_fight == True:
    a = input()
    if while_counter == 0:
        b = random.random()
        next_random_for_enemy = b
        
    b = next_random_for_enemy

    if restart_first_fight == True:
        player.respawn()
        restart_first_fight = False
        print(Fore.LIGHTGREEN_EX + f'''
------------------------------
   Successfully respawned
------------------------------              
''')
        print(Style.RESET_ALL)
        

    if a == "kick" and punch_counter < 3:
        kick_ok = False
    
    else:
        kick_ok = True


    if a == "info:ver/upd/patn:tools":
        print(dev_tools)


    if b >= 0.25 and next_random_for_enemy >= 0.25 and a != "defend" and a != "stats" and a != "tutorial" and a != "info:ver/upd/patn:tools" and a != "" and kick_ok == True and a != "shop" and a != "use health" and a != "use strength" and a != "use vision card":
        start_enemy.punch(player)
        print(f'''
Player's health after punch: {player.hp}
------------------------------''')
        
    if b < 0.25 and next_random_for_enemy < 0.25 and a == "defend":
        exit


    if b < 0.25 and next_random_for_enemy < 0.25 and a != "defend" and a != "stats" and a != "tutorial" and a != "info:ver/upd/patn:tools" and a != "" and kick_ok == True and a != "shop" and a != "use health" and a != "use strength" and a != "use vision card":
        player.super(start_enemy.dmg)

    if a == "punch":
        player.punch(start_enemy)
        punch_counter += 1
        player.coins += punch_coin_reward
        print(f'''
Enemy's health after punch: {start_enemy.hp}
------------------------------''')
        

    if a == "defend":
        player.defend()
        print(f'''
Player's health after defending: {player.hp}
------------------------------''')
        
        
    if a == "stats":
        print(Fore.CYAN + f''' 
------------------------------
Player HP: {player.hp}❤️   DMG: {player.dmg}⚔️    Coins: {player.coins}🪙    Health: {start_shop.hps}🫙    Strength: {start_shop.sps}🫙    Vision Cards: {start_shop.vcs}🎴
Enemy  HP: {start_enemy.hp}❤️    DMG: {start_enemy.dmg}⚔️     Coins: {start_enemy.coins}🪙    

Punch Counter: {punch_counter}      
------------------------------''')
        print( Style.RESET_ALL)
        
        
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
    + Enter "respwan" to respawn after loose
------------------------------------------------------------              
              ''')
     
     
    if a == "kick" and punch_counter < 3:
        print( Fore.RED + f'''
------------------------------
    You can not kick yet!
------------------------------
''')
        print( Style.RESET_ALL)
       
     
     
        
    if a == "kick" and punch_counter >= 3:
        player.kick(start_enemy)
        player.coins += kick_coin_reward
        punch_counter -= 1
        print(f'''
Enemy's health after kick: {start_enemy.hp}
------------------------------''') 
        
        
        
        
    if start_enemy.hp <= 0 and player.hp > 0:
        print( Fore.GREEN + '''
          
******************************
           you win 🏆
******************************''')
        print(Style.RESET_ALL)
        
        

    if player.hp <= 0 and start_enemy.hp > 0:
        print( Fore.RED + '''
          
******************************
           you loose!
 enter "respawn" to try again
******************************''')
        print(Style.RESET_ALL)
        restart_first_fight_request = input()
        if restart_first_fight_request == "respawn":
            punch_counter = 0
            restart_first_fight = True
            print(Fore.LIGHTGREEN_EX + f'''
------------------------------
   Successfully respawned
------------------------------              
''')
        print(Style.RESET_ALL)
            
        
    
    if player.hp <= 0 and start_enemy.hp <= 0:
        print( Fore.LIGHTYELLOW_EX + f'''
******************************
  You both die! Nobody wins
 enter "respawn" to try again
******************************

''')
        print(Style.RESET_ALL)
        if restart_first_fight_request == "respawn":
            punch_counter = 0
            restart_first_fight = True
            print(Fore.LIGHTGREEN_EX + f'''
------------------------------
   Successfully respawned
------------------------------              
''')
        print(Style.RESET_ALL)
        
      
    next_random_for_enemy = random.random()
      
        
    if a == "shop":
        shop_active = True
        print( Fore.LIGHTMAGENTA_EX + '''
          
******************************
          Shop entered
******************************''')
        print(Style.RESET_ALL)
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
                start_shop.buy_strength_potion(1)
                
            if c == "health":
                start_shop.buy_health_potion(1)
                
            if c == "vision":
                start_shop.buy_vision_card(1)
                
            if c == "exit":
                shop_active = False
                print( Fore.LIGHTMAGENTA_EX + '''
          
******************************
          Shop exited
******************************''')
        print(Style.RESET_ALL)
     
     
        
        
    if a == "use strength" and start_shop.sps < 1:
        print( Fore.LIGHTRED_EX + '''
          
******************************
      No Strength Potion 
******************************''')
        print(Style.RESET_ALL)
        
    if a == "use strength" and start_shop.sps >= 1:
        print( Fore.LIGHTGREEN_EX + '''
          
******************************
     Strength Potion used
******************************''')
        print(Style.RESET_ALL)
        player.sps_use()
    
           
           
           
           
    if a == "use health" and start_shop.hps < 1:
        print( Fore.LIGHTRED_EX + '''
          
******************************
     No Health Potion 
******************************''')
        print(Style.RESET_ALL)
               
    if a == "use health" and start_shop.hps >= 1:
        print( Fore.LIGHTGREEN_EX + '''
          
******************************
      Health Potion used
******************************''')
        print(Style.RESET_ALL)
        player.hps_use()
        
        
        
        
    if a == "use vision card" and start_shop.vcs < 1:
        print( Fore.LIGHTRED_EX + '''
          
******************************
        No Vision Card
******************************''')
        print(Style.RESET_ALL)
        
    if a == "use vision card" and start_shop.vcs >= 1:
        print( Fore.LIGHTGREEN_EX + '''
          
******************************
       Vision Card used
******************************''')
        print(Style.RESET_ALL)
        player.vcs_use()
        

    
    while_counter += 1