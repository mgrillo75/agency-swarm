from agency_swarm.tools import BaseTool
from pydantic import Field
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

class AdvancedClassificationTechniques(BaseTool):
    """
    AdvancedClassificationTechniques applies advanced machine learning classification techniques to categorize
    client interactions based on their content, intent, and urgency.
    """

    interaction_text: str = Field(
        ..., description="The text of the client interaction to be classified."
    )
    model: MultinomialNB = Field(
        ..., description="The pre-trained Naive Bayes classifier model used for categorization."
    )
    vectorizer: TfidfVectorizer = Field(
        ..., description="The TF-IDF vectorizer used to convert text data into a format suitable for the model."
    )

    def run(self) -> dict:
        """
        Categorizes a client interaction using a Naive Bayes classifier based on the interaction's text.
        
        Returns:
            A dictionary containing the predicted categories for content, intent, and urgency.
        """
        # Vectorize the interaction text
        text_vector = self.vectorizer.transform([self.interaction_text])
        
        # Predict the categories
        predicted_categories = self.model.predict(text_vector)
        
        # Assuming the model is trained to predict multiple labels
        categories = {
            'content': predicted_categories[0],
            'intent': predicted_categories[1],
            'urgency': predicted_categories[2]
        }
        
        return categories

# Example usage of the tool with hypothetical pre-trained model and vectorizer
# vectorizer = TfidfVectorizer()
# model = MultinomialNB()
# tool_instance = AdvancedClassificationTechniques(
#     interaction_text="I need help with my recent order, it's urgent!",
#     model=model,
#     vectorizer=vectorizer
# )
# print(tool_instance.run())