# 🎯 ATS Resume Optimizer

> **AI-powered resume optimizer that rewrites your resume bullet points to beat Applicant Tracking Systems (ATS) — powered by a free Hugging Face LLM, built with Flask.**

---

## 📸 Demo

| Step 1 — Job Description | Step 2 — Resume Points | Step 3 — ATS Output |
|:---:|:---:|:---:|
| Paste the job posting | Add your existing bullets | Get optimized, ATS-ready points |

---

## ✨ Features

- 🤖 **AI-Powered** — Uses `deepseek-ai/DeepSeek-V3-0324` via Hugging Face (completely free)
- 🏢 **Section-wise Output** — Organizes optimized points by company/institution
- 🛠️ **Skills Section** — Auto-generates a tailored Skills section based on the job description
- 🎯 **ATS-Friendly** — Uses job description keywords, strong action verbs, and measurable results
- 💻 **Local Deployment** — Runs entirely on your machine, no data sent to third parties
- 🎨 **Clean UI** — Step-by-step interface with a modern dark theme

---

## 🚀 How It Works

```
You paste Job Description  →  You paste Resume Points  →  AI rewrites everything ATS-friendly
```

The AI will:
1. **Rewrite** your resume bullets using keywords from the job description
2. **Organize** output by company/institution (Compass Group, Capgemini, TCET, etc.)
3. **Generate** a tailored Skills Section (Technical Skills, Soft Skills, Tools & Technologies)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| AI Model | DeepSeek-V3 via Hugging Face Inference API |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Config | python-dotenv |

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.8+
- A free [Hugging Face](https://huggingface.co) account

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ats-optimizer.git
cd ats-optimizer
```

### 2. Install dependencies
```bash
pip install flask requests python-dotenv huggingface_hub
```

### 3. Get your free Hugging Face API key
1. Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Click **New Token** → Role: **Read** → Generate
3. Copy the token

### 4. Create your `.env` file
```bash
# Create .env in the project root
HF_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Run the app
```bash
python app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

---

## 📋 How to Use

**Step 1** — Paste the full job description and click **Submit**

**Step 2** — Paste your resume points organized by company like this:
```
Company X:
- Managed food service operations for 500+ clients
- Worked with team to reduce costs

Company Y:
- Wrote Python scripts for data processing
- Helped with cloud migration tasks

Company Z:
- Built a web app using React and Node.js
- Won hackathon for ML project
```

**Step 3** — Click **Optimize** and get your ATS-ready output! ✅

---

## 📁 Project Structure

```
ats-optimizer/
│
├── app.py               ← Flask backend + AI logic
├── .env                 ← Your HuggingFace API key (not committed)
├── .gitignore           ← Ignores .env, __pycache__, etc.
├── requirements.txt     ← Python dependencies
├── README.md            ← You are here
└── templates/
    └── index.html       ← Frontend UI
```

---

## 🔒 Environment Variables

| Variable | Description |
|----------|-------------|
| `HF_API_KEY` | Your Hugging Face API token (free) |

> ⚠️ **Never commit your `.env` file.** It is already listed in `.gitignore`.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs by opening an Issue
- 💡 Suggest features via Issues
- 🔧 Submit Pull Requests

---

## 👤 Author

**Ankit Vikas Agrawal**
- LinkedIn: https://www.linkedin.com/in/ankit-vikas-agrawal/

---

⭐ **If this project helped you, give it a star!**
