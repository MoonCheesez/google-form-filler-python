from .base import Question
from googleform import utils


class UnknownQuestion(Question):
    def __init__(self, question_tree):
        # Do not call super() as it is not guaranteed that the superclass can
        # create attributes (e.g. id, title, description) based of the tree
        pass

    @staticmethod
    def is_this_question(tree):
        raise NotImplementedError(
            "This question is not recognized by googleform.")

    def serialize(self):
        return {}

question = UnknownQuestion
