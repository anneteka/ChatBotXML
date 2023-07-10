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