import numpy as np
import pandas as pd

# index_col: 인덱스가 될 column 선택
pokemon = pd.read_csv("pokemon.csv", encoding='CP949', index_col="Name")

# head(), tail(): Check rows from first/last
pokemon.head(5)
pokemon.tail(5)

# dtypes(): Check datatypes of each column
pokemon.dtypes

# iloc[index]: extract a row 
pokemon.iloc[1]

# loc[""]: extract row(s) with corresponding data
pokemon.loc["아르세우스"]

# sort_values(by=""): column 값으로 정렬
# ascending: 오름차순 여부
pokemon.sort_values(by="Name", ascending=False)

# sort_index(): 이름 순으로 정렬
pokemon.sort_index().head()


"""예) 가장 많은 포켓몬이 새로 나온 세대는?"""
# value.counts()
pokemon["Gen"].value_counts().head(10)

"""예) 3세대 포켓몬만 필터링하려면?"""
# 변수에 필터링 조건을 저장
gen_3 = (pokemon["Gen"]==3)
pokemon[gen_3]

"""예) 4세대 포켓몬도 같이 필터링하려면?"""
# '|' 사용
gen_4 = (pokemon["Gen"]==4)
pokemon[ gen_3 | gen_4 ]

"""예) 특공이 130 이상인 포켓몬만 필터링하려면?"""
# 부등호를 필터링 조건에 사용
C_130 = (pokemon["C"]>=130)
pokemon[C_130]

"""예) 공격이 120~140 사이인 포켓몬만 필터링하려면?"""
# between(,) 사용
A_120_to_140 = pokemon["A"].between(120, 141)
pokemon[A_120_to_140].sort_values(by="A", ascending=False)

"""메가진화한 포켓몬을 모두 찾으려면?"""
# contains("")
mega_evol = pokemon.index.str.contains("메가")
pokemon[mega_evol]

"""찾아 바꾸기 기능"""
# .str.replace("", "", regex=False)

"""그룹화"""
# groupby()
generations = pokemon.groupby("Gen")

print(generations["Gen"].count().sort_values(ascending=False))

print(generations["Total"].mean().sort_values(ascending=False))