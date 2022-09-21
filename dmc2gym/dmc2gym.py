from time import time
from gym import spaces
from dm_env import StepType

class DMC2Gym:
    """Convert a DMC environment to a Gym environment"""

    def __init__(self, dmc_env):
        """Initializes a new DMC2Gym wrapper

        Args:
            dmc_env (DMCEnv): The DMC environment to convert.
        """
        dmc_obs_spec = dmc_env.observation_spec()
        self._observation_space = spaces.Box(
            shape=dmc_obs_spec.shape,
            dtype=dmc_obs_spec.dtype,
            low=dmc_obs_spec.low,
            high=dmc_obs_spec.high
        )
        dmc_act_spec = dmc_env.action_spec()
        self._action_space = spaces.Box(
            shape=dmc_act_spec.shape,
            dtype=dmc_act_spec.dtype,
            low=dmc_act_spec.low,
            high=dmc_act_spec.high
        )
        self._dmc_env = dmc_env

    def step(self, action):
        time_step = self._dmc_env.step(action)
        obs = time_step.observation
        reward = time_step.reward
        discount = time_step.discount
        if time_step.last():
            done = True
        else:
            done = False
        return obs, reward, done, {'discount': discount}

    def reset(self):
        time_step = self._dmc_env.reset()
        return time_step.observation

    def render(self):
        return self._dmc_env.render()

    @property
    def observation_space(self):
        return self._observation_space

    @property
    def action_space(self):
        return self._action_space
