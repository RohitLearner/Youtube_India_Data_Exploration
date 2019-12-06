
![Youtube Logo](https://1000logos.net/wp-content/uploads/2017/05/YouTube-logo-500x277.png)

# Youtube India Data Exploration

This is a project regarding predicting YouTube Like & View Counts using Machine Learning Techniques. This project also allows us to analyze the fundamental variables that affect the virality of the video.

## Requirements

Users must have Sckit-learn, Pandas and Python 3 installed.

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

## Machine Learning Model
Random Forest Regressor was chosen as the learning algorithm for modeling the Like & View counts predictions. It is an ensemble method where multiple base estimators (tree) are trained on sub-samples of input data and give output after averaging the result of all estimators. Considering the size of the dataset, computational power available and ability of estimator to fit data, this model was considered.

The parameters of an algorithm always affect its performance. Grid Search and Cross-Validation were used to tune the parameters for the model.

## Prediction & Conclusion
- Likes for old dataset		- 0.93
- Views for old dataset		- 0.91
- Likes for new dataset		- 0.80
- Views for new dataset		- 0.75
	 ###### * numbers are in R2 scores.
	 
*Based on the final result, we conclude that youtube data is highly temporal which can be proved by our data visualization.*

## Contributors

- Rohit Kumar Singh
- Anand Bhararia
- Basant Kumar Bhala 
- Jayabrata Das 
	
(IIT Bombay Students)

## Feedback
Feel free to send us feedback on [file an issue](https://github.com/RohitLearner/Youtube_India_Data_Exploration/issues). Feature requests are always welcome. If you wish to contribute, please take a quick look at the [documentation](https://github.com/RohitLearner/Youtube_India_Data_Exploration/tree/master/documentation).

## Acknowledgments
Inspirations are drawn from various Kaggle projects but majorly incentive is from the following :
1.  [https://www.kaggle.com/residentmario/creating-reading-and-writing](https://www.kaggle.com/residentmario/creating-reading-and-writing)
2.  [https://www.kaggle.com/skalskip/youtube-data-exploration-and-plotly-visualization](https://www.kaggle.com/skalskip/youtube-data-exploration-and-plotly-visualization)
3.  [https://www.kaggle.com/kabure/extensive-usa-youtube-eda](https://www.kaggle.com/kabure/extensive-usa-youtube-eda)

> Written with [StackEdit](https://stackedit.io/).
