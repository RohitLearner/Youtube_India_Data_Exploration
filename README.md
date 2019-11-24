# Youtube India Data Exploration

Analyse Youtube videos and predict likes and views.

## Requirements

User must have Sckit-learn, Pandas and Python 3 installed.

## Usage

```bash 
python3 grid_search.py
python3 train.py
python3 predict.py
```

Run the grid_search.py file, copy the parameters obtained so into train.py and run. Run predict.py to get final predictions.

## File description

* preprocessedIndia.csv : Youtube data (processed) collected from Nov 2017 to June 2018 
* preprocessedtest2019.csv : Youtube data (processed) collected in Nov 2019
* train.csv : Training sample extracted from preprocessedIndia.csv
* test.csv : Test sample extracted from preprocessedIndia.csv
* trained_model : Pre-trained Random Forest Regressor model ( is generated on running train.py)

## Useful links

Preprocessing and data visualisation - <https://www.kaggle.com/iamrohitsingh/youtube-india-data-exploration>

## Contributers

Anand Bhararia, Basant Kumar Bhala, Rohit Kumar Singh and Jayabrata Das (IIT Bombay)
