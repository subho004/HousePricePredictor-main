# Bangalore House Price Predictor

Welcome to the Bangalore House Price Predictor project! This project uses machine learning to predict house prices in Bangalore based on various features such as area, number of bedrooms, number of bathrooms, and square footage.

## Overview

This project aims to provide a simple web application where users can input property details, and the application will return a price prediction based on a trained machine learning model. We have used scikit-learn for model development and Flask for creating the web API.

## Features

- Predict house prices in Bangalore.
- User-friendly web interface.
- Multiple machine learning models to choose from.
- High accuracy achieved with Ridge regression (0.8296651410179634).
  
## Prerequisites

1. **Docker**: Ensure that Docker is installed on your machine. You can download Docker from [here](https://www.docker.com/get-started).

2. **Docker Hub Account**: If you don't have a Docker Hub account, you'll need to create one [here](https://hub.docker.com/).
   
## Usage Docker

1. Pull the Docker Image

```bash
docker pull subho004/housepricepredictor-main-web:latest
```

2. Run the Docker Image

```bash
docker run -p 5001:5001 subho004/housepricepredictor-main-web:latest
```
3. Access the web application in your browser at `http://localhost:5001`.


## Usage GitHub

1. Clone the repository:

   ```bash
   git clone https://github.com/subho004/HousePricePredictor.git
    ````

2. Set up the virtual environment and install dependencies:

    ````bash
    cd HousePricePredictor
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    pip install -r requirements.txt
    ````

3. Create a .env file and add MONGODB_URL
   ```bash
      MONGODB_URL= <YOUR_MONGO_URL>
   ```

4. Run the Flask web application:

    ````bash
    flask run
    ````

5. Access the web application in your browser at `http://localhost:5001`.

6. Enter the property details (area, bedrooms, bathrooms, square footage) and click the "Predict Price" button.


## Model Selection
We have trained three regression models for price prediction:

- Linear Regression
- Lasso Regression
- Ridge Regression
  
Based on our experiments, the Ridge Regression model achieved the highest accuracy (0.8296651410179634) and was selected as the default model for the application.

## Project Structure


### Files and Directories

- **`app.py`**: Flask application code.
- **`static`**: Static assets (CSS, JavaScript, etc.).
- **`templates`**: HTML templates for the web pages.
- **`models`**: Directory for storing machine learning models (e.g., `RidgeHouseModel.pkl`).
- **`data`**: Directory for storing dataset files (e.g., `Cleaned_Housedata.csv`).

### Docker Files

- **`Dockerfile`**: This file contains instructions for building a Docker image for your application.

- **`docker-compose.yml`**: A YAML file defining services, networks, and volumes. It's used for multi-container Docker applications.

### Configuration Files

- **`.dockerignore`**: Similar to `.gitignore`, this file specifies which files and directories should be ignored during the Docker build process.

- **`.env`**: Environment file containing environment variables. It's often used to store sensitive information or configuration settings.

- **`.gitignore`**: Specifies files and directories to be ignored by Git. Commonly includes files generated during development or containing sensitive information.


## Screenshots

### Version 2.0
<img width="1494" alt="Screenshot 2024-01-21 at 10 54 01 AM" src="https://github.com/subho004/HousePricePredictor-main/assets/91646273/28f5dd5f-8a78-48f5-89a6-30de0f0f11e1">

### Version 1.0
![3](https://github.com/subho004/HousePricePredictor/assets/91646273/a6b86bc0-5f88-46c2-9d60-4461880c4bc3)
![2](https://github.com/subho004/HousePricePredictor/assets/91646273/f12a78a3-b84d-4770-b4b7-ece017f2afed)
![1](https://github.com/subho004/HousePricePredictor/assets/91646273/66cbff2a-1f53-41f1-9cd9-3fb1f0331fb0)
![4](https://github.com/subho004/HousePricePredictor/assets/91646273/213ea89f-89ae-438a-8d34-235cc6362e95)
![5](https://github.com/subho004/HousePricePredictor/assets/91646273/8272f99d-8ef1-4b3c-8b4f-70087f156d95)


## Contributing
Contributions are welcome! If you want to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push your changes to your fork.
- Submit a pull request to the main repository.

## Acknowledgments
- Data source: **[Bangalore House Price Prediction Model](https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data)**
- Flask: **[Flask Web Framework](https://flask.palletsprojects.com/)**
- Scikit-Learn: **[Scikit-Learn Machine Learning Library](https://scikit-learn.org/stable/)**
- Bootstrap: **[Bootstrap Frontend Framework](https://getbootstrap.com/)**
