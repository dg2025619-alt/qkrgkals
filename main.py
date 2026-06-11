import streamlit as st
import pandas as pd
import os

st.title("🌊 해양 생물 다양성 분석")

st.write("현재 폴더 파일 목록")
st.write(os.listdir())

csv_file = None

for file in os.listdir():
    if file.endswith(".csv"):
        csv_file = file
        break

if csv_file is None:
    st.error("CSV 파일을 찾을 수 없습니다.")
    st.stop()

st.success(f"찾은 CSV 파일: {csv_file}")

df = pd.read_csv(csv_file)

st.write("데이터 미리보기")
st.dataframe(df.head())

st.write("컬럼 목록")
st.write(df.columns.tolist())
