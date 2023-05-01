Project Churn

Discription:
Project Churn explores the reasons behind customer churn and predicts who will churn by using statistical 
analysis and mechanine learning models.

Project Goal:
The goal is to, as best as possible, accurately predict the likelihood that a customer will churn based 
on past observations.

Initial Hypotheses: 
Churn is largely correlated with not having add-on services and can be used to predict 
those who would churn. How do add-on services correlate to other features like type of internet access and 
customer age, etc and churn? Do social demographics affect churn?

Project Plan: 
  * Acquire: Download the telco customer data from 
  * Prepare: Remove nulls, change objects to int or floats, and encode all relevant categorical features.
  * Explore: Use the above initial hypothesis to tease out statistical relationships to select the most 
  appropriate features to develop the predictive model, focusing on tenure, add-on services, senior citizen status, and internet service
  type.
  * Modeling: Will run selected features against all models while altering hyperparameters to pull back the best
  results (most accurate and/or the model with the best recall metrics).
  
 Reproducing: 
 Clone the repo and run as a Jupiter Notebook. Run each cell indevidually in order or all at once. Make sure all of the
 appropriate modules are in the correct directory.
  
NOTE: you will need your own creditals stored in an env file or SQL database will deny you access. alternatively 
download the telco csv file located in this repo and the notebook will run it via the acquire function.
