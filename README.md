# 📄 AI Resume Scanner with Streamlit

<img width="1772" height="856" alt="job " src="https://github.com/user-attachments/assets/8d7c46de-27f9-4e76-8192-37daea5a32ab" />
28baca3b77/EVsKI-7v5JJFis3mlLDpzD0BIZIzeY1yKL4SaI4q_d5pdg?e=uZCsYw) 
*Replace with actual screenshot later*

An intelligent web app that **analyzes resumes** and **matches them with job listings** using Python and Streamlit.

## 🚀 Features
- **PDF Resume Parser**: Extracts text from uploaded resumes
- **Skill Matching**: Identifies key skills (Python, SQL, etc.)
- **Job Recommendations**: Suggests best-matched jobs from your database
- **Live Demo**: [View on Streamlit Cloud](#) *https://resume-scanner-hluejgx8rspqubpggrdxzn.streamlit.app/*

## ⚙️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**: 
  - `pypdf` - PDF text extraction
  - `pandas` - Data processing
  - `spaCy` - NLP (optional)

## 📦 Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/resume-scanner.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run locally:
   ```bash
   streamlit run app.py
   ```

## 🛠️ Customization
Edit `jobs.csv` to add your own job listings:
```csv
title,company,required_skills
Data Analyst,TechCorp,"Python, SQL, Excel"
```

## 🌐 Deployment
Hosted for free on:  
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://resume-scanner-hluejgx8rspqubpggrdxzn.streamlit.app/)

## 📝 How It Works
1. User uploads resume (PDF)
2. App extracts text and detects skills
3. Matches with jobs database
4. Displays best matches with compatibility scores



## 🤝 Contributing
Pull requests welcome! For major changes, please open an issue first.

## 📜 License
[MIT](https://choosealicense.com/licenses/mit/)
