import streamlit as st

def main():
    st.title("テキストをJSONに変換")
    col1, col2 = st.columns(2)

    with col1:
        input_text = st.text_area("入力テキストを入力してください")
        submit_button = st.button("変換ボタン")

    if submit_button:
        lines = input_text.split("\n")
        metadata = {
            "0枚目(plotid)": lines[0],
            "1枚目 表紙-タイトル(フック)": lines[1],
            "1枚目 表紙-タイトル(ベース)": lines[2],
            "2枚目(見出し)": lines[3],
            "2枚目(本文)": lines[4].replace("\n", "\\n"),
            "3枚目(見出し)": lines[5],
            "3枚目(本文)": lines[6].replace("\n", "\\n"),
            "4枚目(見出し)": lines[7],
            "4枚目(本文)": lines[8].replace("\n", "\\n"),
            "5枚目(見出し)": lines[9],
            "5枚目(本文)": lines[10].replace("\n", "\\n"),
            "6枚目(見出し)": lines[11],
            "6枚目(本文)": lines[12].replace("\n", "\\n"),
            "7枚目(見出し)": lines[13],
            "7枚目(本文)": lines[14].replace("\n", "\\n"),
            "8枚目(見出し)": lines[15],
            "8枚目(本文)": lines[16].replace("\n", "\\n"),
            "9枚目(見出し)": lines[17],
            "9枚目(本文)": lines[18].replace("\n", "\\n"),
            "10枚目(CTA画像)": lines[19],
            "CTA": lines[20]
        }

        with col2:
            st.json(metadata)

if __name__ == "__main__":
    main()
