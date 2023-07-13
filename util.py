from Response import Response

# this function creates a dictionary where the key is the bot response and the value is the Response class
def initializeResponses():
    # Responses -------------------------------------------------------------------------------------------------------
    responses = {}
    responses['Hello!'] = Response(['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    responses['See you!']=Response(['bye', 'goodbye'], single_response=True)
    responses['I\'m doing fine, and you?']=Response(['how', 'are', 'you', 'doing'], required_words=['how'])
    responses['You\'re welcome!']=Response(['thank', 'thanks'], single_response=True)
    responses['Thank you!']=Response(['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    responses['What symptoms do you have?']=Response(['feeling', 'well', 'not', 'good', 'been'], required_words=['not', 'feeling'])
    responses['And what is your age?']=Response( ['feeling_nervous', 'panic', 'breathing_rapidly', 'sweating', 'trouble_in_concentration', 'having_trouble_in_sleeping', 'having_trouble_with_work', 'hopelessness', 'anger', 'over_react', 'change_in_eating', 'suicidal_thought', 
            'feeling_tired', 'close_friend', 'social_media_addiction', 'weight_gain', 'introvert', 'popping_up_stressful_memory',
            'having_nightmares', 'avoids_people_or_activities', 'feeling_negative', 'trouble_concentrating', 'blamming_yourself',
            'hallucinations', 'repetitive_behaviour', 'seasonally', 'increased_energy'], db = True)
    return responses

# initialize symptom questions so the Bot is clear to the user
def initializeSymptomsQuestions():
    questions = {
        "having_trouble_in_sleeping" : "Do you have trouble sleeping?", 
        "hopelessness" : "Do you feel hopelessness?",
        "social_media_addiction" : "Do you have a social media addiction?", 
        "avoids_people_or_activities" : "Do you avoid people or activities?", 
        "close_friend" : "Do you have close friends?", 
        "blamming_yourself" : "Do you blame yourself?",
        "introvert" : "Are you an introvert?",
        "breathing_rapidly" : "Do you have a rapid breath?",
        "increased_energy" : "Do you feel increased energy?",
        "feeling_negative" : "Do you have a negative feeling?",
        "popping_up_stressful_memory" : "Do you get popping up stressful memory?",
        "having_nightmares" : "Do you have nightmares?",
        "feeling_nervous" : "Have you been feeling nervous?",
        "panic" : "Do you feel panicked?",
        "sweating" : "Have you been sweating a lot lately?", 
        "trouble_in_concentration" : "Have you had trouble in concentrating?",
        "having_trouble_with_work" : "Are you having trouble at work?",
        "anger" : "Have you been feeling angry?",
        "over_react" : "Do you feel like you have been overreacting to things lately?",
        "change_in_eating" : "Do you see any change in eating?",
        "suicidal_thought" : "Do you have suicidal thoughts?",
        "feeling_tired" : "Have you been feeling tired?",
        "weight_gain" : "Have you gained weight recently?",
        "trouble_concentrating" : "Do you have trouble concentrating?",
        "hallucinations" : "Do you get hallucinations?",
        "repetitive_behaviour" : "Do you notice repetitive behaviours?",
        "seasonally" : "Do you feel like this seasonally?"
    }
    return questions