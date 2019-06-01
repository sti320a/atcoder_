state = 0b0000  # 初期状態

sleep = 0b0001  # 眠り
poison = 0b0010  # 毒
paralysis = 0b0100  # 麻痺
excitation = 0b1000  # 励起


# 眠り状態か判別
def isSleep(state):
    if state & 0b0001:
        return 'Sleep'
    else:
        return 'Not Sleep'


# 眠り状態にする
state = state | sleep
print(isSleep(state))

# 眠り状態を解く
state = state & ~ sleep
print(isSleep(state))
