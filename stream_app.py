import streamlit as st
from datetime import datetime

def main():
    st.title("Display Date and Time")

    if st.button("Show Date and Time"):
        current_time = datetime.now().strftime("%Y年 %m月 %d日 %H:%M:%S")
        st.write("現在の日付と時刻:", current_time)

if __name__ == "__main__":
    main()