import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="HSE Lite", page_icon="⚡")

st.title("⚡ خبير السلامة (النسخة الخفيفة)")
st.caption("نظام يعمل بمحرك Gemini 2.0 Flash Lite")

# إدخال المفتاح
api_key = st.text_input("لصق الساروت (API Key) هنا:", type="password")
uploaded_file = st.file_uploader("ارفع الصورة", type=['jpg', 'png', 'jpeg'])

if uploaded_file and api_key:
    genai.configure(api_key=api_key)
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة جاهزة", use_container_width=True)
    
    if st.button("🚀 تحليل"):
        with st.spinner("جاري الاتصال بالموديل الخفيف..."):
            try:
                # هنا درنا الموديل اللي كاين فاللائحة ديالك بالضبط
                model = genai.GenerativeModel('models/gemini-2.0-flash-lite-001')
                
                prompt = "استخرج مخاطر السلامة HSE من الصورة واقترح حلولاً. اكتب بالعربية."
                
                response = model.generate_content([prompt, image])
                st.success("✅ تم التحليل بنجاح!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error("حدث خطأ تقني:")
                st.code(e)
                st.info("إذا استمر الخطأ، جرب الضغط على 'Reboot' في Streamlit.")
                
