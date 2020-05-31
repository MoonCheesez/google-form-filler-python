import abc
import re

from googleform import utils


def get_question_title(question_tree):
    # There is an extra space at the end of the class name to prevent matching
    # of the ItemItemTitleContainer class
    element = utils.xpath_freebird_div(question_tree, "ItemItemTitle ")

    # GoogleForm will add a space at the end of the question if it is required
    title = element[0].text.rstrip()

    return title


def get_question_desc(question_tree):
    elements = utils.xpath_freebird_div(question_tree, "ItemItemHelpText")

    desc = elements[0].text if elements else None
    return desc.rstrip() if desc else desc


def get_question_id(question_tree):
    xpath = ".//div[@data-item-id]"
    element = question_tree.xpath(xpath)[0]

    question_id = element.attrib["data-item-id"]

    return question_id


def get_entry_ids(question_tree):
    xpath = ".//*[starts-with(@name, 'entry')]"
    elements = question_tree.xpath(xpath)

    entry_ids = set()
    for element in elements:
        name = element.attrib["name"]
        # This regex removes trailing parts of the entry ids
        # entry.1234_month -> entry.1234
        entry_id = re.match(r"entry\.\d+", name).group(0)

        entry_ids.add(entry_id)

    return list(entry_ids)


def get_is_required(question_tree):
    xpath = ".//span[@class='freebirdFormviewerViewItemsItemRequiredAsterisk']"
    return bool(question_tree.xpath(xpath))


class Question(abc.ABC):
    def __init__(self, question_tree):
        self.tree = question_tree
        self.id = get_question_id(question_tree)
        self.entry_ids = get_entry_ids(question_tree)

        # Get the title and the description
        self.is_required = get_is_required(question_tree)
        self.title = get_question_title(question_tree)
        self.description = get_question_desc(question_tree)

    @staticmethod
    @abc.abstractmethod
    def is_this_question(tree):
        pass

    @abc.abstractmethod
    def serialize(self):
        pass
