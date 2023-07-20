from lxml import etree as ET


def process_answer(text):
    tree = ET.parse('resources/answers.xml')
    text = str(text).lower().strip()
    res = tree.xpath(f"//KeyWords[@text='{text}']/../@answer")[0]
    return res


def process_symptoms(text):
    tree = ET.parse('resources/symptoms.xml')
    text = str(text).lower().replace(" and ", ",")
    texts = text.split(",")
    res = []
    for symptom in texts:
        symptom = symptom.strip().lower()
        s = tree.xpath(f"//KeyWords[@text='{symptom}']/../@name")
        if s is not None and s != []:
            res.append(s[0])
    return res


def get_question(symptom):
    tree = ET.parse('resources/symptoms.xml')
    res = tree.xpath(f"//Symptom[@name='{symptom}']/Question/@text")[0]
    return res

def node_id_data(xml_path, node_id):
    tree = ET.parse(xml_path)
    name = tree.xpath(f"//*[@id='{node_id}']/@name")[0]
    node_type = tree.xpath(f"name(//*[@id='{node_id}'])")
    return node_type, name


def process_current_node(xml_path, node_id):
    tree = ET.parse(xml_path)
    node = tree.xpath(f"//*[@id='{node_id}']")
    child_name = tree.xpath(f"//*[@id='{node_id}']/*/@name")[0]
    child_node_type = tree.xpath(f"name(//*[@id='{node_id}']/*)")
    return child_node_type, child_name


def get_next_node(xml_path, node_id, answer):
    tree = ET.parse(xml_path)
    res = tree.xpath(f"//*[@id='{node_id}']/*[@answer='{answer}']/@id")
    question = ""
    new_id = ""
    return new_id, question

# print(process_answer("a lot"))
# print(process_symptoms("tired and sad,"))
# print(get_question("hallucinations"))
# print(findTextForSymptoms(""))
print(process_current_node('../resources/chatbot/decision_tree.xml', "9"))
print(process_current_node('../resources/chatbot/decision_tree.xml', "1"))
print()
print(node_id_data('../resources/chatbot/decision_tree.xml', "9"))
print(node_id_data('../resources/chatbot/decision_tree.xml', "1"))