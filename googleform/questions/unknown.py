from .base import Question
from googleform import utils


class UnknownQuestion(Question):
    def __init__(self, question_tree):
        super().__init__(question_tree)

    @staticmethod
    def is_this_question(tree):
        raise NotImplementedError(
            "This question is not recognized by googleform.")

    def serialize(self):
        raise NotImplementedError(
            "This question is not recognized by googleform.")

question = UnknownQuestion
