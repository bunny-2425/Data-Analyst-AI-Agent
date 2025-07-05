# Data-AnalystA-AI-Agent

# 🧠📊 Intelligent Data Analyst Agent

An AI-powered Streamlit application that acts as your personal data analyst. Upload any dataset, ask questions in natural language, and get instant insights and visualizations—all powered by a cutting-edge LLM.

---

## 🚀 Features

- **Natural Language Q&A**: Ask questions about your data and get human-like answers using `meta-llama/Llama-4-Maverick-17B`.
- **Multi-format File Support**: Upload `.csv`, `.xlsx`, `.txt`, `.pdf`, and image files (`.png`, `.jpg`)—the agent will handle them all.
- **Data Visualization**: Instantly generate bar, line, and pie charts based on your data selection.
- **OCR Integration**: Extracts text from scanned images and PDFs for deeper analysis.
- **Streamlit UI**: Clean, intuitive, and responsive interface for real-time interaction.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web app framework
- **Together API** – LLM interaction (`Llama 4 Maverick`)
- **Pandas** – Data handling
- **Matplotlib & Seaborn** – Visualization
- **PyMuPDF & pytesseract** – PDF and image text extraction
- **Openpyxl, python-docx** – Excel and Word file support
- **dotenv** – Secure API key management

---

## 📂 Project Structure

📁 Intelligent-Data-Analyst-Agent/
├── app1.0.py # Streamlit application

├── agent_core.py # Core agent logic using Together API

├── file_handler.py # File reader for various formats

├── visualizer.py # Chart generation logic

├── test_file_handler.ipynb # File reading tests

├── requirements.txt # Required dependencies

├── .env # API keys (excluded from version control)


---

## 🔧 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/intelligent-data-analyst-agent.git
   cd intelligent-data-analyst-agent
   ```

2.Install dependencies
```bash
pip install -r requirements.txt
```

3.Add your Together API key
Create a .env file in the root directory and add:
```bash
TOGETHER_API_KEY=your_api_key_here
```

4.Run the application
```bash
streamlit run app1.0.py
```

🧪 Sample Input & Output
Text File Analysis: Uploads a .txt file → Agent extracts and analyzes content.
Image to Text: Uploads an image → OCR extracts data → LLM answers questions.
Chart Output Example:
