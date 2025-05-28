**Dataset Analysis using Pandas & NumPy**

**📜 Overview**
This project analyzes a **public dataset** using **Pandas** and **NumPy** to extract key insights, compute basic statistics, and explore feature correlations.

**📂 Project Structure**
```
dataset-analysis/
├── analysis.py              # Python script for data analysis
├── requirements.txt         # Dependencies
├── README.md                # Documentation
```

**🔹 Installation & Setup**
**Prerequisites**
- **Python 3.x** (Check with `python3 --version`)
- **VS Code** (Optional for coding efficiency)
- **Google Cloud SDK** (For deployment, if needed)

**Install Dependencies (Without Homebrew)**
```bash
python3 -m pip install numpy pandas
```

**🚀 Running the Analysis**
**1️⃣ Load Dataset**
```python
import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)
```

**2️⃣ Print First Few Rows**
```python
print(data.head())
```

**3️⃣ Check Column Data Types**
```python
print(data.info())
```

**4️⃣ Compute Basic Statistics**
```python
print("Mean:\n", data.mean(numeric_only=True))
print("Median:\n", data.median(numeric_only=True))
print("Mode:\n", data.mode().iloc[0])
print("Standard Deviation:\n", data.std(numeric_only=True))
```

**5️⃣ Compute Feature Correlations**
```python
print(data.corr(numeric_only=True))
```

**🌍 Pushing to GitHub**
**Initialize Git**
```bash
git init
git add .
git commit -m "Initial dataset analysis"
```

**Push to Your Repository**
```bash
git remote add origin https://github.com/YOUR_USERNAME/dataset-analysis.git
git branch -M main
git push -u origin main
```

**📜 License**
This project is licensed under the **MIT License**.
