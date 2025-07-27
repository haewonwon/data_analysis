import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("visitors.csv")

plt.rcParams['font.family'] = 'AppleGothic'

df.columns = df.columns.str.strip()

# 1월 ~ 12월 컬럼 목록
monthly_columns = ['1월', '2월', '3월', '4월', '5월', '6월',
                   '7월', '8월', '9월', '10월', '11월', '12월']

# 연도별 평균 이용자 수 계산
df['평균'] = df[monthly_columns].mean(axis=1)

# 시각화
plt.figure(figsize=(12, 6))  # 그래프 전체 크기 설정 (가로 12인치, 세로 6인치)
plt.bar(df['연도'].astype(str), df['평균'], color='yellow')  # 연도별 평균 이용자 수를 막대그래프로 그림

plt.title('연도별 인천아트플랫폼 평균 이용자 수', fontsize=14)  # 그래프 제목 설정
plt.xlabel('연도')  # x축 라벨 설정
plt.ylabel('평균 이용자 수')  # y축 라벨 설정
plt.xticks(rotation=45)  # x축 레이블(연도)을 45도 회전시켜서 겹치지 않게 표시
plt.grid(axis='y', linestyle='--', alpha=0.6)  # y축 방향에 점선 형태의 격자선 추가 (반투명)
plt.tight_layout()  # 그래프 레이아웃을 자동으로 정렬해서 요소들이 안 겹치게 정리
plt.show()  # 그래프를 화면에 출력