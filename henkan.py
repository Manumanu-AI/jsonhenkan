import streamlit as st
import json

# Streamlitアプリのレイアウトを定義
st.title('テキストをJSONに変換')
col1, col2 = st.columns(2)

with col1:
    st.header("テキスト入力")
    # テキストエリアを用意し、ユーザーからの入力を受け取る
    input_text = st.text_area("こちらにテキストを入力してください:", height=300)
    # 変換ボタン
    convert_button = st.button("変換")

# 変換ロジック
def convert_to_json(input_text):
    lines = input_text.split('\n')
    metadata = {
        "plot_id": "",
        "1枚目-表紙-タイトル(フック)": "",
        "1枚目-表紙-タイトル(ベース)": "",
        "2枚目(見出し)": "",
        "2枚目(本文)": "",
        "3枚目(見出し)": "",
        "3枚目(本文)": "",
        "4枚目(見出し)": "",
        "4枚目(本文)": "",
        "5枚目(見出し)": "",
        "5枚目(本文)": "",
        "6枚目(見出し)": "",
        "6枚目(本文)": "",
        "7枚目(見出し)": "",
        "7枚目(本文)": "",
        "8枚目(見出し)": "",
        "8枚目(本文)": "",
        "9枚目(見出し)": "",
        "9枚目(本文)": "",
    }

    # テキストを解析してmetadataに格納
    for line in lines:
        parts = line.split(')')
        if len(parts) > 1:
            key, value = parts[0], ')'.join(parts[1:]).strip()
            if '枚目' in key:
                section, label = key.split('枚目')
                section = section + '枚目'
                if '表紙-タイトル(フック)' in label:
                    metadata["1枚目-表紙-タイトル(フック)"] = value
                elif '表紙-タイトル(ベース)' in label:
                    metadata["1枚目-表紙-タイトル(ベース)"] = value
                else:
                    metadata[section + label] = value.replace('\n', '\\n')
            elif '枚目(plotid' in key:
                metadata["plot_id"] = value

    return metadata

if convert_button:
    # テキストをJSONに変換
    json_data = convert_to_json(input_text)
    # col2にJSONデータを表示
    with col2:
        st.header("JSONデータ")
        st.json(json_data)
