from stable_baselines3.common.env_checker import check_env
from minesweeperenv import MinesweeperEnv


env = MinesweeperEnv(render_mode=None)
# It will check your custom environment and output additional warnings if needed
check_env(env)