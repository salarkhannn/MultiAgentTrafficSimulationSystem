import traci

traci.start(["sumo", "-c", "src/karachi/osm.sumocfg"])
step = 0
while step < 1000:
    traci.simulationStep()
    step+=1
traci.close()