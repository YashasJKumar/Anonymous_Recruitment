# Anonymous_Recruitment

This project is a Flask web application that connects to a PostgreSQL database trying to provide anonymity for applicants in the initial stages of the Recruitment.Each applicant will be assigned with a unique ID & also gets notified with SMTP mail integration.

![image](https://github.com/user-attachments/assets/3d482164-9286-498a-ad1f-77786ef2c32f)


## Table of Contents

- [Prerequisites](#prerequisites)
- [Setting Up PostgreSQL](#setting-up-postgresql)
- [Project Setup](#project-setup)
- [Database Migration](#database-migration)
- [Running the Application](#running-the-application)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+(recommended) installed on your machine
- PostgreSQL installed and running
- `pip` package manager installed

## Setting Up PostgreSQL

1. **Start the PostgreSQL server:**

   If PostgreSQL isn't already running, start it using the following command:
   
   ```bash
   sudo service postgresql start
   ```

2. **Create a PostgreSQL database:**

   Log in to the PostgreSQL shell:

   ```bash
   psql -U postgres
   ```

   Create a new database:

   ```sql
   CREATE DATABASE your_database_name;
   ```

   Optionally, create a new user and grant privileges:

   ```sql
   CREATE USER your_username WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;
   ```

   Exit the PostgreSQL shell:

   ```sql
   \q
   ```

## Project Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YashasJKumar/Anonymous_Recruitment
   cd Anonymous_Recruitment
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database connection:**

   Open the `config.py` file (or wherever your configuration is set), and replace the `SQLALCHEMY_DATABASE_URI` with your PostgreSQL connection string:

   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_username:your_password@localhost/your_database_name'
   ```

## Database Migration

1. **Initialize Flask-Migrate:**

   If you haven't already, initialize the migration tool:

   ```bash
   flask db init
   ```

2. **Create an initial migration:**

   ```bash
   flask db migrate -m "Initial migration"
   ```

3. **Apply the migration:**

   ```bash
   flask db upgrade
   ```

## Running the Application

1. **Run the Flask application:**

   Make sure your virtual environment is activated, then start the Flask development server:

   ```bash
   flask run
   ```

   The application should now be running at `http://127.0.0.1:5000/`.

## Troubleshooting

- **FileNotFoundError:** Ensure that all file paths are correct and that the working directory is set to the project's root directory.
- **Database Connection Issues:** Double-check your `SQLALCHEMY_DATABASE_URI` for correct syntax and ensure that the PostgreSQL server is running.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.
