from gymnasium.wrappers import RecordVideo
import gymnasium as gym
env_name = 'MountainCar-v0'
env = gym.make(env_name, render_mode="human")
# env = RecordVideo(env, video_folder="./video/", name_prefix=f"{env_name}")
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
    env.close()
