import streamlit as st
import datetime

# הגדרות עמוד (אופציונלי)
st.set_page_config(page_title="האפליקציה שלי", layout="centered")

# הזרקת CSS ליישור לימין (RTL)
st.markdown("""
    <style>
    .main {
        direction: rtl;
        text-align: right;
    }
    div[st-desc- Wood] {
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("האפליקציה שלי 🚀")
st.subheader("ברוכים הבאים!")

# הצגת הודעות סטטוס בשורה אחת (לחיסכון במקום)
col1, col2 = st.columns(2)
with col1:
    st.success("✅ הפעולה הצליחה!")
    st.info("ℹ️ מידע כללי")
with col2:
    st.warning("⚠️ שים לב לנושא")
    st.error("❌ שגיאה במערכת")

st.divider() # קו מפריד ויזואלי

# קלט מהמשתמש
comment = st.text_area("הערות", height=100, placeholder="כתוב כאן משהו...")
date = st.date_input("בחר תאריך", datetime.date.today())

# כפתור לביצוע פעולה
if st.button("שמור נתונים"):
    st.balloons() # אפקט חגיגי
    st.write(f"### סיכום:")
    st.write(f"📅 **תאריך:** {date}")
    st.write(f"📝 **אורך ההערה:** {len(comment)} תווים")
