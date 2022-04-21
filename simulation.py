import time

from road import Road


def step(road, time_increment):
    vehicles = road.vehicles
    for index in range(len(vehicles) - 1):
        vehicles[index].update_speed(vehicles[index+1], time_increment)

    vehicles[len(vehicles) - 1].update_speed(vehicles[0], time_increment)
    road.update_pos()


road_obj = Road(100, 1, 10)
print(road_obj)

nb_step = 50
dt = 1

for i in range(nb_step):
    step(road_obj, dt)
    time.sleep(0.001)
    print(road_obj)
