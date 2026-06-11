import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="해양 생물 종 다양성 변화 분석",
    layout="wide"
)

# 제목
st.title("🌊 해양 생물 종 다양성 변화 원인 분석")

st.markdown("""
이 앱은 해양 생물 종 다양성 변화와 관련된 요인을 분석합니다.

분석 변수
- 해수면 온도(SST)
- 해양 pH
- 산호 백화 심각도
- 해양 열파 발생 여부
""")

# 데이터 불러오기
df = pd.read_csv("realistic_ocean_climate_dataset 2(1).csv")

# 데이터 확인
st.header("1. 데이터 미리보기")
st.dataframe(df.head())

# 기초 통계
st.header("2. 기초 통계")
st.dataframe(df.describe())

# 상관관계 분석
st.header("3. 생물 다양성에 영향을 주는 요인")

corr_sst = df["SST (°C)"].corr(df["Species Observed"])
corr_ph = df["pH Level"].corr(df["Species Observed"])
corr_bleach = df["Bleaching Severity"].corr(df["Species Observed"])

result = pd.DataFrame({
    "요인": [
        "해수면 온도(SST)",
        "pH",
        "산호 백화 심각도"
    ],
    "상관계수": [
        corr_sst,
        corr_ph,
        corr_bleach
    ]
})

st.dataframe(result)

# 수온과 생물종 수
st.header("4. 수온과 생물 다양성")

st.scatter_chart(
    df,
    x="SST (°C)",
    y="Species Observed"
)

# pH와 생물종 수
st.header("5. pH와 생물 다양성")

st.scatter_chart(
    df,
    x="pH Level",
    y="Species Observed"
)

# 산호 백화와 생물종 수
st.header("6. 산호 백화와 생물 다양성")

st.scatter_chart(
    df,
    x="Bleaching Severity",
    y="Species Observed"
)

# 해양 열파 분석
st.header("7. 해양 열파의 영향")

heatwave_avg = (
    df.groupby("Marine Heatwave")["Species Observed"]
    .mean()
)

st.bar_chart(heatwave_avg)

# 결론 자동 생성
st.header("8. 분석 결과")

strongest = result.iloc[
    result["상관계수"].abs().idxmax()
]

st.success(
    f"""
생물 종 수와 가장 강한 관계를 보인 요인은
'{strongest['요인']}' 입니다.

상관계수는 {strongest['상관계수']:.3f} 입니다.

데이터를 통해 해양 생물 다양성은
수온, pH, 산호 백화, 해양 열파와
관련이 있음을 확인할 수 있습니다.
"""
)

st.header("9. 탐구 결론")

st.write("""
해양 생물 종 다양성은 다양한 환경 요인의 영향을 받는다.

특히 수온 상승, pH 변화(해양 산성화),
산호 백화, 해양 열파는 생물 종 수 변화와
관련이 있는 것으로 나타났다.

따라서 기후 변화가 해양 생태계에 영향을
미칠 가능성이 있음을 확인할 수 있다.
""")
