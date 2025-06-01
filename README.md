# 🧠 psy-geek
## Personality Analysis Using 16PF

<!--
**Author**: [PALLADIUM26](https://github.com/PALLADIUM26)
**Repository**: [github.com/PALLADIUM26/psy-geek](https://github.com/PALLADIUM26/psy-geek)
-->

### 📌 Overview

`psy-geek` is a personality analysis tool that leverages the 16 Personality Factor (16PF) model to assess individual personality traits. The project integrates a machine learning backend with a user-friendly frontend interface, allowing users to input data and receive personality assessments.

### 🧰 Features

* **16PF-Based Analysis**: Utilizes the 16PF model for comprehensive personality assessment.
* **Machine Learning Integration**: Employs a Random Forest classifier (`my_random_forest.joblib`) for predictions.
* **Frontend Interface**: Provides an interactive user interface for data input and result visualization.
* **Modular Architecture**: Separates concerns with distinct `frontend/` and `backend/` directories.

### 🗂️ Project Structure

```
psy-geek/
├── backend/                # Backend logic and API endpoints
├── frontend/               # Frontend interface (HTML/CSS/JavaScript)
├── my_random_forest.joblib # Pre-trained Random Forest model
├── .gitignore              # Git ignore file
└── README.md               # Project documentation
```

### 🚀 Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PALLADIUM26/psy-geek.git
   cd psy-geek
   ```

2. **Set Up the Backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   py app.py
   ```

3. **Set Up the Frontend**:
   * Navigate to the `frontend/` directory.
   * Open `index.html` in a web browser or serve it using a local server.

4. **Access the Application**:
   * Interact with the frontend interface to input data and receive personality assessments.

