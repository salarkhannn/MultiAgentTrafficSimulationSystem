from environment.sumo_env import SUMOEnv
from models.train_model import train_rl_agent
from environment.utils import get_vehicle_data
import os

def test_environment():
    print("Testing SUMO environment initialization...")
    config_path = "src/karachi/osm.sumocfg"
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"SUMO config file not found at {config_path}")
    
    env = SUMOEnv(sumo_config_path=config_path)
    state = env.reset()
    print(f"Initial State: {state}")
    print("Environment initialized successfully")

def test_utils():
    print("Testing utitlity functions...")
    sample_vehicle_id = "veh0"
    vehicle_data = get_vehicle_data(sample_vehicle_id)
    print(f"Vehicle data for {sample_vehicle_id}: {vehicle_data}")
    print(f"Utility functions are working correctly.")

def test_training():
    print("Testing RL agent training...")
    config_path = "src/karachi/osm.sumocfg"
    env = SUMOEnv(sumo_config_path=config_path)
    try:
        train_rl_agent(env)
        print("Training script executed without errors.")
    except Exception as e:
        print(f"Training failed with error: {e}")

if __name__ == "__main__":
    print("Running project tests...")
    try:
        test_environment()
        test_utils()
        test_training()
        print("All tests passed")
    except Exception as e:
        print(f"Test failed with error: {e}")