#!/usr/bin/env python
# coding: utf-8

# # <노인복지센터 현황 시각화 프로젝트> &#128214;
# 	
# 

# ## PART4. 추가 시각화
# ### 1) 미래 인구수 차트 

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc # rc == run configure(configuration file)


# In[4]:


# 파일 읽기
df = pd.read_excel('장래 인구수.xlsx', encoding='cp949') 
del df['시나리오별(1)']


# In[8]:


# NaN 값 삭제 후 '경기도' 위치 확인
df.dropna().head(10)


# In[9]:


# 경기도 데이터만 가져오기
df = df[171:190]
df.head(10)


# In[10]:


# 시도별 열 삭제
del df["시도별(1)"]


# In[11]:


# 열과 행 스위치
df = np.transpose(df)
df


# In[12]:


# 65+ 인구수만 가져오기
df = df[179]
df


# In[13]:


# 첫 행 삭제
df = df.drop(['인구구조, 부양비별(1)'])


# In[14]:


# 문자열 칼럼을 숫자로 바꾸기
df_179 = pd.to_numeric(df)


# In[15]:


# 데이터 프레임 이름 변경
df_179.name = '65+ 인구수'
df_179


# In[16]:


# 차트 만들기
plt.rcParams["font.family"] = 'Malgun Gothic'
plt.rcParams["font.size"] = 16
plt.rcParams["figure.figsize"] = (20, 10)


# In[17]:


df_179.plot(color='#ff0000')
plt.grid()
plt.legend()
plt.title("< 장래 인구수 >")
plt.xlabel("년도")
plt.ylabel("인구수")
plt.show()


# In[18]:


# Plotly 내장 데이터 활용 -> 인구수 추이 관찰
get_ipython().system('pip install plotly # plotly 설치')


# In[19]:


# 라이브러리 임포트
# plotly 내장 데이터 조회 api를 사용하여 한국의 기대수명 관련 샘플 데이터를 가져오기
# https://pypi.org/project/chart-studio/#description
get_ipython().system('pip install chart-studio')


# In[22]:


# 라이브러리 임포트
import chart_studio
chart_studio.tools.set_credentials_file(username='cherryy', api_key='p2T19zq5NrjdoI0jSHIg')
import chart_studio.plotly as py
import plotly.express as px


# In[23]:


# plotly 내장 데이터 조회 api를 사용하여 한국의 기대수명 관련 샘플 데이터를 가져오기
df2 = px.data.gapminder().query("country=='Korea, Rep.'")
fig = px.line(df2, x="year", y="lifeExp", title='Life expectancy in Korea, Rep.')
py.iplot(fig)


# ----------

# ### 2) 노인시설 지도화_히트맵표현

# In[ ]:


# Plotly를 활용한 HeatMap 
import pandas as pd
import plotly.express as px


# In[ ]:


# df_2 : 노인여가복지시설(경로당)
# 파일 읽기, 
df_2 = pd.read_csv('노인여가복지시설현황(경로당).csv', encoding='cp949',
                   index_col="설치일자",parse_dates=True)
df_2.head()


# In[81]:


# 2. mapbox로 지도 그리기

fig = px.scatter_mapbox(df_2, lat="WGS84위도", lon="WGS84경도",
                  hover_name="시설명", hover_data=["도로명 주소", "지번 주소"],
                  color_discrete_sequence=['limegreen'], size_max=15, zoom=7, height=400)

fig.update_layout(mapbox_style="open-street-map")

fig.show()


# In[82]:


# HeatMap 표현
# 지도에 기관 위치를 찍고, 기관별 이용회원수를 z축(컬러)으로 표현.

fig = px.density_mapbox(df_2, lat="WGS84위도", lon="WGS84경도", z ="이용회원수",
                 radius=10,  center=dict(lat=37.57, lon=127.11),
                   zoom=7.7, height=700)

fig.update_layout(mapbox_style="open-street-map")

fig.show()


# -----------

# In[ ]:




