import streamlit as st
import random

st.title("✊✋✌️ 가위바위보 게임")

choices = ["가위", "바위", "보"]
user_choice = st.radio("당신의 선택은?", choices)

if st.button("결과 확인"):
    computer_choice = random.choice(choices)

    st.write(f"당신의 선택: **{user_choice}**")
    st.write(f"컴퓨터의 선택: **{computer_choice}**")

    # 승패 판단
    if user_choice == computer_choice:
        result = "비겼습니다!"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "당신이 이겼습니다! 🎉"
    else:
        result = "컴퓨터가 이겼습니다. 😢"

    st.subheader(result)
