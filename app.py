import streamlit as st # type: ignore

from dotenv import load_dotenv # type: ignore

load_dotenv()

st.title("コーディネーター: 質問に応じた提案を行います")

st.write("##### 動作モード1: 旅行コーディネーター")
st.write("旅行先を入力し、動作モードを選択し、「実行」ボタンを押すことでおすすめの観光地３つを提案します。")
st.write("##### 動作モード2: 服装コーディネーター")
st.write("服装の種類を入力し、動作モードを選択し、「実行」ボタンを押すことでおすすめの服装コーディネート３つを提案します。")

input_message = st.text_input(label="調べたいことがらのテキストを入力してください。")

text_count = input_message

selected_item = st.radio(
    "動作モードを選択してください。",
    ["旅行コーディネーター", "服装コーディネーター"]
)

if st.button("実行"):
    if selected_item == "服装コーディネーター":
        
        from langchain_openai import ChatOpenAI # type: ignore
        from langchain.schema import SystemMessage, HumanMessage # type: ignore
        llm =ChatOpenAI(model_name = "gpt-4o-mini",temperature=0.5)
        message =[
            SystemMessage(content="あなたは優秀な服装コーディネーターです"),
            HumanMessage(content=f"{text_count}について、おすすめの服装コーディネートを3つ提案してください。")
        ]
        result = llm(message)
    else:
        from langchain_openai import ChatOpenAI # type: ignore
        from langchain.schema import SystemMessage, HumanMessage # type: ignore
        llm =ChatOpenAI(model_name = "gpt-4o-mini",temperature=0.5)
        message =[
            SystemMessage(content="あなたは優秀な旅行コーディネーターです"),
            HumanMessage(content=f"{text_count}について、おすすめの観光地を3つ提案してください。")
        ]
        result = llm(message)

    st.write(result.content)