import traci

def get_vehicle_data(vehicle_id):
    return {
        "speed": traci.vehicle.getSpeed(vehicle_id),
        "waiting_time": traci.vehicle.getWaitingTime(vehicle_id),
    }
