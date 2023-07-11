from lxml import etree as ET

tree = ET.parse('decision_tree.xml')
root = ET.Element("root")


#returns Node id and feature for the next question
#returns first question or diagnose

def generate_question(node_id: str, answer=None):
    #if there is no feature, we cant create a question but a Diagnose
    feature = tree.xpath(f"//*[@id={node_id}]/@feature")[0]
    feature_list = tree.xpath(f"//*[@id={node_id}]/@feature")

    if answer is not None:
        # is the actual node, the one which contains the received answer?
        # if so just create the question with the feature of the next node:
        # but still need to be able to check 2 arguments with xpath

        #problem is, what if the



        new_node_id = tree.xpath(f"//*[@feature={feature}][@answer={answer}]/@id")  #maybe need to change this
        #*** trying some things
        print(new_node_id)
        print(feature)
        print(tree.xpath(f"//*[@id{node_id}]/[@feature={feature}]/[@answer={answer}/@id"))
        #*** until here
        if len(tree.xpath(f"//*[@id={node_id}]/@feature")) != 0: # and int(new_node_id) >= int(node_id):
            next_feature = tree.xpath(f"//*[@id={new_node_id}]/@feature")[0]
            return question(next_feature)
        else:
            return generate_diagnose(new_node_id)
        """
        next_feature = tree.xpath(f"//*[@id={new_node_id}]/@feature")[0]
        next_feature_list = tree.xpath(f"//*[@id={node_id}]/@feature")
        print(new_node_id)
        # need to somehow make sure that the new_node_id is either the same node or the exact next possible node
        if len(next_feature_list) != 0 and int(new_node_id) >= int(node_id):
            return question(next_feature)
        else:
            return generate_diagnose(new_node_id)
        """


    else: #answer=None
        if len(feature_list) != 0:
            return question(feature)
        else:
            id = tree.xpath(f"//*[@id={node_id}]/@id")
            return generate_diagnose(id)

"""    
    if len(tree.xpath(f"//*[@id={node_id}]/@feature")) == 0:
        id = tree.xpath(f"//*[@id={node_id}]/@id")
        return generate_diagnose(id)
    else:
        feature =tree.xpath(f"//*[@id={node_id}]/@feature")
        # id = tree.xpath(f"//*[@id={node_id}]/@id")
        return question(feature)


def generate_question(node_id: str, answer: str):
    #get feature of id and then look for th node with the feature and the answer,
    # because the id provides one answer but there could be multipl enodes with dfferent answers
    feature = tree.xpath(f"//*[@id={node_id}/@feature")[0]
    new_node_id = tree.xpath(f"//*[@feature={feature}][@answer={answer}]/@id")
    return new_node_id


    if len(tree.xpath(f"//*[@id={node_id}]/@feature"))==0:
        id = tree.xpath(f"//*[@id={node_id}]/@id")
        return id

    else:
        feature =tree.xpath(f"//*[@id={node_id}]/@feature")
        id = tree.xpath(f"//*[@id={node_id}]/@id")
        return feature, id

"""


# if generate_questions returns an empty feature generate the diagnose
# node_id to identify the node in where the diagnose lies in

def generate_diagnose(node_id):
    diagnose = tree.xpath(f"//*[@id={node_id}]/Disorder/@name")
    if diagnose[0] == 'eating disorder':
        return f"You could have an {diagnose[0]}."
    if diagnose[0] == 'PDD':
        return f"You could have {diagnose[0]} (an pervasive developmental disorder)."
    if diagnose[0] == 'psychotic deprission':
        return f"You could have a {diagnose[0]}."
    if diagnose[0] == 'ADHD':
        return f"You could have {diagnose[0]} (attention deficit hyperactivity disorder)."
    if diagnose[0] == 'PTSD':
        return f"You could have {diagnose[0]} (post-traumatic stress disorder)."
    if diagnose[0] == 'anexiety':
        return f"You could have {diagnose[0]}."
    if diagnose[0] == 'MDD':
        return f"You could have a {diagnose[0]} (major depressive disorder)."
    if diagnose[0] == 'sleeping disorder':
        return f"You could have a {diagnose[0]}."
    if diagnose[0] == 'bipolar':
        return f"You could be {diagnose[0]}."
    if diagnose[0] == 'OCD':
        return f"You could have {diagnose[0]} (obsessive-compulsive disorder)."
    if diagnose[0] == 'Loneliness':
        return f"You could be suffering off of {diagnose[0]}."
    if diagnose[0] == 'ASD':
        return f"You could be suffering off of {diagnose[0]} (autism spectrum disorder)."

# need to adapt the grammar of the question to each feature
def question(feature):
    if feature == 'having_trouble_in_sleeping':
        question = "Do you have trouble in sleeping?"
        return question
    if feature == 'hopelessness':
        question = "Do you feel hopelessness?"
        return question
    if feature == 'social_media_addiction':
        question = "Do you have a social media addiction?"
        return question
    if feature == 'social_media_addiction':
        question = "Do you have a social media addiction?"
        return question
    if feature == 'avoids_people_or_activities':
        question = "Do you avoid people or activities?"
        return question
    if feature == 'close_friend':
        question = "Do you have close friend's?"
        return question
    if feature == 'blamming_yourself':
        question = "Are you blamming yourself?"
        return question
    if feature == 'introvert':
        question = "Are you an introvert?"
        return question
    if feature == 'breathing_rapidly':
        question = "Do you breath rapidly?"
        return question
    if feature == 'increased_energy':
        question = "Do you feel increased energy?"
        return question
    if feature == 'feeling_negative':
        question = "Do you have the symptom of often feeling negative?"
        return question
    if feature == 'popping_up_stressful_memory':
        question = "Do you get popping up stressful memory?"
        return question
    if feature == 'having_nightmares':
        question = "Do you have nightmares?"
        return question


def all_features():
    features = tree.xpath(f"//@feature")
    return set(features)

def all_diagnoses():
    diagnoses = tree.xpath(f"//@name")
    return set(diagnoses)


if __name__ == '__main__':
    # example to work with
    id='1'   #introvert
    diagnose_id = "17" # do you feel increased energy?
    message2 = 'no'
    print(generate_question(diagnose_id, 'yes'))
    #print(all_diagnoses())
    #print(generate_question(diagnose_id))
    #print(generate_diagnose('5'))

    #print(question(id))




