import streamlit as st
from pypdf import PdfReader
import pandas as pd
import os

# ===== Custom Theme and Setup =====
st.set_page_config(
    page_title="AI Resume Scanner Pro",
    page_icon="📄",
    layout="wide"
)

# Custom CSS for professional look
st.markdown("""
<style>
    .stApp {
        background: #f5f9ff;
    }
    .css-1v0mbdj {
        border-radius: 10px;
    }
    .st-b7 {
        background-color: #2e86de !important;
    }
    .st-c0 {
        background-color: #e6f0ff;
    }
</style>
""", unsafe_allow_html=True)

# ===== 1. Header Section =====
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/1570/1570887.png", width=100)
with col2:
    st.title("AI Resume Scanner Pro")
    st.caption("Powered by NLP • v2.0")

# ===== 2. File Upload =====
with st.expander("📤 Upload Resume", expanded=True):
    uploaded_file = st.file_uploader(
        "Drag and drop your resume (PDF only)",
        type="pdf",
        label_visibility="collapsed"
    )

# ===== 3. Load Job Data =====
@st.cache_data
def load_jobs():
    try:
        jobs = pd.read_csv("jobs.csv")
        # Convert required_skills to list if they're strings
        if isinstance(jobs.iloc[0]['required_skills'], str):
            jobs['required_skills'] = jobs['required_skills'].apply(lambda x: [s.strip() for s in x.split(',')])
        return jobs
    except Exception as e:
        st.error(f"Error loading jobs.csv: {e}")
        return pd.DataFrame(columns=['title', 'company', 'required_skills'])

jobs_df = load_jobs()

# ===== 4. Processing Section =====
if uploaded_file:
    with st.spinner("Analyzing resume..."):
        try:
            # PDF Processing
            reader = PdfReader(uploaded_file)
            text = " ".join([page.extract_text() for page in reader.pages])
            
            # Simple skill detection (replace with proper NLP if needed)
            detected_skills = []
            for skill in ['Python', 'SQL', 'Machine Learning', 'Java', 'AWS']:
                if skill.lower() in text.lower():
                    detected_skills.append(skill)
            
            # Success Message
            st.success(f"""
            ✅ Analysis Complete!  
            Detected skills: {', '.join(detected_skills) if detected_skills else 'No skills detected'}
            """)
            
            # ===== 5. Results Dashboard =====
            tab1, tab2, tab3 = st.tabs(["📊 Matching Jobs", "🔍 Skills Analysis", "📝 Resume Text"])
            
            with tab1:
                if not jobs_df.empty:
                    # Calculate matches
                    jobs_df['match_score'] = jobs_df['required_skills'].apply(
                        lambda skills: sum(1 for skill in skills if skill in detected_skills) / max(1, len(skills)) * 100
                    )
                    
                    # Show top matches
                    top_jobs = jobs_df.sort_values('match_score', ascending=False).head(10)
                    
                    st.dataframe(
                        top_jobs[['title', 'company', 'match_score']],
                        use_container_width=True,
                        hide_index=True,
                        column_config={
                            "match_score": st.column_config.ProgressColumn(
                                "Match %",
                                min_value=0,
                                max_value=100,
                                format="%.0f%%"
                            )
                        }
                    )
                    st.download_button(
                        "💼 Export Job Matches",
                        top_jobs.to_csv(index=False),
                        "job_matches.csv"
                    )
                else:
                    st.warning("No job data loaded. Please check jobs.csv")
            
            with tab2:
                if detected_skills:
                    skill_levels = {skill: min(100, 70 + i*10) for i, skill in enumerate(detected_skills)}
                    st.bar_chart(pd.DataFrame.from_dict(
                        {"Skill Level": skill_levels},
                        orient="index"
                    ))
                else:
                    st.info("No skills detected for visualization")
            
            with tab3:
                st.subheader("Extracted Resume Text")
                st.text_area("Full Text", text, height=300)
                
        except Exception as e:
            st.error(f"Error processing resume: {e}")

# ===== Sidebar for Admin =====
with st.sidebar:
    st.header("Admin Panel")
    if st.button("🔄 Reload Job Data"):
        load_jobs.clear()
        st.rerun()
    
    if st.checkbox("Show raw job data"):
        st.dataframe(jobs_df)