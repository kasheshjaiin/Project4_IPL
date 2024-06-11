# IPL Score Prediction

This project involves predicting the final score of an IPL (Indian Premier League) cricket match using machine learning models. The data is processed and analyzed using Spark, and several machine learning models are implemented including a Neural Network, Linear Regression, and Random Forest.

## Project Overview

### Objectives
- Load and preprocess IPL match data.
- Implement machine learning models to predict the final score of a match.
- Evaluate the performance of different models.
- Save the trained model for future predictions.
- Provide an interactive widget for demonstrating the model.

### Features
- Data Loading: Load IPL match data from a CSV file hosted on AWS S3.
- Data Preprocessing: Clean and preprocess the data including label encoding for categorical features and scaling for numerical features.
- Model Training:
  - **Neural Network**: Built using Keras with TensorFlow backend.
  - **Linear Regression**: Simple linear regression model.
  - **Random Forest**: Random forest regressor to capture non-linear patterns.
- Model Evaluation: Evaluate models using Mean Absolute Error (MAE) and Mean Squared Error (MSE).
- Feature Importance: Visualize feature importance from the Random Forest model.
- Model Saving: Save the trained neural network model for future use.
- Interactive Widget: Demonstrate the trained model using an interactive widget with Voilà.

### Data
The dataset used in this project includes details of IPL matches such as venue, batting team, bowling team, batsman, bowler, and more. Key columns include:
- `mid`: Match ID
- `date`: Date of the match
- `venue`: Venue of the match
- `bat_team`: Batting team
- `bowl_team`: Bowling team
- `batsman`: Batsman on strike
- `bowler`: Bowler delivering the ball
- `runs`: Runs scored on the ball
- `total`: Total score to be predicted

## Setup and Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/ipl-score-prediction.git
    cd ipl-score-prediction
    ```

2. **Install Dependencies**:
    Ensure you have Python and Jupyter Notebook installed. Install the required Python packages using the `requirements.txt` file:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Jupyter Notebooks**:
    - For training and evaluating models, open and run the `IPL_Score_Prediction_colab.ipynb` notebook using Jupyter:
      ```sh
      jupyter notebook IPL_Score_Prediction_colab.ipynb
      ```

    - For demonstrating the trained model using an interactive widget, use Voilà to run the `widget.ipynb` notebook:
      ```sh
      voila widget.ipynb
      ```

## Usage

1. **Data Loading and Preprocessing**:
   The notebook loads data from an S3 bucket and preprocesses it by dropping irrelevant columns, encoding categorical features, and scaling numerical features.

2. **Model Training**:
   Train different models (Neural Network, Linear Regression, Random Forest) on the preprocessed data.

3. **Model Evaluation**:
   Evaluate each model using metrics like MAE and MSE, and visualize the feature importance from the Random Forest model.

4. **Model Saving**:
   Save the trained neural network model to a file for future predictions.

5. **Interactive Widget**:
   Use Voilà to run the `widget.ipynb` notebook and interactively predict scores by selecting the venue, batting team, bowling team, striker, and bowler.

## Contributors

- **[Abid Hussain](https://github.com/abidhussainca1294)** - 
- **[Ali Khan](https://github.com/khanali37gmail)** - 
- **[Amir Siddiqui](https://github.com/ajsidd)** - 
- **[Kashish Jain](https://github.com/kasheshjaiin)** - 


## Acknowledgments

- [Kaggle](https://www.kaggle.com/) for providing IPL datasets.
- [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/) for deep learning frameworks.
