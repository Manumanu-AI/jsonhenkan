import streamlit as st
import json

# テキストを解析してメタデータに変換する関数
def convert_text_to_metadata(text):
    # 各行に分割
    lines = text.split('\n')
    
    # メタデータ辞書の初期化
    metadata = {}
    current_key = None
    current_value = ""
    
    for line in lines:
        # セクションのヘッダーを検出
        if "枚目" in line or "CTA画像" in line:
            # 前のセクションの内容を保存
            if current_key:
                metadata[current_key] = current_value.rstrip("\\n")
            # 新しいセクションのキーとして設定
            current_key = line.strip()
            current_value = ""
        else:
            # 現在のセクションの内容に追加
            current_value += line.replace('\n', '\\n') + "\\n"
    
    # 最後のセクションを辞書に追加
    if current_key and current_value:
        metadata[current_key] = current_value.rstrip("\\n")
    
    return json.dumps(metadata, ensure_ascii=False, indent=2)

# Streamlitインターフェース
st.title('テキストからメタデータへの変換ツール')

# ユーザー入力
user_input = st.text_area("ここにテキストをコピペしてください", height=300)

if st.button('変換'):
    # テキストをメタデータに変換
    metadata = convert_text_to_metadata(user_input)
    
    # 結果を表示
    st.text_area("変換されたメタデータ", metadata, height=300)
