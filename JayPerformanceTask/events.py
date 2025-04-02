from random import randint


def whirlpool(my_ship):
  print(
      "Oh no, your ship got pulled into a whirlpool, and it is slowly damaging your hull!"
  )
  hull_damage = randint(2, 8)
  if my_ship.hull <= 10:
    print(
        "Your hull is critically low, and you are unable to escape the whirlpool"
    )
  print("You have been damaged by the whirlpool")
  my_ship.hull -= hull_damage
  my_ship.morale -= 5
  print(
      f"You have lost {hull_damage} hull, and your morale has decreased by 5")
  print(f" Current hull: {my_ship.hull}")
  print(f" Current morale: {my_ship.morale}")


def pirates(my_ship):
  print(
      "Pirates have attacked your ship, and it is slowly damaging your hull! They have robbed you of your food and coin too!"
  )
  if my_ship.defense <= 70:
    print(
        "Your defense is high, and you were able to defend against the pirates!, you lost nothing!"
    )
  else:
    hull_damage = randint(2, 8)
    my_ship.hull -= hull_damage
    my_ship.morale -= 5
    my_ship.coin -= 20
    my_ship.food -= 20
    print(
        f"You have lost {hull_damage}, 20 coin, 20 food, and your morale has decreased by 5"
    )


def shark(my_ship):
  print(
      "You're crewmate spots a fin in the water, you assure him it just an orca passing by, but you take a closer look and its a megeladon (A prehistoric shark that no one has seen before, its double the size of your ship!!"
  )
  print("It attacks you, and takes a huge chunk of your hull with it!")
  hull_damage = randint(10, 15)
  my_ship.hull -= hull_damage
  print(f"You have lost {hull_damage} hull")


def storm(my_ship):
  choice = input(
      "you see a storm coming, do you want to evade(e) and lose a couple of miles or go through the storm(l)?"
  )
  if choice == "e":
    print(
        "You evade the storm, and manage to escape the storm, you lose a few miles since you had to go through a different route"
    )
    my_ship.morale -= 5
    my_ship.food -= 5
  else:
    print(
        "You go through the storm, fighting the harsh rain. It degrades your hull and ruins some of the food aboard"
    )
    my_ship.food -= 10
    my_ship.hull -= 8


def island(my_ship):
  print(
      "Your crewmate says Land ahoy!, you rush to the deck and see an island filled with resources, you decide to explore it!"
  )
  choice = input(" Do you want to Explore(e) or just keep on going (k)?")
  if choice == "e" or "E":
    print(
        "You explore the island and find a huge chest of gold, food, and other supplies!"
    )
    my_ship.coin += randint(20, 30)
    my_ship.food += randint(6, 8)
    my_ship.morale += 5
    my_ship.hull += randint(10, 20)
    my_ship.food += randint(6, 8)
    print("You also got resources to fix your hull!")
  else:
    print(
        "You decide to keep on going, and you end up missing out on loot! I think you know what you are going to do teh next time you find an island!"
    )
    my_ship.morale -= 5
    my_ship.food -= 5


def nothing(my_ship):
  print("Nothing eventfull happened today. Phew!")
  my_ship.miles += randint(2, 8)
  food_ate = randint(3, 10)
  my_ship.food -= food_ate
  morale_gained = randint(3, 10)
  my_ship.morale += morale_gained
  print(f"You have gained {morale_gained} morale")


def enemy(my_ship):
  print("You have encountered an enemy ship!")
  choice = input("Do you want to attack(a) or try to negotiate(n)?")
  if choice == "a" or "A":
    print("You attack the enemy ship, and it dies!")
    my_ship.morale += randint(10, 20)
    my_ship.hull -= randint(10, 20)
    my_ship.food -= randint(10, 20)
    my_ship.coin -= randint(10, 20)
  else:
    print(
        "You try to negotiate with the enemy ship, but it ends up attacking you!"
    )
    my_ship.morale -= randint(5, 15)
    my_ship.hull -= randint(5, 15)
    my_ship.food -= randint(10, 20)
    my_ship.coin -= randint(10, 20)


def hurricane(my_ship):
  print(
      "You're crewmate spots a hurricane in the ocean, you decide to try to evade it!"
  )
  choice = input("Do you want to evade(e) or try to fight(f)?")
  if choice == "e" or "E":
    print(
        "You evade the hurricane, and you end up saving your crewmates!, but you got pushed off your original route and are lost a few miles"
    )
    my_ship.morale += randint(10, 20)
    my_ship.miles -= randint(4, 10)
  else:
    print(
        "You try to fight the hurricane, but it ends up pushing you off your original route and you are lost a few miles"
    )
    my_ship.morale -= randint(5, 15)
    my_ship.miles -= randint(4, 10)


def island2(my_ship):
  print(
      "Your crewmate says Land ahoy!, you rush to the deck and see an island filled with resources, you decide to explore it!"
  )
  choice = input(" Do you want to Explore(e) or just keep on going (k)?")
  if choice == "e" or "E":
    print(
        "You choose to get a search party and explore the island, but the island belonged to a gang of pirates!, and tehy robbed you of your food and money!"
    )
    my_ship.morale -= randint(10, 20)
    my_ship.food -= randint(5, 10)
    my_ship.coin -= randint(15, 20)
  else:
    print(
        "You decide to keep on going, and good job you did!, that island belonged to a bunch of pirates!"
    )
    my_ship.morale += randint(5, 10)
    my_ship.food -= randint(5, 10)


def foeorfriend(my_ship):
  print(
      "You see a ship on the water, waving a flag of truce. They want to tavel with you! Do you take the risk?"
  )
  choice = input(" press y for yes and n for no")
  if choice == "y" or "Y":
    print(
        "You decide to take the risk, and they gave you resources to aid you on your journey!"
    )
    my_ship.morale += randint(10, 20)
    my_ship.food += randint(4, 10)
    my_ship.coin += randint(5, 10)
    my_ship.hull += randint(5, 15)
  else:
    print("You decide to not take the risk, and they decide to attack you!")
    my_ship.morale -= randint(5, 10)
    my_ship.food -= randint(5, 10)
    my_ship.coin -= randint(15, 20)


events_list = [
    whirlpool, pirates, shark, storm, island, nothing, enemy, hurricane,
    island2, foeorfriend
]
