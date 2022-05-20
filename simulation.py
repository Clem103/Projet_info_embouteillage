import time

from road import Road


def step(road: Road, time_increment: float) -> None:
    """
    Plays one step of the simulation with the given road and time increment.

    :param road: Road object where the vehicles are stored
    :param time_increment: Time increment (dt) for the simulation. For the current model, anything below 0.5s leads to a static solution (no traffic jam)
    :return: Nothing
    :author: Clément Vellu

    """
    vehicles = road.vehicles
    for index in range(len(vehicles) - 1):
        vehicles[index].update_speed(vehicles[index+1], time_increment)

    vehicles[len(vehicles) - 1].update_speed(vehicles[0], time_increment)
    road.update_pos()


if __name__ == '__main__':

    road_obj = Road(200, 1, 10)
    print(road_obj)

    nb_step = 1000
    dt = 0.5    # Due to the model, any time step below 0.5s leads to a static solution (with no more evolution)

    for i in range(nb_step):
        step(road_obj, dt)
        time.sleep(0.01)
        print(road_obj)

    input("Press any key to continue")
