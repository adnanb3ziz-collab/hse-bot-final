import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="HSE AI Free", page_icon="🛡️")

st.title("🛡️ خبير السلامة (النسخة المجانية)")
st.caption("يعمل بموديل Gemini 2.0 Experimental (بدون قيود)")

# إدخال المفتاح
api_key = st.sidebar.text_input("🔑 Google API Key", type="password")

# رفع الصورة
uploaded_file = st.file_uploader("ارفع صورة الورشة", type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة جاهزة", use_container_width=True)
    
    if api_key:
        genai.configure(api_key=api_key)
        
        if st.button("🚀 تحليل فوري"):
            with st.spinner("جاري التحليل..."):
                try:
                    # هنا التغيير: اخترنا الموديل التجريبي المجاني من لائحتك
                    model = genai.GenerativeModel('models/gemini-2.0-flash-exp')
                    
                    prompt = """
                    Role: HSE Auditor. 
                    Output Language: Arabic.
                    Task: Identify safety hazards and cite ISO 45001.
                    Structure:
                    1. 🚨 المخاطر.
                    2. ⚖️ القانون/ISO.
                    3. ✅ الحل.
                    """
                    
                    response = model.generate_content([prompt, image])
                    st.markdown(response.text)
                    st.success("✅ تم التحليل بنجاح (وضع مجاني)")
                    
                except Exception as e:
                    # إذا فشل، نجرب الموديل الخفيف جداً كاحتياط
                    try:
                        model = genai.GenerativeModel('models/gemini-2.0-flash-lite-001')
                        response = model.generate_content([prompt, image])
                        st.markdown(response.text)
                    except:
                        st.error("⚠️ يبدو أن السيرفر مشغول جداً، حاول مرة أخرى بعد دقيقة.")
                        
