from lxml import etree as ET


def process_answer(text):
    tree = ET.parse('resources/answers.xml')
    root = ET.Element("root")
    text = str(text).lower()
    res = tree.xpath(f"//KeyWords[@text='{text}']/../@answer")[0]
    return res


def process_symptoms(text):
    tree = ET.parse('resources/symptoms.xml')
    root = ET.Element("root")
    text = str(text).lower().replace(" and ", ",")
    texts = text.split(",")
    res = []
    for symptom in texts:
        symptom = symptom.strip().lower()
        s = tree.xpath(f"//KeyWords[@text='{symptom}']/../@name")
        if s is not None and s != []:
            res.append(s[0])

    return res


print(process_answer("a lot"))
print(process_symptoms("tired and sad,"))
