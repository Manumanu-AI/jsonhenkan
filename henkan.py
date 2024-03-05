import streamlit as st
import re
import json

# テキストを解析してメタデータに変換する関数
def convert_text_to_metadata(text):
    # 改行文字を\nに置換
    text = text.replace('\n', '\\n')
    
    # メタデータ辞書の初期化
    metadata = {}
    
    # テキストをセクションに分割
    sections = re.split(r'(\d+枚目[\s\S]*?)(?=\d+枚目|\Z)', text)
    for section in sections:
        if section:
            # 枚数と内容を分離
            header, *content = section.split('\n', 1)
            content = content[0] if content else ""
            
            # メタデータキーを生成
            key = header.replace(' ', '').replace('-', ' ')
            
            # メタデータ辞書に内容を追加
            if '見出し' in key or '表紙' in key:
                metadata[key] = content.replace('\\n', '')
            else:
                metadata[key] = content
    
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
