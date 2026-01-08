import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="HSE Final Bot", page_icon="🛡️")

st.header("🛡️ نظام تحليل المخاطر (النسخة النهائية)")

# 1. إدخال المفتاح
api_key = st.text_input("نسخ ولصق كود Google API Key هنا:", type="password")

# 2. رفع الصورة
uploaded_file = st.file_uploader("اختر صورة", type=['jpg', 'png', 'jpeg'])

if uploaded_file and api_key:
    # إظهار الصورة
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة جاهزة", use_container_width=True)
    
    # تهيئة Google
    genai.configure(api_key=api_key)
    
    if st.button("🚀 تحليل نهائي"):
        with st.spinner("جاري الاتصال..."):
            status_box = st.empty()
            
            # المحاولة 1: الموديل السريع
            try:
                status_box.text("جاري تجربة الموديل السريع (Flash)...")
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(["استخرج مخاطر السلامة من الصورة (ISO 45001) بالعربية.", image])
                st.success("✅ تم التحليل بنجاح (Flash)!")
                st.markdown(response.text)
                
            except Exception as e_flash:
                # المحاولة 2: الموديل القديم (احتياطي)
                try:
                    status_box.text("الموديل الأول فشل، جاري تجربة الموديل الاحتياطي (Pro Vision)...")
                    model = genai.GenerativeModel('gemini-pro-vision')
                    response = model.generate_content(["Analyze safety hazards in Arabic", image])
                    st.success("✅ تم التحليل بنجاح (Legacy Mode)!")
                    st.markdown(response.text)
                    
                except Exception as e_final:
                    # إذا فشل كل شيء
                    st.error("❌ فشلت جميع المحاولات. الخطأ هو:")
                    st.code(f"Error 1: {e_flash}\nError 2: {e_final}")
                    st.warning("تأكد أن المفتاح (API Key) صالح وأنك قمت بتفعيله في Google AI Studio.")
                    
