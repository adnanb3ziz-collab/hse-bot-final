import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="HSE AI Expert", page_icon="🛡️")

# الواجهة
st.title("🛡️ خبير السلامة المهنية (AI Auditor)")
st.write("مساعد ذكي لتحليل مخاطر العمل ومخالفات ISO 45001")

# القائمة الجانبية للمفتاح
api_key = st.sidebar.text_input("🔑 Google API Key", type="password")

# زر رفع الصورة
uploaded_file = st.file_uploader("ارفع صورة للورشة أو الحالة غير الآمنة", type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    # عرض الصورة
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة قيد الفحص...", use_container_width=True)
    
    # التأكد من وجود المفتاح قبل التحليل
    if api_key:
        # إعداد الاتصال
        genai.configure(api_key=api_key)
        
        if st.button("🚀 ابدأ التحليل (Start Audit)"):
            with st.spinner("جاري استشارة خوارزميات السلامة..."):
                try:
                    # استخدام الموديل السريع
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    # التعليمات للخبير
                    prompt = """
                    Role: Senior HSE Auditor (ISO 45001 & Moroccan Labor Code).
                    Task: Analyze the image for safety hazards.
                    Language: Arabic (with technical terms).
                    
                    Report Structure:
                    1. 🚨 **المخاطر المرصودة**: (List hazards).
                    2. ⚖️ **المخالفة القانونية**: (Cite ISO 45001 clause or NM 00.5.801).
                    3. ✅ **الحل المقترح**: (Immediate action).
                    4. 🔥 **مستوى الخطورة**: (High/Medium/Low).
                    """
                    
                    # الحصول على النتيجة
                    response = model.generate_content([prompt, image])
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"حدث خطأ: {e}")
    else:
        st.warning("⚠️ المرجو إدخال كود API في القائمة الجانبية (يسار الشاشة) للبدء.")
      
