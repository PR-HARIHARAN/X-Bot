import tweepy
#import google.generativeai as genai

from model import chat_with_gemini as cwg
api_key = ""
api_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


query = "help me to write a tweet within 2 lines about machine learning with sarcasm with emojis "
client.create_tweet(text=cwg(query))


#gemini_api_key = "AIzaSyBwljeKkqwLbuy6k5_P2_VFBhV9uCYNKxw"


"""def chat_with_gemini(query):
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content(query)
    return response.text


if __name__ == "__main__":
    query = "write me an tweet within two lines about latest tecnology in artifical intelligence with the tone of sarcasm"
    print(chat_with_gemini(query))"""



