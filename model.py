# Import libraries
import google.generativeai as genai

gemini_api_key = ""


def chat_with_gemini(query):
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content(query)
    return response.text


"""if __name__ == "__main__":
    query = "write me an tweet within two lines about latest tecnology in artifical intelligence with the tone of sarcasm"
    print(chat_with_gemini(query))"""
