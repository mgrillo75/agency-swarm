from agency_swarm.tools import BaseTool
from pydantic import Field
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

class AdvancedClassificationTechniques(BaseTool):
    """
    A tool that employs advanced classification techniques to categorize emails and other communications
    from vendors. It uses machine learning models to accurately classify and sort incoming messages based
    on content, urgency, and relevance.
    """

    model_data: dict = Field(
        ..., description="Pre-trained model data and configuration."
    )
    message: str = Field(
        ..., description="The content of the email or communication to classify."
    )

    def run(self):
        """
        Classifies the incoming message using a pre-trained machine learning model.
        """
        # Load model components
        vectorizer = TfidfVectorizer(vocabulary=self.model_data['vocabulary'])
        classifier = MultinomialNB()
        classifier.classes_ = np.array(self.model_data['classes'])
        classifier.class_count_ = np.array(self.model_data['class_count'])
        classifier.feature_count_ = np.array(self.model_data['feature_count'])
        classifier.class_log_prior_ = np.array(self.model_data['class_log_prior'])

        # Create a pipeline
        model = make_pipeline(vectorizer, classifier)

        # Predict the category of the message
        predicted_category = model.predict([self.message])[0]

        return f"The message has been classified as: {predicted_category}"

# Example usage:
# model_data = {
#     'vocabulary': {'urgent': 0, 'pay': 1, 'invoice': 2, 'meeting': 3, 'project': 4},
#     'classes': ['urgent', 'normal', 'low'],
#     'class_count': [10, 50, 5],
#     'feature_count': [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 2, 2, 2, 2]],
#     'class_log_prior': [-1.0986, -0.1823, -2.9957]
# }
# classifier_tool = AdvancedClassificationTechniques(
#     model_data=model_data,
#     message="Please review the urgent invoice for the recent project."
# )
# print(classifier_tool.run())