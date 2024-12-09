from environment.sumo_env import SUMOEnv
from models.train_model import train_rl_agent

env = SUMOEnv(config_file="karachi/osm.sumocfg")
train_rl_agent(env)