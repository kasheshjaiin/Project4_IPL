from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load your dataset
df = pd.read_csv('ipl_history.csv') 

# Function to get unique values for each feature from the dataset
def get_unique_values(feature):
    return df[feature].unique()

# Render the index.html template with dropdown options
@app.route('/')
def index():
    venues = get_unique_values('venue')
    batting_teams = get_unique_values('bat_team')
    bowling_teams = get_unique_values('bowl_team')
    strikers = get_unique_values('batsman')
    bowlers = get_unique_values('bowler')
    
    return render_template('index.html', venues=venues, batting_teams=batting_teams, 
                           bowling_teams=bowling_teams, strikers=strikers, bowlers=bowlers)

if __name__ == '__main__':
    app.run(debug=True)
