from prepare.telegram import telegram_database
from prepare.xml_processing import process_xml
from prepare.decision_tree import decision_tree as dt

# service file for working with the incoming user messages, additional logic layer between the ui logic and the database logic

# incoming messages processing logic is stored here
def process_general_message(user_id, message_text):
    user, node, xml = telegram_database.get_user(user_id)
    if node == -2:        # testing has not started, user has to use the /testing command
        return "Please start the testing using the /testing command."
    elif node == -1:         # testing was started and this message text contains symptoms
        symptoms = process_xml.process_symptoms(message_text)
        decision_tree = dt.get_decision_tree_text(symptoms)
        telegram_database.update_user(user_id, 0, decision_tree)
        child_type, child_node, child_id = process_xml.process_current_node(decision_tree, 0)
        question = process_xml.get_question(child_node)
        return "We will ask you questions now.\n" + question
    else: # this message contains an answer to a previously asked question
        if node != 0:
            current_type, current_name = process_xml.node_id_data(xml, node)
            if current_type == "Disorder":
                return get_disorder_message(current_name)  # process result message + offer to start testing again
        # processes the answer based on a /resources/data/answers.xml file
        answer = process_xml.process_answer(message_text)
        if answer is None:
            return "I don't understand. Please answer the question again"
        new_node_id = process_xml.get_next_node(xml, node, answer)
        child_type, child_name, child_id = process_xml.process_current_node(xml, new_node_id)
        if child_type == "Symptom": # asks next question
            telegram_database.update_user(user_id, current_node=new_node_id)
            return process_xml.get_question(child_name)
        else: # process result message + offer to start testing again
            telegram_database.update_user(user_id, current_node=child_id)
            return get_disorder_message(child_name)


def get_disorder_message(disorder):
    return process_xml.generate_diagnose_message(disorder)


def setup_user(user_id):
    telegram_database.create_user(user_id=user_id, xml_string="")
    print("user created with id " + str(user_id))


def start_testing(user_id):
    telegram_database.update_user(user_id=user_id, current_node=-1, xml="")
    print("testing started for user " + str(user_id))
