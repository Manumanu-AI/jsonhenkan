import streamlit as st
import re
import json

# Streamlitアプリのレイアウト設定
st.title('テキストからメタデータへの変換器')

# 2カラムのレイアウトを作成
col1, col2 = st.columns(2)

# col1にテキスト入力エリアを配置
with col1:
    st.write("以下にテキストを入力してください：")
    input_text = st.text_area("", height=300)

# 変換ボタン
if st.button('変換'):
    # 改行文字を\nに置換
    text = input_text.replace('\n', '\\n')

    # メタデータ辞書の初期化
    metadata = {
        "plot_id": "",
        "1枚目-表紙 (タイトル)": "",
        "2枚目(見出し)": "",
        "2枚目(本文)": "",
        "3枚目(見出し)": "",
        "3枚目(本文)": "",
        "4枚目(見出し)": "",
        "4枚目(本文)": "()",
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

    # テキストをセクションに分割
    sections = re.split(r'(\d+枚目[\s\S]*?)(?=\d+枚目|\Z)', text)

    # 各セクションを処理
    for section in sections:
        if section:
            # 枚数と内容を分離
            header, *content = section.split('\\n', 1)
            content = content[0] if content else ""
            
            # メタデータキーを生成
            key = header.replace(' ', '').replace('-', ' ')
            
            # メタデータ辞書に内容を追加
            if '見出し' in key or '表紙' in key:
                metadata[key] = content.replace('\\n', '\\\\n')
            else:
                metadata[key] = content.replace('\\n', '\\\\n')

    # メタデータをJSON形式の文字列に変換
    metadata_json = json.dumps(metadata, ensure_ascii=False, indent=2)

    # 変換されたメタデータをcol2に表示
    with col2:
        st.write("変換されたメタデータ：")
        # JSON文字列内の\\nを\nに置換して表示
        st.text_area("", value=metadata_json.replace('\\\\n', '\\n'), height=300)
