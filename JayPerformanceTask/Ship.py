from random import randint, choice
from math import floor
from events import events_list


class Ship:

  def __init__(self, name):
    self.name = name
    self.food = 100
    self.hull = 100
    self.miles = 0
    self.morale = 100
    self.cycle = 0
    self.coin = 40
    self.defense = randint(50, 100)

  def is_alive(self):
    return self.food > 0 and self.hull > 0 and self.morale > 0 and self.coin > 0

  def print_stats(self):
    header = f"Cycle {self.cycle}"
    print("=" * 40)
    print(f"{header:^40s}")
    print("=" * 40)
    print(f"    Miles {self.miles:5d}    Food {self.food:5d}")
    print(f"    Morale {self.morale:5d}   Money {self.coin:4d}")
    print(f"      Hull {self.hull:5d}   Defense {self.defense:4d}")
    print("=" * 40)

  def calc_resources(self):
    travel_distance = randint(2, 8)
    food_consumed = floor(travel_distance * 2)
    self.miles += travel_distance
    self.food -= food_consumed
    return {"travel_dist": travel_distance, "food_consumed": food_consumed}

  def random_event(self):
    choice(events_list)(self)
