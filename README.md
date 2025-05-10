# Codeforces Analytics Project

The Codeforces Analytics Project is a comprehensive data pipeline and visualization system designed to analyze programming contests from the Codeforces platform. It implements a full Extract, Transform, Load (ETL) pipeline, orchestrated by Apache Airflow, to process contest data from the Codeforces API into a PostgreSQL database. The processed data is then visualized through a Streamlit dashboard.

---

## 🚀 Project Architecture

The project follows a modular architecture comprising several interconnected components:

1. **Data Extraction** – Fetches contest data from the Codeforces API.
2. **Data Transformation** – Processes and cleans the raw contest data.
3. **Data Storage** – Persists transformed data in a PostgreSQL database.
4. **Workflow Orchestration** – Manages the ETL workflow using Apache Airflow.
5. **Data Visualization** – Presents contest data through a Streamlit dashboard.

---

## 🔁 ETL Pipeline Components

The ETL pipeline is the core of the system, responsible for acquiring, processing, and storing Codeforces contest data:

- **Extraction**: The `fetch_contests.py` script retrieves contest data from the Codeforces API and stores it in `data/contests.csv`.
- **Transformation**: The `transformation.py` script processes the raw data, cleaning and restructuring it into `data/contests_transformed.csv`.
- **Loading**: The `load_to_db.py` script loads the transformed data into the PostgreSQL database.
- **Visualization**: The Streamlit dashboard queries the database to generate visualizations.

---

## 🧱 Infrastructure Components

The system operates within a Docker-based infrastructure that includes multiple interconnected services:

- **PostgreSQL**: Database for storing both Airflow metadata and contest data.
- **Redis**: Message broker for Airflow's Celery Executor.
- **Airflow Webserver**: Web interface for managing Airflow workflows.
- **Airflow Scheduler**: Schedules and triggers workflow executions.
- **Airflow Worker**: Executes the tasks within the workflows.

The entire system is integrated through Docker Compose, which manages the various services and their interactions.

---

## 📅 Airflow Orchestration

The Apache Airflow DAG (`contest_etl_dag.py`) orchestrates the ETL workflow, providing scheduling, monitoring, and error handling capabilities.

**Key DAG Configuration**:
- **Owner**: Youssef
- **Schedule**: Daily (`@daily`)
- **Retries**: 5 (with 5-minute delay between retries)
- **Start Date**: May 7, 2025

---

## 🛢️ Database Integration

The system uses PostgreSQL for data storage. The connection is managed through SQLAlchemy, with contest data stored in a table named `contests`.

**Connection URI**:
```text
postgresql+psycopg2://airflow:airflow@postgres:5432/codeforces
```

---

## 🛠️ Getting Started

Follow these steps to set up and run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/youssefamr4800/Codeforces_analytics_project.git
   cd Codeforces_analytics_project
   ```

2. **Start the Docker containers**:
   ```bash
   docker-compose up --build
   ```

3. **Access the Airflow web interface**:
   Open your browser and go to `http://localhost:8080`

4. **Trigger the ETL pipeline**:
   In the Airflow interface, locate the `contest_etl_dag` and trigger it manually or wait for the scheduled run.

5. **Access the Streamlit dashboard**:
   Navigate to `http://localhost:8501` to view the visualizations.

---

## 📁 Project Structure

```plaintext
├── dags/
│   └── contest_etl_dag.py
├── data/
│   ├── contests.csv
│   └── contests_transformed.csv
├── scripts/
│   ├── fetch_contests.py
│   ├── transformation.py
│   └── load_to_db.py
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

---

## 📜 License

This project is licensed under the MIT License.

---

For more detailed information, please visit the project's [DeepWiki page](https://deepwiki.com/youssefamr4800/Codeforces_analytics_project).
