from .base import Question
from googleform import utils


def get_options(tree):
    xpath = (".//label[contains(@class,"
             "'freebirdFormviewerViewItemsRadioChoice')]//span")

    return utils.get_elements_text(tree, xpath)


def has_other_option(tree):
    return utils.has_freebird_div(tree, "RadioOtherChoice")


class RadioListQuestion(Question):
    def __init__(self, question_tree):
        super().__init__(question_tree)

        self.options = get_options(self.tree)
        self._answer = None
        self._other_answer = None
        self.has_other_option = has_other_option(self.tree)

    @staticmethod
    def is_this_question(tree):
        return utils.has_freebird_div(tree, "RadioOption")

    def answer(self, option_name):
        self._answer = option_name

    def answer_other(self, other_answer):
        if not self.has_other_option:
            raise ValueError("The RadioListQuestion does not have an 'other' "
                             "option")
        self._answer = "__other_option__"
        self._other_answer = other_answer

    def serialize(self):
        # Radio list questions should only have one entry id
        entry_id = self.entry_ids[0]

        serialized_payload = {
            entry_id: self._answer,
        }

        if self._answer == "__other_option__":
            other_option_key = entry_id + ".other_option_response"
            serialized_payload[other_option_key] = self._other_answer

        return serialized_payload


question = RadioListQuestion
