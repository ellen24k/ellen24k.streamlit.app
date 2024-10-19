

import streamlit as st

st.title("리다이렉트 예제")

if st.button("네이버로 이동"):
    st.markdown('<a href="https://www.naver.com" target="_self">네이버로 이동</a>', unsafe_allow_html=True)

# st.write("ellen24k")
# st.write("3초 후에 네이버로 이동합니다...")
