import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="HSE Pro", page_icon="✅")

st.title("✅ خبير السلامة (النسخة المستقرة)")
st.caption("يعمل بمحرك Gemini 1.5 Flash (سريع ومجاني)")

# إدخال المفتاح
api_key = st.text_input("لصق الساروت (API Key) هنا:", type="password")
uploaded_file = st.file_uploader("ارفع الصورة", type=['jpg', 'png', 'jpeg'])

if uploaded_file and api_key:
    genai.configure(api_key=api_key)
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة جاهزة", use_container_width=True)
    
    if st.button("🚀 تحليل"):
        with st.spinner("جاري التحليل..."):
            try:
                # رجعنا للموديل 1.5 دابا حيث نتا درتي التحديث للمكتبة
                # هذا الموديل عندو كوطة كبيرة ومستحيل يقوليك 429 دابا
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = "استخرج مخاطر السلامة HSE من الصورة واقترح حلولاً. اكتب بالعربية."
                
                response = model.generate_content([prompt, image])
                st.success("✅ تم التحليل بنجاح!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error("خطأ:")
                st.code(e)
                
