# hero.py
from __future__ import print_function
from asyncio import current_task
from copyreg import constructor
from numbers import Integral
import random
from sqlite3 import IntegrityError
from telnetlib import WILL

class Hero:
  #   name: String
      starting_health: IntegrityError
      current_health: Integral


    # we know the name of our hero, so we assign it here
self.name = name
    # similarly, our starting health is passed in, just like name
self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
self.current_health = starting_health

*** Above this comment is the constructor/intializerwe wil create all of our methods for the hero class
***

def battle(self, opponent):
    ...current_task hero WILL take fighting the opponent here
     passed in.
    ...
    heroes_name = []
    heroes_name.append(self).name)
    heroes_name.append(opponent.name)

    winner=random.choice(heroes_name)
   for hero in heroes != winner
         loser =hero

    print(f'{winner} has detected {loser}')
       
    #TODO" Battle each hero untill a victor emerges
    #phases to Implement:
    #1) Randomly choose winner ,print the name of victor 
    # hint : Look into random library, more specifically the choice method 

    for hero in heroes:
          if hero !=winner:
              loser=winner 

print (f'{winner}has defeated{loser}

   
   

...
def battle(self, opponet): bv6cf
...Current hero will take turn fighting the opponent Hero
passed in
hero =[Hero
heroe.append(self.name)
heroes.append(.nameopponent)


winner =random,choice(heroes)