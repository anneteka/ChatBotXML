from lxml import etree as ET

# util scripts for working with retrieving data from xml files


# checks if the string is a valid answer that equals to yes or no and returns the accepted value for further processing
def process_answer(text):
    tree = ET.parse('../../resources/data/answers.xml')
    res = None
    try:
        text = str(text).lower().strip()
        res = tree.xpath(f"//KeyWords[@text='{text}']/../@answer")[0]
    except:
        ""
    return res


# generates a result message for the bot based on the disorder name
def generate_diagnose_message(diagnose):
    tree = ET.parse('../../resources/data/disorders.xml')
    text = tree.xpath(f"//*[@name='{diagnose}']/Message/@text")[0]
    link = tree.xpath(f"//*[@name='{diagnose}']/Link/@url")[0]
    return text+link+"\nUse /testing command to start the test again"


# parses a string to look for symptoms recognised by the algorithm and alternative symptoms equal to the recognised ones
def process_symptoms(text):
    tree = ET.parse('../../resources/data/symptoms.xml')
    text = str(text).lower().replace(" and ", ",")
    texts = text.split(",")
    res = []
    for symptom in texts:
        symptom = symptom.strip().lower()
        try:
            s = tree.xpath(f"//KeyWords[@text='{symptom}']/../@name")
            if s is not None and s != []:
                res.append(s[0])
        except:
            "do nothing"
    return res


# extracts a question text based on the symptom name
def get_question(symptom):
    tree = ET.parse('../../resources/data/symptoms.xml')
    res = tree.xpath(f"string(//*[@name='{symptom}']/Question/@text)")
    return res


# return node data by node id
def node_id_data(xml_text, node_id):
    tree = ET.fromstring(xml_text)
    name = tree.xpath(f"string(//*[@id='{node_id}']/@name)")
    node_type = tree.xpath(f"name(//*[@id='{node_id}'])")
    return node_type, name


# returns child node data by parent node id, is needed to determine next question or result
def process_current_node(xml_text, node_id):
    tree = ET.fromstring(xml_text)

    child_name = tree.xpath(f"string(//*[@id='{node_id}']/*/@name)")
    child_node_type = tree.xpath(f"name(//*[@id='{node_id}']/*)")
    child_id = tree.xpath(f"string(//*[@id='{node_id}']/*/@id)")
    return child_node_type, child_name, child_id


# determines next node by parent node id and user input answer
def get_next_node(xml_text, node_id, answer):
    tree = ET.fromstring(xml_text)
    new_id = tree.xpath(f"string(//*[@id='{node_id}']/*[@answer='{answer}']/@id)")
    return new_id

# print(process_answer("a lot"))
# print(process_symptoms("tired and sad,"))
# print(get_question("hallucinations"))
# print(findTextForSymptoms(""))
