
![Screenshot 2024-08-16 161130](https://github.com/user-attachments/assets/288da99d-6304-4caa-b306-b44eb19b7c82)


 # OVERVIEW 

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
The dataset for this analysis is sourced from Yelp and contains detailed food reviews. It encompasses a total of 429,771 rows and 8 columns, structured in a wide format.

Dataset Overview: Source: Yelp Website Total Rows:429,771 Total Columns: 8 Column Details:

Review_id: A unique identifier assigned to each review. Data Type: Integer (object)

User_ID: A unique identifier assigned to each user. Data Type: Integer (object)

Business_id : A unique identifier assigned to each Business. Data Type: String (object)

Stars: The ratings of reviews. Data Type: String (int64)

Useful: Categorization of the review. Data Type: String (int64)

Fuuny: Categorization of the review. Data Type: String (int64)

Cool: Categorization of the review Data Type: Integer (int64)

Text: The review. Data Type: Float (float64)

Date: Date when the review was written. Data Type: Integer (float64)


# MODELLING 

---
 To classify the sentiment of reviews, multiple machine learning models were implemented and optimized using hyperparameter tuning. Each model brings its own strengths to the task, and their performance was assessed based on various evaluation metrics.
 
 
The data preprocessing steps taken for this project included:

1. Splitting the data between the target and features
2. Label Encoding the target
3. Vectorising the data using TFIDF Vectoriser
4. Using SMOTE to avoid bias in the data
5. Split the data using Train-Test Split of 80-20

Additionally the models in the modelling section include:
1. Logistic Regression
2. Random Forest Classifier
3. Linear Support Vector Machine
4. Multinomial Bayes
5. Decision Trees Classifier

The tuned Random Forest offered both the highest accuracy score as well as the highest recall. We will use the model in our deployment.

# Deployment 
---

We processed text data by encoding the review categories and vectorizing the text using TF-IDF. Then, we balanced the dataset using SMOTE to handle class imbalances. After splitting the data into training and testing sets, we trained a Random Forest classifier on the processed data and saved both the vectorizer and the trained model for future use.
 

 
 
                         
