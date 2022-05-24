import numpy as np
import streamlit as st
import joblib

def run_ml() :
  vec = joblib.load('data/vec.pkl')
  classifier = joblib.load('data/classifier.pkl')
  sentence = st.text_input('문장 입력')
  st.subheader('문장을 입력하면, 긍정/부정을 예측해준다.')

  if st.button('예측 실행') :
    new_data = np.array([sentence])
    X_new = vec.transform(new_data)
    X_new.toarray()
    y_pred = classifier.predict(X_new)
    st.write('입력하신 리뷰는 5점 만점에 ', str(y_pred[0]), '점입니다.' )
    if y_pred[0] == 5:
      st.text('입력하신 문장은 긍정적입니다.')
    else :
      st.text('입력하신 문장은 부정적입니다.')