from Ship import Ship
import time


def play_game():
  global my_ship
  time.sleep(1)
  print("The year is 1475")
  time.sleep(1)
  print()
  print("Its a sunny day in Greece, and the wind is just right")
  time.sleep(1)
  print()
  print("The perfect day to set sail")
  time.sleep(1)
  print()
  print(
      "hullo captain, Your ship is ready to embark on a 100 mile voyage across the pacific ocean to find the end of the world, and all the riches that may await you. What is the ships name again?"
  )
  print()
  shipName = input("What is your ships name?:")
  print()
  my_ship = Ship(shipName)
  print(
      f"right, the {shipName}. lets set sail Captain!, Hurry up now!, we dont want to leave you behind since you are in charge of everything from now on!"
  )

  while my_ship.miles < 50 and my_ship.is_alive():
    
    print()
    my_ship.cycle += 1
    my_ship.print_stats()
    print()
    my_ship.random_event()

    consumed = my_ship.calc_resources()
    print()
    print(
        f":: In this cycle, {my_ship.name} covered {consumed['travel_dist']} miles, and used {consumed['food_consumed']} food"
    )
    input("Press enter to continue")

  if my_ship.is_alive():
    print()
    print("Congratulations, you have reached the end of the world")
    print()
    print(
        "You have survived to the end of the world, and you have earned the title of hero of the century"
    )
    print(f" And you have only done it in {my_ship.cycle} cycles")
  else:
    print()
    print(
        f"You have lost the fight, and the ship has crashed into the ocean. the {my_ship.name} will sink to the bottom of the ocean and stay there for the rest of eternity"
    )


play_game()
