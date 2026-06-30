🎬 Movie Discovery & Recommendation Engine
A professional desktop application built with Python, MySQL, and Tkinter. This project demonstrates a 3-tier architecture that bridges a normalized relational database with an interactive, filter-driven GUI.

🚀 Features
Dynamic Filtering: Search your library by Genre, Content Type (Movie/Series), and Minimum Rating.Normalized Relational Data: Built on a 3-table structure (Categories, Movies, Preferences) ensuring data integrity.Professional GUI: Built with Tkinter to provide a clean, desktop-app experience.
Global Content Library: Supports diverse datasets including both Bollywood and Hollywood media.
Real-time Interaction: Automated SQL connectivity allows for live updates and querying without manual data entry.

🛠 Tech Stack
Database: MySQL 8.0
Logic Layer: Python 3.13
Connectivity: mysql-connector-python
Interface: Tkinter (GUI)

⚙️ How to Setup
1. Database SetupOpen MySQL Workbench.Create your database: CREATE DATABASE streaming_db;Run the provided movies_database.sql file using Server > Data Import.
2. Python EnvironmentEnsure Python is installed on your system.
Install the MySQL connector:(Bash) pip install mysql-connector-python
3. Running the AppOpen your project folder in your terminal.Update the host, user, and password fields in app.py to match your local MySQL configuration.
Run the application:(Bash) python app.py

📂 Project Structure
/Movie_Recommendation_Project
│
├── app.py                  # Main Python application
├── movies_database.sql      # Database schema and seed data
└── README.md               # Project documentation

🏗 Schema Design
The project utilizes a Relational Schema to eliminate data redundancy.
Categories: Genre taxonomies.
Movies: Core library data with Foreign Keys.
Preferences: User-level interaction data.

🤝 Contact
Developed for the Mini Project Submission. Feel free to reach out for questions regarding the technical architecture or query optimization logic.
