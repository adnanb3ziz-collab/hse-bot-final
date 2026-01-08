import streamlit as st
import google.generativeai as genai

st.title("🛠️ فحص الموديلات (System Check)")

# 1. عرض نسخة المكتبة (باش نعرفو واش المشكل فالتحديث)
try:
    ver = genai.__version__
    st.info(f"📚 نسخة المكتبة المثبتة: {ver}")
    # إذا كانت أقل من 0.4.0 راه ماغاديش تخدم Gemini
except:
    st.error("❌ لا يمكن تحديد نسخة المكتبة!")

# 2. إدخال المفتاح
api_key = st.text_input("🔑 دخل الساروت (API Key) باش نشوفو اللائحة:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    if st.button("📋 اعرض اللائحة (Call ListModels)"):
        st.write("جاري الاتصال بسيرفر Google...")
        try:
            # هادي هي الدالة اللي طلب منك الميساج ديرها
            models = genai.list_models()
            
            found_any = False
            st.write("### الموديلات المتوفرة لحسابك:")
            
            for m in models:
                # قلب ليا غير على الموديلات اللي كتولد المحتوى
                if 'generateContent' in m.supported_generation_methods:
                    st.success(f"✅ الموديل: `{m.name}`")
                    found_any = True
            
            if not found_any:
                st.warning("⚠️ الساروت خدام، ولكن ما لقينا حتا موديل متوافق!")
                
        except Exception as e:
            st.error(f"❌ حدث خطأ أثناء جلب اللائحة: {e}")
            st.warning("تأكد أن الساروت صحيح وأنك مفعل Generative Language API فالموقع.")
            
