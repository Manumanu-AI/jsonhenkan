import streamlit as st
import json
import re

# アプリのレイアウトを定義
st.title('テキストからJSONメタデータへの変換器')

# 2カラムレイアウト
col1, col2 = st.columns(2)

# 左側のカラムでテキスト入力
with col1:
    st.header("テキスト入力")
    input_text = st.text_area("ここにテキストを貼り付けてください", height=300)

# 右側のカラムで結果表示
with col2:
    st.header("変換結果 (JSON)")

# ボタンを押したときの動作
if st.button('変換'):
    # テキストを処理してメタデータ辞書を作成
    metadata = {
        "plot_id": "",
        "1枚目-表紙 (タイトル)": "",
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
    
    # テキストをセクションごとに分割し、メタデータ辞書を更新
    sections = re.split(r'(\d+枚目[\s\S]*?)(?=\d+枚目|\Z)', input_text)
    for section in sections:
        if section:
            header, *content = section.split('\n', 1)
            content = content[0] if content else ""
            key = header.strip().replace(' ', '').replace('-', ' ')
            if '見出し' in key or '表紙' in key:
                metadata[key] = content.replace('\\n', '')
            else:
                metadata[key] = content
    
    # JSON形式で結果を表示
    st.text_area("JSON", json.dumps(metadata, ensure_ascii=False, indent=2), height=300)
