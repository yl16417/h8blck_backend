from googleapiclient import discovery
import os


def processRequest(textList):
    """
    Sends list of texts to Perspective API for analysis and returns their toxicity scores
    :param textList: The array of texts to analyse
    :return: A map from analysed texts to their corresponding toxicity scores
    """
    analysedTexts = []
    for text in textList:
        analysedTexts.append(makePerspectiveRequest(text))
    return analysedTexts


def makePerspectiveRequest(text):
    """
    Makes a request to Perspective API which returns a response of the form:
    {
        "attributeScores": {
            "TOXICITY": {
                "summaryScore": {
                    "value": 0.9208521,
                    "type": "PROBABILITY"
                }
            }
        },
        "languages": ["en"]
    }
    Extracts the toxicity score
    :param text: The text to analyse
    :return: The text mapped to its toxicity score
    """
    # Generates API client object dynamically based on service name and version.
    API_KEY = os.environ.get('PERSPECTIVE_API_KEY', None)
    if not API_KEY:
        return {"", ""}
    
    service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)
    
    analyze_request = {
        'comment': {'text': text},
        'languages': ['en'],
        'requestedAttributes': {'TOXICITY': {}}
    }
    
    response = service.comments().analyze(body=analyze_request).execute()
    toxicityScore = response['attributeScores']['TOXICITY']['summaryScore']['value']
    return {text: toxicityScore}
