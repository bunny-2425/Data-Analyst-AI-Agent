import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_plot(df: pd.DataFrame, chart_type: str, x_col: str, y_col: str = None):
    plt.figure(figsize=(8, 5))
    
    if chart_type == "bar":
        sns.barplot(data=df, x=x_col, y=y_col)
    elif chart_type == "line":
        sns.lineplot(data=df, x=x_col, y=y_col)
    elif chart_type == "pie":
        df[x_col].value_counts().plot.pie(autopct='%1.1f%%')
    elif chart_type == "hist":
        sns.histplot(data=df, x=x_col)
    else:
        raise ValueError("Unsupported chart type!")

    plt.title(f"{chart_type.title()} Chart of {x_col} vs {y_col}" if y_col else f"{chart_type.title()} Chart of {x_col}")
    plt.tight_layout()
    plt.savefig("chart_output.png")  # Save chart as an image
    plt.close()

    return "chart_output.png"