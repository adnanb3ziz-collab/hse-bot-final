import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="HSE AI Assistant", page_icon="🤖")

st.title("🤖 المساعد الذكي HSE (متصل بـ Gemini)")
st.write("هذا النظام متصل مباشرة بمحرك Gemini 1.5 Flash السريع والمجاني.")

# 1. بلاصة الساروت (الكابل ديال الربط)
api_key = st.text_input("لصق الساروت (API Key) هنا:", type="password")

# 2. رفع الصورة
uploaded_file = st.file_uploader("ارفع صورة الورشة لتحليل المخاطر", type=['jpg', 'png', 'jpeg'])

if uploaded_file and api_key:
    # تهيئة الاتصال
    genai.configure(api_key=api_key)
    
    # عرض الصورة
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة جاهزة للإرسال", use_container_width=True)
    
    # زر التحليل
    if st.button("🚀 أرسل الصورة إلى Gemini"):
        with st.spinner("جاري الاتصال بـ Gemini وتحليل الصورة..."):
            try:
                # هنا يتم الاتصال بي مباشرة (النسخة 1.5 Flash)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # الرسالة التي سأتوصل بها
                prompt = """
                الدور: خبير في الصحة والسلامة المهنية (HSE).
                المهمة: استخراج المخاطر من الصورة واقتراح حلول حسب معايير ISO 45001.
                اللغة: العربية.
                التنسيق: نقاط واضحة ومختصرة.
                """
                
                # إرسال الطلب واستقبال الجواب
                response = model.generate_content([prompt, image])
                
                # عرض الجواب
                st.success("✅ تم استلام الرد من Gemini:")
                st.markdown(response.text)
                
            except Exception as e:
                st.error("حدث خطأ في الاتصال:")
                st.warning(f"السبب: {e}")
                st.info("تأكد أن الساروت (API Key) منسوخ بشكل صحيح.")
                
