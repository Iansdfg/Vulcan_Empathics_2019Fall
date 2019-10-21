from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
from statistics import stdev, mean
import json
import csv
subscription_key = "f56de4b340b6472f951a0b5b7cfc8f8c"

def get_sentiment_input(json_file):
    with open(json_file) as json_file:
        output_data = []
        input_data = json.load(json_file)
    count = 1
    for input_datum in input_data:
        output_datum = {}
        output_datum['id'] = count
        count += 1
        output_datum['text'] = input_datum['DisplayText']
        output_datum['time'] = input_datum['Offset']
        # time:
        output_data.append(output_datum)
    return output_data


def get_sentiment_score(documents, subscription_key, sentence_length = None):
    # subscription_key = "f56de4b340b6472f951a0b5b7cfc8f8c"
    credentials = CognitiveServicesCredentials(subscription_key)

    text_analytics_url = "https://westus2.api.cognitive.microsoft.com/"
    text_analytics = TextAnalyticsClient(endpoint = text_analytics_url, credentials = credentials)

    response = text_analytics.sentiment(documents = documents)
    all_dics, all_statistic_scores = [], []
    scores = []
    for pos, document in enumerate(response.documents):
        dic, statistic_score = {}, {}
        curr_score = float("{:.2f}".format(document.score))
        dic["Sentence"] = documents[pos]['text']
        dic["Time"] = documents[pos]['time']/10000000
        dic["Sentiment Score"] = curr_score

        scores.append(curr_score)
        dic['max_score'] = max(scores)
        dic['min_score'] = min(scores)
        dic['avg_score'] = mean(scores)
        dic['std_score'] = stdev(scores) if len(scores)>1 else scores[0]
        all_dics.append(dic)
        # print(dic)

    return all_dics
 

if __name__ == '__main__':
    document = [{'id': 1, 'text': 'OK.', 'time': 13600000, 'language': 'en'}, {'id': 3, 'text': "You know, I don't understand the radiation doctor.", 'time': 31600000, 'language': 'en'}]#, {'id': 1, 'text': 'When I had the seeds. Then he assured me that the whole issue was now in the rearview mirror. Those were his words, they were in the rearview mirror.', 'time': 84600000, 'language': 'en'}, {'id': 1, 'text': "And so now it's really sort of disappointing and maybe a little bit of a shock to hear the news. I'm suggesting that we have to actually look further. I can definitely see that I could definitely see that.", 'time': 195900000, 'language': 'en'}, {'id': 1, 'text': 'Probably makes you wonder about how much you can trust all this now.', 'time': 336000000, 'language': 'en'}, {'id': 1, 'text': "Well, yeah, obviously I can't trust anything, the last guy told me I mean? What happened did he screw it up.", 'time': 376300000, 'language': 'en'}, {'id': 1, 'text': "Well, we're going to do is we're going to go ahead. I really see how this is hard. We're going to go ahead and get the scan.", 'time': 465800000, 'language': 'en'}, {'id': 1, 'text': 'And find out what that tells us.', 'time': 552300000, 'language': 'en'}, {'id': 1, 'text': "And then based on that we'll go from there.", 'time': 579900000, 'language': 'en'}, {'id': 1, 'text': 'OK.', 'time': 616600000, 'language': 'en'}]
    results, statistic_score= get_sentiment_score(document,subscription_key)
    print(results, statistic_score)
    # for i in range(len(results)):
    #     print(results[i]['Time'], scores)