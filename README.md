
# Predict_love
Data visualisation with DASH / Data cleaning  + descriptive statistics and Machine learning with Python (pandas,numpy, scikitlearn)

Hi, let’s talk about machine learning, get back when we carried out the first team-project of the year spent at the French university Lyon II in order to be graduated in Data Science in 2023 (Master). 
Our mission : to find out the best model capable of predicting “love”- let’s call it “match” - between two people. In other words, discover the magic formula to take over the “speed dating” heterosexual market. **KPI : f1 score**. 

Provided data : a survey carried out by a group of students at Columbia University.  Sample : 6804 students – around half coming from miscellaneous American universities – the other half coming from European or Asian universities. Average Age : 26 y.o. Rate of match : < 20%. 

Protocol : 8 out of 10 people met 10 partners (the other ones : 6). Everybody had to fill-in an extensive form covering demo (age, gender,…), personal fields of interest (TV, reading,…), and their expectations regarding their ideal partner. All the met partners rated them in return (e.g.: "On a scale from 0 to 10, to what extend was your partner attractive ?") Ouput : 70 variables to be cleaned (some missing data, same intel reported several times in different columns, ...). 

What kind of code you will find : 

#**PART 1 : DEEP-DIVE**

(1) **Interactive Data visualization** with **DASH** to get a first glance on main data (pie-char, histogram, scatter plot) 

[interactive_histograms.txt](https://github.com/Xhrys69/predict_love/files/9801858/interactive_histograms.txt) 
[interactive_pie-charts.txt](https://github.com/Xhrys69/predict_love/files/9801859/interactive_pie-charts.txt) 
[[interactive_scatterplots.txt](https://github.com/Xhrys69/predict_love/files/9801860/interactive_scatterplots.txt)] 

-> How to proceed  ? (1) Open Visual Studio Code (2) Connect the terminal to a Virtual Environnement (3) Paste the txt.file (4) Run the file

(2) **Data cleaning and descriptive statistics with Python (pandas, numpy)**

[Data_cleaning_easy-date_Train.pdf](https://github.com/Xhrys69/predict_love/files/9801930/Data_cleaning_easy-date_Train.pdf)

(3) 1st Model we built : **Anova and Machine learning** with Python (scikit learn – TreeClassifier and Random Forest after SMOTE)

[Machine_learning_F1 score 61%_Anova_Smote_tree_classifier_random_forest.pdf](https://github.com/Xhrys69/predict_love/files/9801938/Machine_learning_F1.score.61._Anova_Smote_tree_classifier_random_forest.pdf)

(4) 2nd Model we built : **Our winner Model (F1 score : 78%. Error rate : 9.5%) !**

https://github.com/spicatchou/Easydate-Christolic/blob/074dfa0d462e7cc46a527e52812a0d2481db1aca/easydate.ipynb


#**PART 2 : DEPLOYEMENT**

(1)**This model can be directly run with Python**

https://github.com/spicatchou/Easydate-Christolic/blob/d98cf5e310d043dc1cd2cec4afa44a8607cb8bdc/model.sav

(2)**Interactive Data visualisation of the results**

https://github.com/spicatchou/Easydate-Christolic/blob/64e5eb550053050d92d9d88d429ddad435721f5c/dash-result.py


