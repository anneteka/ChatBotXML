from lxml import etree as ET
tree = ET.parse('decision_tree.xml')
symptoms = ET.parse('resources/symptoms.xml')
def generate_question(node_id: str, answer=None):
    """
    This function, returns corresponding question or diagnose for a Node

    if both id and answer will be given, the function will return the new id and the question (or diagnose)
    if only the id is given it will return the corresponding question (or diagnose)
    """
    # important!
    # if we have an argument "name" in a node, we kow we are at a Disorder-Diagnose node
    #
    # if we do not have an answer given we "just" need to return the question to the feature of node_id given.

    if answer is not None:
        if answer == tree.xpath(f"//*[@id='{node_id}']/@answer")[0]:
            #answer == node_answer
            child_nodes = tree.xpath(f"//*[@id='{node_id}']/*/@id")
            print(child_nodes)
            return get_question_or_diagnose(child_nodes)

        else:
            parent_node_id = tree.xpath(f"//*[@id='{node_id}']/../@id")[0]
            sibling_id = get_sibling_id(parent_node_id, node_id)
            sibling_childs = tree.xpath(f"//*[@id='{sibling_id}']/*/@id")
            print(sibling_childs)

            return get_question_or_diagnose(sibling_childs)
    else:
        # get feature or name of current id:
        if len(tree.xpath(f"//*[@id='{node_id}']/@feature")) != 0:
            feature = tree.xpath(f"//*[@id='{node_id}']/@feature")
            return question(feature[0])
        else:
            name = tree.xpath(f"//*[@id='{node_id}']/@name")
            return generate_diagnose(name[0])

    #add exception, if id tag is Disorder we cannot take a answer argument


def get_sibling_id(parent, node_id):
    sibling_nodes_id = tree.xpath(f"//*[@id={parent}]/*/@id")
    sibling_nodes_id.remove(str(node_id))
    sibling_id = sibling_nodes_id[0]
    return sibling_id

def get_question_or_diagnose(list):
    if len(list) > 1:
        question_feature = tree.xpath(f"//*[@id={list[0]}]/@feature")
        print(question_feature[0])
        return question(question_feature[0])
    else:
        disorder_name = tree.xpath(f"//*[@id={list[0]}]/@name")
        return generate_diagnose(disorder_name[0])



# if generate_questions returns an empty feature generate the diagnose
# node_id to identify the node in where the diagnose lies in
def generate_diagnose(name):  # change diagnose to name
    disorders = ET.parse('resources/disorders.xml')
    xpath = f"string(//*[@name='{name}']/Message/@diagnose)"
    xpath_1 = f"string(//*[@name='{name}']/Message/@text)"
    xpath_2 = f"string(//*[@name='{name}']/Link/@description)"
    xpath_3 = f"string(//*[@name='{name}']/Link/@url)"

    diagnose = disorders.xpath(xpath)
    text = disorders.xpath(xpath_1)
    description = disorders.xpath(xpath_2)
    url = disorders.xpath(xpath_3)

    message = diagnose+"\n"+text+"\n"+description+"\n"+url
    return message


# need to adapt the grammar of the question to each feature
def question(feature):
    # xpath to find attribute: "//*[@name={feature}]/child::Question/@text"
    # xpath to extract value of attribute:
    xpath = f"string(//*[@name='{feature}']/Question/@text)"
    return symptoms.xpath(xpath)



def all_features():
    features = tree.xpath(f"//@feature")
    return set(features)

def all_diagnoses():
    diagnoses = tree.xpath(f"//@name")
    return set(diagnoses)






