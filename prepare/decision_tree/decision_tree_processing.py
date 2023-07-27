from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import *
import xml.etree.ElementTree as ET


def decision_tree_to_xml(decision_tree, feature_names, class_names):
    # converts the tree to a text representation, see /resources/chatbot/decision_tree_example
    tree_text = export_text(decision_tree, feature_names=feature_names)

    lines = tree_text.split('\n')

    lines = [line.strip() for line in lines if line.strip()]

    root = ET.Element('DecisionTree')

    current_level = -1
    last_nodes = {0: root}
    id_counter = 1
    process_line(lines, root, current_level, last_nodes, id_counter)

    tree = ET.ElementTree(root)
    root.set('id', '0')

    root.set('classNames', ','.join(class_names))

    return ET.tostring(tree.getroot()).decode()


# recursive algorithm for processing the plain text decision tree into a xml based tree
# based on counting the levels of the tree and keeping track of current and parent nodes
def process_line(lines, parent_element, current_level, last_nodes, id_counter):
    while lines:
        line = lines[0]
        line_level = get_indentation_level(line)

        if line_level >= current_level:
            lines.pop(0)
            node = ET.SubElement(parent_element, 'Symptom')
            node.set('id', str(id_counter))
            id_counter += 1

            if 'class:' in line:
                class_name = get_node_class_name(line)
                node.tag = "Disorder"
                # class_element = ET.SubElement(node, 'Disorder')
                node.set('name', class_name)

            else:
                node.set('name', get_node_feature(line))
                node.set('answer', get_node_threshold(line))

                last_nodes[line_level] = node

                if lines and get_indentation_level(lines[0]) > line_level:
                    lines = process_line(lines, node, line_level + 1, last_nodes, id_counter)

        elif line_level < current_level:
            parent_node = last_nodes[line_level - 1]

            lines = process_line(lines, parent_node, line_level - 1, last_nodes, id_counter)

    return lines


# returns tree node depth
def get_indentation_level(line):
    return line.count('|')


# returns class (disorder) name if present in a string
def get_node_class_name(line):
    class_name = line.split('class: ')[1].strip()
    return class_name


# returns feature (symptom) name if present in a string
def get_node_feature(line):
    return line.split('|--- ')[1].split(' ')[0]


# returns a decision corresponding to the node
def get_node_threshold(line):
    if "<" in line:
        return "no"
    elif ">" in line:
        return "yes"
    else:
        return "class"
