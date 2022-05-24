import string
import streamlit as st
import pandas as pd
from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
my_stopwords = stopwords.words('english')

def message_cleaning(sentence) :
  # 1. 구두점 제거
  Test_punc_removed = [char for char in sentence if char not in string.punctuation]
  # 2. join 으로 문자열 합치기
  Test_punc_removed_join = ''.join(Test_punc_removed)
  # 3. 불용어 확인 후 제거
  Test_punc_removed_join_clean = [word for word in Test_punc_removed_join.split() if word.lower() not in my_stopwords]
  # 4. 결과값 반환
  return Test_punc_removed_join_clean

def main() :
    st.title('리뷰 긍정 부정 예측 앱')

    menu = ['Home', 'EDA', 'Machine Learning']
    choice = st.sidebar.selectbox('메뉴 선택', menu)
    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()

if __name__ == '__main__' :
    main()

# 파이썬 가상환경 확인
# 이 앱은 구글 코랩에서 만든 환경과 동일
# 파이썬 가상환경을 streamlit 3.7로 변경
# vs code의 가상환경 맞춰 변경