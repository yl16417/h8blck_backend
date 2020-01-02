from googleapiclient import discovery
import os


def processRequest(data):
    """
    Sends list of texts to Perspective API for analysis and returns their toxicity scores
    :param: data The array of texts to analyse
    :return: A map from analysed texts to their corresponding toxicity scores
    """
    return {data[0]: makePerspectiveRequest(data[0], data[1])}


def makePerspectiveRequest(text, keyNum):
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
    API_KEY = os.environ.get('PERSPECTIVE_API_KEY_' + keyNum, None)
    if not API_KEY:
        return {"", ""}
    
    service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)
    
    analyze_request = {
        'comment': {'text': text},
        'languages': ['en'],
        'requestedAttributes': {'TOXICITY': {}}
    }
    
    response = service.comments().analyze(body=analyze_request).execute()
    return response['attributeScores']['TOXICITY']['summaryScore']['value']
