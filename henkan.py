import streamlit as st

def convert_text_to_json(text):
   lines = text.strip().split('\n')
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
       "9枚目(本文)": ""
   }

   for line in lines:
       if line.startswith('0枚目(plotid)'):
           metadata["plot_id"] = line.replace('0枚目(plotid)', '').strip()
       elif line.startswith('1枚目 表紙-タイトル(フック)'):
           metadata["1枚目-表紙 (タイトル)"] = line.replace('1枚目 表紙-タイトル(フック)', '').strip()
       elif line.startswith('1枚目 表紙-タイトル(ベース)'):
           metadata["1枚目-表紙 (タイトル)"] += " " + line.replace('1枚目 表紙-タイトル(ベース)', '').strip()
       elif line.startswith('2枚目(見出し)'):
           metadata["2枚目(見出し)"] = line.replace('2枚目(見出し)', '').strip()
       elif line.startswith('2枚目(本文)'):
           metadata["2枚目(本文)"] = line.replace('2枚目(本文)', '').strip().replace('\n', '\\n')
       elif line.startswith('3枚目(見出し)'):
           metadata["3枚目(見出し)"] = line.replace('3枚目(見出し)', '').strip()
       elif line.startswith('3枚目(本文)'):
           metadata["3枚目(本文)"] = line.replace('3枚目(本文)', '').strip().replace('\n', '\\n')
       # ... and so on for other keys

   return metadata

def main():
   st.set_page_config(page_title="Text to JSON Converter", layout="wide")

   col1, col2 = st.columns(2)

   with col1:
       text = st.text_area("Enter text here:")
       if st.button("Convert"):
           metadata = convert_text_to_json(text)
           col2.json(metadata)

   with col2:
       st.write("JSON data will appear here after conversion.")

if __name__ == "__main__":
   main()
