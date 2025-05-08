# 🏆 Codeforces Contest ETL Pipeline & Dashboard

This project extracts, transforms, and loads Codeforces contest data into a PostgreSQL database using Apache Airflow, and visualizes the data through a Streamlit dashboard.

---

## 📁 Project Structure

.
├── dags/
│ └── contest_etl_dag.py # Airflow DAG definition
├── scripts/
│ ├── fetch_contests.py # Extracts contests from Codeforces API
│ ├── transformation.py # Transforms raw data
│ └── load_to_db.py # Loads data into PostgreSQL
├── data/ # Raw and transformed data files (ignored by Git)
├── dashboard/streamlit_app.py # Streamlit dashboard
├── requirements.txt # Python dependencies
└── README.md # This file

yaml
Copy
Edit

---

## ⚙️ Technologies Used

- **Apache Airflow** – ETL orchestration
- **Python + Pandas** – Data extraction & transformation
- **PostgreSQL** – Data storage
- **SQLAlchemy** – Database interaction
- **Streamlit** – Data dashboard
- **Docker (optional)** – Containerization

---

## 🔄 ETL Pipeline (Airflow DAG)

- **Extract**: Fetches contest data from [Codeforces API](https://codeforces.com/api/contest.list).
- **Transform**: Cleans and reformats the data (timestamp conversion, column filtering).
- **Load**: Stores cleaned data in a PostgreSQL table.

The DAG runs daily and ensures fresh contest data is always available.

---

## 📊 Streamlit Dashboard

Interactive dashboard to:

- View all contests
- Filter by contest type
- Explore summary statistics
- Visualize contest durations
- Identify the longest/shortest contests

---

## 🏁 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/codeforces-etl-dashboard.git
cd codeforces-etl-dashboard
2. Set up Airflow
Follow Airflow installation guide or use Docker.

Ensure your PostgreSQL database is running with the following connection (or update it in load_to_db.py and Streamlit app):

bash
Copy
Edit
postgresql+psycopg2://airflow:airflow@postgres:5432/codeforces
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or manually install:

bash
Copy
Edit
pip install pandas requests sqlalchemy psycopg2-binary streamlit apache-airflow
4. Run Airflow
Ensure Airflow services are running and the DAG is placed in your dags/ directory.

bash
Copy
Edit
airflow webserver --port 8080
airflow scheduler
Then, go to http://localhost:8080, enable the DAG, and trigger it.

5. Run Streamlit App
bash
Copy
Edit
cd dashboard
streamlit run streamlit_app.py
📌 Notes
.csv files (contests.csv, contests_transformed.csv) are stored in data/ and should be ignored by Git using .gitignore.

Avoid long-running code at the top level of DAG files — this can cause Airflow DAG import timeouts.

📬 Contact
Developed by Youssef Amr Saeed
For questions or suggestions, open an issue on GitHub.

📄 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

You're ready to commit and push this file to GitHub. Want me to help you make the `.gitignore` or `requirements.txt` next?
