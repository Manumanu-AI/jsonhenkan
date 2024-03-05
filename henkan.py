import streamlit as st
import re
import json

def convert_to_metadata(input_text):
    # テキストの改行を直接 \n として扱う
    # JSONでのエスケープは json.dumps が適切に行う

    # メタデータ辞書の初期化
    metadata = {
        "plot_id": "",
        # 他のキーも同様に初期化
    }

    # テキストをセクションに分割する正規表現を調整
    sections = re.split(r'(\d+枚目.*?)(?=\d+枚目|$)', input_text, flags=re.DOTALL)

    for section in sections:
        if section.strip():
            # セクションの見出しと本文を分割
            parts = section.split('\n', 2)
            if len(parts) >= 2:
                key = parts[0].strip().replace(' ', '').replace('-', ' ')
                content = parts[1].strip()
                # \n で改行を区切る
                metadata[key] = content.replace('\n', '\\n')
    
    return metadata

st.title('テキストからメタデータへの変換器')

# 2カラムのレイアウトを作成
col1, col2 = st.columns(2)

# col1にテキスト入力エリアを配置
with col1:
    st.write("以下にテキストを入力してください：")
    input_text = st.text_area("", height=300)

# 変換ボタン
if st.button('変換'):
    # 変換処理を実行
    metadata = convert_to_metadata(input_text)

    # 変換されたメタデータをcol2に表示
    with col2:
        st.write("変換されたメタデータ：")
        st.text_area("", value=json.dumps(metadata, ensure_ascii=False, indent=2), height=300)
