import streamlit as st
from research_agent import run_research

st.set_page_config(
    page_title="ResearchPilot AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(99,102,241,.12), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(14,165,233,.10), transparent 30%),
        #080b12;
    color: #f8fafc;
}
#MainMenu, footer { visibility: hidden; }
header { background: transparent !important; }
.block-container { max-width: 1200px; padding-top: 3rem; padding-bottom: 4rem; }

.hero { text-align: center; padding: 2rem 1rem 1rem; }
.hero-badge {
    display: inline-block; padding: 7px 14px; border-radius: 999px;
    background: rgba(99,102,241,.12); border: 1px solid rgba(129,140,248,.25);
    color: #a5b4fc; font-size: 13px; font-weight: 600; margin-bottom: 18px;
}
.hero-title {
    font-size: 56px; line-height: 1.05; font-weight: 800; letter-spacing: -2px; margin: 0;
    background: linear-gradient(90deg,#fff,#c7d2fe,#67e8f9);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-subtitle {
    max-width: 720px; margin: 20px auto 0; color: #94a3b8;
    font-size: 18px; line-height: 1.7;
}
.research-card, .report-container {
    background: rgba(15,23,42,.78); border: 1px solid rgba(148,163,184,.12);
    border-radius: 24px; padding: 28px; margin-top: 30px;
    box-shadow: 0 20px 60px rgba(0,0,0,.25);
}
.feature-card {
    background: rgba(15,23,42,.65); border: 1px solid rgba(148,163,184,.10);
    border-radius: 18px; padding: 22px; height: 100%;
}
.feature-icon { font-size: 28px; margin-bottom: 10px; }
.feature-title { font-weight: 700; color: #f8fafc; font-size: 16px; }
.feature-text { color: #94a3b8; font-size: 14px; line-height: 1.6; margin-top: 7px; }
.stButton > button {
    width: 100%; border-radius: 12px; border: 1px solid rgba(129,140,248,.3);
    padding: 12px 20px; font-weight: 700;
    background: linear-gradient(135deg,#6366f1,#0891b2); color: white;
}
textarea { border-radius: 14px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ AI-POWERED RESEARCH ENGINE</div>
    <h1 class="hero-title">ResearchPilot AI</h1>
    <p class="hero-subtitle">
        Turn a research topic into a structured, evidence-based report
        using autonomous web research and modern AI reasoning.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="research-card">', unsafe_allow_html=True)
st.markdown("### 🔎 What do you want to research?")

topic = st.text_area(
    "Research topic",
    placeholder="Example: The impact of artificial intelligence on cybersecurity in 2026",
    height=120,
    label_visibility="collapsed",
)

col1, col2 = st.columns([4, 1])
with col1:
    st.caption("Tip: Use a specific topic for more focused research.")
with col2:
    research_button = st.button("🚀 Research", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🌐</div>
        <div class="feature-title">Live Web Research</div>
        <div class="feature-text">Searches the web for relevant information instead of relying only on model knowledge.</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">AI Analysis</div>
        <div class="feature-text">Uses a CrewAI research agent powered by Groq's language models.</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📑</div>
        <div class="feature-title">Structured Reports</div>
        <div class="feature-text">Produces organized research with findings, analysis, conclusions, and sources.</div>
    </div>
    """, unsafe_allow_html=True)

if research_button:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
    else:
        with st.status("ResearchPilot is researching...", expanded=True) as status:
            try:
                st.write("🔎 Searching the web...")
                result = run_research(topic.strip())
                st.write("🧠 Analyzing relevant information...")
                st.write("📑 Preparing the research report...")
                status.update(label="Research completed successfully!", state="complete", expanded=False)
                st.session_state["research_result"] = str(result)
            except Exception as error:
                status.update(label="Research failed", state="error")
                st.error(f"Something went wrong:\n\n{error}")

if "research_result" in st.session_state:
    st.markdown('<div class="report-container">', unsafe_allow_html=True)
    st.markdown("## 📄 Research Report")
    st.download_button(
        "⬇️ Download Report",
        data=st.session_state["research_result"],
        file_name="research_report.md",
        mime="text/markdown",
    )
    st.markdown(st.session_state["research_result"])
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("ResearchPilot AI • Streamlit • CrewAI • DuckDuckGo • Groq")
