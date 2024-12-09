import gymnasium
from gymnasium import spaces
import traci

class SUMOEnv(gymnasium.Env):
    def __init__(self):
        super(SUMOEnv, self).__init__()
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=0, high=100, shape=(1,), dtype=float)

    def reset(self):
        traci.load(["-c", "osm.sumocfg"])
        return [0]
    
    def step(self, action):
        if action == 0:
            traci.vehicle.setSpeed("veh0", 10)
        else:
            traci.vehicle.setSpeed("veh0", 5)
        traci.simulationStep()

        reward = -traci.vehicle.getWaitingTime("veh0")
        done = traci.simulation.getMinExpectedNumber() == 0
        observation = [traci.vehicle.getSpeed("veh0")]

        return observation, reward, done, {}

    def close(self):
        traci.close()
