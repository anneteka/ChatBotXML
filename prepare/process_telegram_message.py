from prepare import telegram_database
from prepare.xml_processing import process_xml
from prepare.decision_tree import decision_tree as dt


def process_general_message(user_id, message_text):
    user, node, xml = telegram_database.get_user(user_id)
    if node == -2:
        # user has to use the /testing command
        return "Please start the testing using the /testing command."
    elif node == -1:
        # testing was started and this message text contains symptoms
        symptoms = process_xml.process_symptoms(message_text)
        print(symptoms)
        decision_tree = dt.get_decision_tree_text(symptoms)
        print(decision_tree)
        telegram_database.update_user(user_id, 0, decision_tree)
        child_type, child_node, child_id = process_xml.process_current_node(decision_tree, 0)
        question = process_xml.get_question(child_node)
        return "We will ask you questions now.\n" + question
    else:
        if node != 0:
            current_type, current_name = process_xml.node_id_data(xml, node)
            if current_type == "Disorder":
                print(current_name)
                return current_name  # process disorder message + start testing again

        answer = process_xml.process_answer(message_text)
        if answer is None:
            return "I don't understand. Please answer the question again"
        new_node_id = process_xml.get_next_node(xml, node, answer)
        print(new_node_id)
        child_type, child_name, child_id = process_xml.process_current_node(xml, new_node_id)
        print(child_name)
        if child_type == "Symptom":
            telegram_database.update_user(user_id, current_node=new_node_id)
            return process_xml.get_question(child_name)
        else:
            telegram_database.update_user(user_id, current_node=child_id)
            return child_name
            return


def get_disorder_message(disorder):
    return "disorder res"


def setup_user(user_id):
    telegram_database.create_user(user_id=user_id, xml_string="")
    print("user created with id " + str(user_id))


def start_testing(user_id):
    telegram_database.update_user(user_id=user_id, current_node=-1, xml="")
    print("testing started for user " + str(user_id))
