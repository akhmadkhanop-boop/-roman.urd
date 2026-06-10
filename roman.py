import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🌐 Roman Urdu Translator")
st.write("English aur Roman Urdu ke beech translate karo!")

# Direction choose karo
direction = st.selectbox(
    "Kis taraf translate karna hai?",
    ["English → Roman Urdu", "Roman Urdu → English"]
)

# Tone choose karo
tone = st.selectbox("Tone:", ["Casual", "Formal", "Business"])

# Input
text = st.text_area("Apna text yahan likho:", height=200)

if st.button("Translate Karo"):
    if text:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=500,
            messages=[
                {
                    "role": "system",
                    "content": f"Tum ek expert translator ho. Direction: {direction}. Tone: {tone}. Sirf translation do, faltu baat nahi. Roman Urdu mein sahi spelling use karo."
                },
                {
                    "role": "user",
                    "content": f"Translate karo: {text}"
                }
            ]
        )
        translation = response.choices[0].message.content
        st.write("### Translation:")
        st.write(translation)
    else:
        st.write("⚠️ Pehle text likho!")