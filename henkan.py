import streamlit as st
import json

def text_to_json(input_text):
    lines = input_text.split('\n')
    metadata = {
        "plot_id": lines[0].split(')')[1].strip(),
        "1枚目-表紙 (タイトル)": lines[1].split(')')[1].strip() + " - " + lines[2].split(')')[1].strip(),
    }
    for i in range(2, len(lines), 2):
        if i < len(lines) - 1:
            heading = lines[i].split(')')[0].replace('枚目', '枚目(見出し)').strip()
            content = lines[i].split(')')[1].strip() + "\n" + lines[i+1].strip()
            metadata[heading] = content.replace('\n', '\\n')

    return metadata

# Streamlit UI
st.title('テキストをJSONに変換')

with st.form("my_form"):
    col1, col2 = st.columns(2)

    with col1:
        user_input = st.text_area("テキストを入力してください", height=300)

    with col2:
        st.write("変換結果 (JSON)")

    submitted = st.form_submit_button("変換ボタン")

    if submitted:
        json_data = text_to_json(user_input)
        with col2:
            st.json(json_data)
