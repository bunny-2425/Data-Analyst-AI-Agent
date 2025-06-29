import streamlit as st
import pandas as pd
import os
from file_handler import read_file
from visualizer import generate_plot
from together import Together
from PIL import Image
import uuid

st.set_page_config(page_title="Data Analyst Agent", layout="wide")
st.title("🧠📊 Intelligent Data Analyst Agent")
st.markdown("""
Upload your data file and ask any questions. The agent can analyze data, generate insights, and create visualizations.
Supports `.csv`, `.xlsx`, `.txt`, `.pdf`, and image files.
""")

# Session state for persistent data if needed
if 'df' not in st.session_state:
    st.session_state.df = None

# File Upload
uploaded_file = st.file_uploader("Upload your data file", type=["csv", "xlsx", "txt", "pdf", "png", "jpg"])

# Read file
if uploaded_file:
    file_path = os.path.join("uploaded_files", f"{uuid.uuid4()}_{uploaded_file.name}")
    os.makedirs("uploaded_files", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    df = read_file(file_path)
    st.session_state.df = df

    if df is not None:
        st.subheader("🔍 Preview of Uploaded Data")
        st.dataframe(df.head())

        # Q&A Section
        st.subheader("💬 Ask Questions About Your Data")
        question = st.text_input("Type your question here")

        if st.button("Get Answer") and question:
            client = Together()
            response = client.chat.completions.create(
                model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
Here is the data:
{df.to_csv(index=False)}

Now answer this question: {question}
"""
                    }
                ]
            )
            answer = response.choices[0].message.content
            st.success("Answer:")
            st.markdown(answer)

        # Visualization Section
        st.subheader("📈 Generate Visualization")
        chart_type = st.selectbox("Choose chart type", ["bar", "line", "pie"])
        x_col = st.selectbox("Select X-axis", df.columns)
        y_col = None
        if chart_type in ["bar", "line"]:
            y_col = st.selectbox("Select Y-axis", df.columns)

        if st.button("Generate Chart"):
            plot_path = generate_plot(df, chart_type=chart_type, x_col=x_col, y_col=y_col)
            st.image(Image.open(plot_path), caption="Generated Chart")

    else:
        st.error("Unsupported file format or failed to read the file. Please upload a valid file.")
