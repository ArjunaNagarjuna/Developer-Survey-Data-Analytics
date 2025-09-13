📊 Survey Data Explorer

An interactive Streamlit application to explore and analyze survey data (like the Stack Overflow Developer Survey).
Upload your survey CSV files, filter responses, and visualize trends by country, developer roles, and coding experience.

🚀 Features

Upload survey data (survey_results_public.csv and survey_results_schema.csv)

Apply interactive filters:

🌍 Country

👔 Developer Role

📈 Years of Coding Experience

View the filtered dataset (first 50 rows)

Visualize top countries and role distributions

🛠️ Installation

Clone the repository:

git clone https://github.com/yourusername/survey-data-explorer.git
cd survey-data-explorer


Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows


Install dependencies:

pip install -r requirements.txt

📂 Files

Survey_app.py → Main Streamlit app

requirements.txt → Dependencies

README.md → Project documentation

▶️ Usage

Run the Streamlit app:

streamlit run Survey_app.py


Open the link provided (default: http://localhost:8501) in your browser.

Upload survey_results_public.csv

Upload survey_results_schema.csv

Use sidebar filters to explore the data interactively!

📊 Example Visualizations

Top 10 countries in the survey (bar chart)

Developer roles distribution (horizontal bar chart)

📦 Requirements

Python 3.8+

Streamlit

Pandas

Matplotlib









