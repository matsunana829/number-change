import streamlit as st

st.set_page_config(page_title="数字だけ変えたい！", layout="wide")
st.title("数字だけ変えたい！")
st.markdown("""
使い方

①自分のTEI/XMLのsurface内を以下にコピペする（現在は例文が入力されています）

②各種idのコマ数の部分（canbas/12 や 00012.tif など）を`{num}` または `{num:05d}`（五桁）にする

③「数字の範囲」で示したコマ数の分だけ、変更したsurfaceが生成できます

""")

# テンプレート入力
template = st.text_area("テンプレート：", value="""<surface lry=\"3455\" lrx=\"4920\" uly=\"285\" ulx=\"810\"
         sameAs=\"https://kokusho.nijl.ac.jp/biblio/200023857/canvas/{num}\">
         <graphic
            url=\"https://kokusho.nijl.ac.jp/api/iiif/200023857/v4/NIKI/015-0641/015-0641-{num:05d}.tif/full/full/0/default.jpg\"
            width=\"5616px\" height=\"3744px\"
            sameAs=\"https://kokusho.nijl.ac.jp/api/iiif/200023857/v4/NIKI/015-0641/015-0641-{num:05d}.tif\"/>
</surface>""", height=200)

col1, col2 = st.columns(2)
with col1:
    num_start = st.number_input("数字の開始：", min_value=0, value=1, step=1)
with col2:
    num_end = st.number_input("数字の終了：", min_value=0, value=5, step=1)

if st.button("生成"):
    results = []
    template_lines = template.strip().splitlines()
    for num in range(num_start, num_end + 1):
        for line in template_lines:
            try:
                results.append(line.format(num=num))
            except Exception as e:
                results.append(f"[エラー] {str(e)}")
        results.append("")  # 空行で区切り

    output = "\n".join(results)
    st.text_area("生成された結果：", value=output, height=300)
    st.download_button("📄 結果をテキストでダウンロード", output, file_name="output.txt")
