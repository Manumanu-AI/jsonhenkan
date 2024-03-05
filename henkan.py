import streamlit as st
import json
import re

# メタデータを生成する関数
def generate_metadata(text):
    # テキストの前処理: このステップでは特に改行の扱いを変更する必要はなし
    processed_text = text
    
    # メタデータ辞書の初期化
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
    
    # プロットIDの抽出
    plot_id_match = re.search(r'0枚目\(plotid\)\n(.*?)\n', processed_text)
    if plot_id_match:
        metadata["plot_id"] = plot_id_match.group(1)
    
    # 各セクションの情報を抽出してメタデータに追加
    sections = re.split(r'(\d+枚目[\s\S]*?)(?=\d+枚目|\Z)', processed_text)
    for section in sections:
        if section:
            header, *content = section.split('\n', 1)
            content = content[0] if content else ""
            key = re.sub(r'(\d+)枚目', r'\1枚目-', header).strip().replace(' ', '-')
            if '見出し' in key or '表紙' in key or 'CTA画像' in key:
                metadata[key] = content
            else:
                metadata[key] = content
    
    return json.dumps(metadata, ensure_ascii=False, indent=2).replace('\\n', '\n')

# Streamlit UI
st.title('テキストからメタデータ(JSON)への変換')

# テキスト入力エリア
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        input_text = st.text_area("テキストをここに貼り付けてください", height=300)
    with col2:
        output_text = st.empty()

# 変換ボタン
if st.button('変換'):
    # メタデータの生成と表示
    metadata_json = generate_metadata(input_text)
    output_text.text_area("変換されたメタデータ", metadata_json, height=300, key="output")
