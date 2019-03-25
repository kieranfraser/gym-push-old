from gym.envs.registration import register

register(
    id='push-v0',
    entry_point='gym_push.envs:PushEnv',
)
register(
    id='push-v1',
    entry_point='gym_push.envs:PushEnv1',
)
register(
    id='push_eval_1-v0',
    entry_point='gym_push.envs:PushEval1',
)