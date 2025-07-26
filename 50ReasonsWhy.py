import streamlit as st
import time

# Set page configuration
st.set_page_config(
    page_title="💌 50 Reasons Why Yatakshi is the Most Special Person",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------------
# Custom CSS: Romantic Theme + Fade
# -----------------------------------
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .title {
        text-align: center;
        font-size: 2.5rem;
        font-family: 'Georgia', cursive;
        color: #d63384;
        margin-bottom: 20px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    .card {
        background-color: #ffe6f0;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        text-align: center;
        font-size: 1.4rem;
        font-family: 'Georgia', cursive;
        color: #5c3c52;
        line-height: 1.8;
        opacity: 0;
        animation: fadeIn 0.7s ease-in-out forwards;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------
# Emoji-Rich 50 Reasons for Yatakshi
# -----------------------------------
reasons = [
    "😂✨ Your laughter doesn’t just sound nice — it changes the atmosphere. It’s like joy in its purest form.",
    "👂💖 The way you truly listen makes people feel like they matter — like they’ve finally found their person.",
    "🌸💞 Your kindness doesn’t feel like a habit — it feels like a natural extension of who you are.",
    "👁️🌼 You notice the beauty in things others rush past. That’s a kind of magic most people don’t have.",
    "💬✨ When you talk about what you love, your eyes sparkle, and I could watch them forever.",
    "🧠💫 You remember things most people forget, and that makes people feel cherished — like their soul is seen.",
    "🚪🌷 You don’t just enter a room. You bring warmth, peace, and something inexplicably comforting.",
    "💗👑 You somehow make everyone feel like the most important person — and it’s not even an act. It’s just you.",
    "🤝🌍 Your care for others is so genuine — it restores something broken in the world.",
    "😊🌞 Your smile feels like something the sun would be jealous of — it’s that radiant.",
    "🌱🔥 You have this quiet hope inside you that never gives up — and that’s so rare.",
    "🎨🌈 Your creativity doesn’t just impress — it inspires, uplifts, and makes people believe in color again.",
    "🦁🌟 You’re braver than you know — and I wish you could see yourself the way others do.",
    "🤗🫶 Being around you feels like a hug no one wants to leave.",
    "😄🎭 Your sense of humor is so perfectly you — gentle, clever, never cruel, always needed.",
    "🏡📝 Conversations with you feel like home — safe, real, unforgettable.",
    "💘🛡️ You love your people with a kind of loyalty that’s rare and absolutely beautiful.",
    "🌠👣 You make others want to be better — not because you ask, but because of how you are.",
    "🪞🔥 You never fake it. Your authenticity is quietly bold, and people admire it more than they say.",
    "📜🌌 Your advice feels like it comes from a soul that’s lived a hundred lives.",
    "🔍🎠 You’re curious about the world like it’s a playground — and that curiosity is contagious.",
    "🌪️🕊️ You handle chaos with a kind of grace that makes people believe things will be okay.",
    "🪶📩 You do small things that make huge impacts and probably never even realize it.",
    "🌬️🤍 People feel safe around you — like they can exhale, be messy, and still be accepted.",
    "🎥🖌️ Watching you chase your dreams is like watching art in motion.",
    "🌟❤️‍🩹 You find goodness where others stop looking — that says so much about your heart.",
    "🗣️🪷 Your voice has this calmness that could pull someone back from the edge.",
    "🫱🫲💓 You bring out the gentlest, most human parts in everyone you meet.",
    "🎁🧸 You give people room to breathe when they’re overwhelmed, and love when they need it most.",
    "🌃🎇 Your joy, when you're really happy — could light up an entire skyline.",
    "🧠💡 You’re brilliant — not just book-smart, but people smart, heart-smart. It’s incredible.",
    "👁️‍🗨️🌺 You don’t just make people feel seen. You make them feel worth seeing.",
    "🌍🚀 Your adventurous spirit makes life feel bigger, better, and full of possibility.",
    "👯🌈 The way you care about your friends makes them feel like the luckiest people alive.",
    "💪🧘 Even when things are hard, you carry a kind of strength that doesn’t demand attention — but deserves all of it.",
    "🧺📸 You can turn the most ordinary day into something worth remembering.",
    "🫶💗 You don’t just feel for others — you feel with them. That’s real compassion.",
    "🎉🪞 You celebrate others with such honesty, it reminds them they’re worth celebrating.",
    "🧠📚 The way you think? It’s beautiful. Insightful, rare, layered like a book people want to keep reading.",
    "📆🎀 You take regular moments and turn them into memories just by being in them.",
    "🔥🎯 You don’t quit on what you love — that’s powerful.",
    "⏳💝 Even when you’re busy, you make time. That speaks volumes about your heart.",
    "📖🕊️ You read emotions like poetry — gently, with understanding.",
    "🔥🧣 Being around you is like sitting beside a fire on a cold day — warm, quiet, healing.",
    "🪨🌄 You fall, but you rise. And when you rise, it’s always a little brighter than before.",
    "🌾🍃 You don’t need grand things to be happy — and that joy in simplicity is beautiful.",
    "🎭🤍 You’re honest — not brutally, but beautifully. It builds trust in a world full of masks.",
    "🕯️🙌 You believe in people, sometimes more than they believe in themselves — and that faith changes lives.",
    "🚪🎆 You walk into someone’s life and suddenly, without warning, it starts feeling more alive.",
    "💖🌸 And maybe the most special thing? You just being you is more than enough to make someone fall without ever saying a word."
]

# -----------------------------------
# State Initialization
# -----------------------------------
if "index" not in st.session_state:
    st.session_state.index = 0

# -----------------------------------
# Title
# -----------------------------------
st.markdown('<div class="title">💌 50 Reasons Why Yatakshi is the Most Special Person</div>', unsafe_allow_html=True)

# -----------------------------------
# Flashcard Display with Animation
# -----------------------------------
st.markdown(f'<div class="card">{reasons[st.session_state.index]}</div>', unsafe_allow_html=True)

# -----------------------------------
# Navigation Buttons with Unique Keys
# -----------------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️ Previous", key="prev_btn", use_container_width=True):
        st.session_state.index = (st.session_state.index - 1) % len(reasons)
        time.sleep(0.1)  # to retrigger animation

with col3:
    if st.button("Next ➡️", key="next_btn", use_container_width=True):
        st.session_state.index = (st.session_state.index + 1) % len(reasons)
        time.sleep(0.1)

# -----------------------------------
# Footer
# -----------------------------------
st.markdown(
    "<br><center><sub>Made with 💗 for My Laadli (Beloved) Yatakshi.</sub></center>",
    unsafe_allow_html=True
)
