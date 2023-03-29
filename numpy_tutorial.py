import pandas as pd
import numpy as np

tens_list = np.arange(start=0, stop=111, step=10)
# -> 배열: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

print(tens_list.shape)
# Result: (12,)
# 배열의 차원을 나타내는 튜플 반환

print(tens_list.ndim)
# Result: 1
# 배열의 차원을 정수로 출력

print(tens_list.size)
# Result: 12
# 배열의 요소 개수 반환

two_dim_tens_list = tens_list.reshape(4, 3)

print(two_dim_tens_list)
# 4*3 형태의 이차원배열 출력
# "parameter의 총곱 = 기존 배열의 element 개수"이어야 함

three_dim_tens_list = tens_list.reshape(2, 3, 2)
# 2*3*2 형태의 삼차원배열 출력

auto_tens_list = tens_list.reshape(2, -1)
# parameter로 '-1' 전달 시 자동으로 크기 계산함

print(np.random.randint(1, 10, [3, 5]))
# 2~9 사이의 3*5 난수 배열을 생성

print(np.random.randn(2, 4, 3))
# Z(표준정규분포)에서 생성된 값으로 2*4*3 삼차원배열 생성

"""
nan(not a number)

np.nan
-> nan

np.nan == 5
-> False

np.nan = np.nan
-> False
"""