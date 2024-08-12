   # FOODY  AND FOODIE SENTIMENT ANALYSIS 
   
   ![Foody & Foodie Logo](logo.png)
 
    ---
 # OVERVIEW 
    ---
  Foody&Foodie, a beloved family-run restaurant in San Francisco, CA, has been a community staple for years. With a rich history in the food industry, the owners have gained insights into customer preferences and dining trends. They understand that maintaining a competitive edge requires more than delicious food and excellent service; it requires an acute awareness of customer sentiments and feedback. Recognizing that customer satisfaction is a dynamic target influenced by shifting trends and evolving market conditions, Foody&Foodie is implementing a data-driven approach to gather and analyze customer feedback. This project aims to provide a reliable method for interpreting customer sentiments, enabling Foody&Foodie to make informed decisions to enhance their offerings and dining experience. Ultimately, this initiative will help Foody&Foodie stay ahead in a competitive market by adapting to the ever-changing demands of their customers and strengthening their reputation as a cherished dining destination.


 # PROBLEM STATEMENT 
---
The management of Foody&Foodie understands the importance of a reliable method for gathering and analyzing customer feedback. By leveraging insights into customer sentiments, they aim to make informed decisions that enhance their offerings and overall customer experience. This approach will allow them to stay attuned to customer needs, ensuring that their menu and service meet and exceed expectations. Through systematic sentiment analysis, Foody&Foodie can adapt to changing preferences, reinforcing their commitment to providing exceptional food and service while maintaining a competitive edge in the market.


# CHALLENGES 
---
The food industry relies on several measurable parameters, such as customer satisfaction, quality of food, service speed, and ambiance, to gauge a restaurant's success. To ensure the accuracy and fairness of evaluations, it is essential to identify and use a neutral dataset that encompasses all these aspects. This will allow for a comprehensive analysis, helping restaurants like Foody&Foodie make well-informed decisions to enhance their offerings and meet their customers' evolving needs.

# OBJECTIVES 
---
Main objective:
 ---
   * The goal is to develop a robust predictive model that can accurately classify the sentiment of a customer's review, aiming to achieve both a recall score and an accuracy score of over 80%, ensuring reliable insights into customer feedback and enhancing the restaurant's ability to meet customer needs.
 
 Specfic objectives:
 ---
 * Identify the Most Common Words Used in the Dataset Using a Word Cloud:
Generate a visual representation of the most frequently occurring words in the customer reviews dataset. This will provide an at-a-glance overview of the prevalent themes and topics in the reviews, highlighting key terms that customers commonly use when describing their experiences.

 * Confirm the Most Common Words That Are Positively and Negatively Tagged:
Analyze the dataset to determine the words that are most often associated with positive and negative sentiments. This involves categorizing and quantifying the words based on their sentiment tags, which helps in understanding what language customers use when expressing satisfaction or dissatisfaction.

 * Recognize the Products That Have Been Reviewed by Customers:
Identify and list the specific products, dishes, or services that are frequently mentioned in the customer reviews. This helps in pinpointing the items that generate the most feedback, whether positive or negative, and provides insight into what aspects of the restaurant’s offerings are most significant to customers.

  * Analyze the Distribution of Sentiments:
Examine the overall sentiment distribution across the reviews, breaking down the proportion of positive, negative, and neutral sentiments. This analysis provides a comprehensive view of the restaurant’s performance from the customers’ perspective, highlighting areas of strength and opportunities for improvement.

# DATA 
---
* Data Source: Yelp reviews from restaurants in the San Francisco area. 

* Data Preprocessing: Removing capitalizations, stopwords, and applying lemmatization.


# MODELLING 

---
 To classify the sentiment of reviews, multiple machine learning models were implemented and optimized using hyperparameter tuning. Each model brings its own strengths to the task, and their performance was assessed based on various evaluation metrics.
 
 
# 1.Logistic Regression
---
 
 Logistic regression is a linear model commonly used for binary and multiclass classification problems. In this project, the following steps were taken:

* Training: The logistic regression model was trained using the review data, with a focus on achieving convergence by setting the maximum number of iterations to 3000. This ensures that the model has ample opportunity to fit the data adequately.

* Hyperparameter Tuning: Grid search was used to optimize the hyperparameters, including:

* `C`: The inverse of regularization strength. Smaller values indicate stronger regularization.

* `max_iter`: The maximum number of iterations for the solver to converge.

* `solver`: The algorithm used for optimization, such as 'liblinear' or 'saga'.


# 2.Random Forest Classifier
---
The random forest classifier is an ensemble learning method that builds multiple decision trees and merges their predictions to improve accuracy and control over-fitting. The following approach was used:

* Implementation: A random forest model was implemented with initial hyperparameters set as:

       * `n_estimators`: 100, representing the number of trees in the forest.

       * `max_depth`: 10, the maximum depth of each tree to control the complexity and prevent over-fitting.

       * `min_samples_split`: 10, the minimum number of samples required to split an internal node.

       * `min_samples_leaf`: 5, the minimum number of samples required to be at a leaf node.
  
* `Hyperparameter Tuning`: Tuning involved adjusting the number of trees and the depth of each tree to find the optimal balance       between bias and variance.


# 3.Linear Support Vector Machine (SVM)
---

 SVM is a powerful classification method, particularly for high-dimensional data. The linear SVM was applied as follows:

 * Dimensionality Reduction: To manage the high dimensionality of the text data, `TruncatedSVD was used`. This technique reduces the feature space while preserving as much information as possible, which is crucial for computational efficiency and model performance.
 
 * Training: The linear SVM model was trained on the reduced feature set to classify the text data efficiently.
 
 * Hyperparameter Tuning: The tuning process involved:
 
   * Adjusting the number of components for TruncatedSVD to determine the optimal level of dimensionality reduction.
   
   * Fine-tuning the regularization parameter (C) of the SVM to balance the trade-off between achieving a low training error and a low testing error.
   
   * Exploring different ranges for n-grams to capture various levels of textual information.
   
   
# 4. Multinomial Naive Bayes
---
Multinomial Naive Bayes is particularly well-suited for text classification tasks due to its probabilistic nature. The steps taken include:

* Training: The Multinomial Naive Bayes model was trained to classify the text data based on the frequency of words or features.

* Hyperparameter Tuning: The primary focus was on adjusting the alpha parameter, which is the smoothing parameter. Smoothing is used to handle cases where a particular feature does not appear in the training set, thus avoiding zero probabilities.


# 5. Decision Tree Classifier
Decision tree classifiers are intuitive and easy to interpret models that make decisions based on the features of the input data. Here's how it was implemented:

 * Implementation: A decision tree classifier was implemented to create a model that splits the data based on the most significant features at each node.
 
* Hyperparameter Tuning: The model was optimized by adjusting parameters like the maximum depth of the tree, the minimum number of samples required to split a node, and the minimum number of samples required at a leaf node.

Each model was evaluated using metrics such as accuracy, precision, recall, and F1-score to determine the best-performing model for sentiment classification. The diverse range of models and techniques provides a comprehensive approach to tackling the sentiment analysis problem, ensuring robustness and reliability in the predictions.

 
 # LICENCE 
 ---
 This project is licensed under the MIT License - see the LICENSE file for details.
 
 
                         