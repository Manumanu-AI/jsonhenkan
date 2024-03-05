import streamlit as st
import json

# テキストを解析してメタデータに変換する関数
def convert_text_to_metadata(text):
    # テキストを行に分割
    lines = text.split('\n')
    
    # メタデータ辞書の初期化
    metadata = {}
    
    # 現在のキーを追跡
    current_key = None
    
    for line in lines:
        if line.endswith(')') or line.endswith('画像') or "枚目" in line:
            # 新しいセクションの開始を検出
            current_key = line.strip()
            metadata[current_key] = ""  # 初期値として空文字列を設定
        elif current_key:
            # 現在のセクションにテキストを追加
            metadata[current_key] += line + "\\n"
    
    # 不要な改行の削除
    for key in metadata:
        metadata[key] = metadata[key].strip("\\n")
    
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
