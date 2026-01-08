import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="HSE AI Expert", page_icon="🛡️")

# العنوان
st.title("🛡️ خبير السلامة المهنية (AI Auditor)")
st.caption("يعمل بمحرك Gemini 2.0 Flash (الجيل الجديد)")

# القائمة الجانبية للمفتاح
api_key = st.sidebar.text_input("🔑 Google API Key", type="password")

# رفع الصورة
uploaded_file = st.file_uploader("ارفع صورة الورشة أو الخطر", type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    # عرض الصورة
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة قيد الفحص...", use_container_width=True)
    
    if api_key:
        genai.configure(api_key=api_key)
        
        if st.button("🚀 ابدأ التحليل (Start Audit)"):
            with st.spinner("جاري تحليل المخاطر بأحدث تقنيات الذكاء الاصطناعي..."):
                try:
                    # هنا التغيير الحاسم: استخدمنا الموديل اللي لقينا فاللائحة ديالك
                    model = genai.GenerativeModel('models/gemini-2.0-flash')
                    
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
                    st.success("✅ تم التحليل بنجاح باستخدام Gemini 2.0")
                    
                except Exception as e:
                    st.error(f"حدث خطأ: {e}")
                    st.info("جرب موديل آخر من القائمة إذا استمر المشكل.")
    else:
        st.warning("⚠️ المرجو إدخال كود API في القائمة الجانبية للبدء.")
        
