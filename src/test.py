import traci

traci.start(["sumo-gui", "--no-warnings", "-c", "src/IJP-road/osm.sumocfg"])
step = 0
while step < 1000:
    traci.simulationStep()
    step+=1
for vehicle_id in traci.vehicle.getIDList():
    speed = traci.vehicle.getSpeed(vehicle_id)
    print(f"Vehicle {vehicle_id} speed: {speed} m/s")

    route = traci.vehicle.getRoute(vehicle_id)
    print(f"Vehicle {vehicle_id} route: {route}")

    waiting_time = traci.vehicle.getWaitingTime(vehicle_id)
    print(f"Vehicle {vehicle_id} waiting time: {waiting_time} seconds")

traci.close()

