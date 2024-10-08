import pickle

# Load your pre-trained model from a pickle file
with open('./models/tuned_rf_tf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the vectorizer
with open('./models/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)