import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bikes.csv")

# 한글 깨짐 방지
plt.rcParams['font.family'] = 'AppleGothic'

plt.plot(df["날짜"], df["이용자수"], marker='o')
plt.title("날짜별 자전거 이용자 수")
plt.xlabel("날짜")
plt.ylabel("이용자 수")
plt.grid(True)
plt.tight_layout()
plt.show()