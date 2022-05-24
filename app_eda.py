import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda() :
    df=pd.read_csv('data/review2.csv')
    df=df.drop('Unnamed: 0', axis=1)

    st.write(df.head())

    st.text('리뷰의 길이를 히스토그램 차트로 출력')
    fig1 = plt.figure()
    df['length'].hist()
    st.pyplot(fig1)

    st.text('리뷰의 길이가 가장 긴 데이터')
    st.write( df['length'].loc[ df['length'] == df['length'].max() ] )

    st.text('리뷰의 길이가 가장 짧은 데이터')
    st.write( df['length'].loc[ df['length'] == df['length'].min() ] )

    st.text('별점별로 리뷰가 몇개씩 있는지 시각화(내림차순)')
    sorted_data = df['stars'].value_counts().index
    fig1 = plt.figure()
    sns.countplot(data= df, x= 'stars', order= sorted_data )
    st.pyplot(fig1)

    selected = st.selectbox('선택', sorted(df['stars'].unique()))
    st.write(df.loc[ df['stars'] == selected, ['stars', 'text'] ])