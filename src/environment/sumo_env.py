import gymnasium
from gymnasium import spaces
import numpy as np
import traci

class SUMOEnv(gymnasium.Env):
    def __init__(self, sumo_config_path, max_steps=1000):
        super(SUMOEnv, self).__init__()

        # SUMO configuration
        self.sumo_config_path = sumo_config_path
        self.max_steps = max_steps
        self.step_count = 0

        # Define action and observation spaces
        # Example: Discrete actions for traffic lights (e.g., 2 states: Green or Red)
        self.action_space = spaces.Discrete(2)

        # Observation space: Example includes vehicle count, average speed, etc.
        # Adjust the observation space based on your requirements
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(3,), dtype=np.float32)

    def reset(self):
        """Reset the simulation and return the initial observation."""
        try:
            traci.close()
        except traci.exceptions.TraCIException:
            # TraCI wasn't running, so no need to close
            pass

        try:
            traci.start(["sumo-gui", "-c", self.sumo_config_path])
        except Exception as e:
            raise RuntimeError(f"TraCI failed to start: {e}")
        self.step_count = 0

        # Initial observation
        return self._get_observation()

    def step(self, action):
        """Apply the action, advance the simulation, and return the new state, reward, and done flag."""
        # Apply action (example: control traffic light states, not implemented here)
        # Update your logic based on the nature of actions in your MARL setup

        traci.simulationStep()
        self.step_count += 1

        observation = self._get_observation()
        reward = self._compute_reward()
        done = self.step_count >= self.max_steps or traci.simulation.getMinExpectedNumber() == 0

        return observation, reward, done, {}

    def render(self, mode='human'):
        """Render the simulation (if applicable)."""
        pass  # SUMO's GUI can be used to visualize the simulation

    def close(self):
        """Close the environment and stop SUMO."""
        if traci.isRunning():
            traci.close()

    def _get_observation(self):
        """Retrieve the current state of the environment."""
        vehicle_ids = traci.vehicle.getIDList()
        avg_speed = np.mean([traci.vehicle.getSpeed(veh_id) for veh_id in vehicle_ids]) if vehicle_ids else 0
        vehicle_count = len(vehicle_ids)
        waiting_time = np.sum([traci.vehicle.getWaitingTime(veh_id) for veh_id in vehicle_ids])

        return np.array([vehicle_count, avg_speed, waiting_time], dtype=np.float32)

    def _compute_reward(self):
        """Compute the reward for the current state."""
        # Example: Minimize waiting time
        waiting_time = np.sum([traci.vehicle.getWaitingTime(veh_id) for veh_id in traci.vehicle.getIDList()])
        return -waiting_time  # Negative reward for higher waiting times
