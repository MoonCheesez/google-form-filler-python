from .base import Question


class TimeQuestion(Question):
    def __init__(self, question_tree):
        super().__init__(question_tree)

        self.hour = None
        self.minute = None

    @staticmethod
    def is_this_question(tree):
        xpath = """.//div[contains(
            @class,
            'freebirdFormviewerViewItemsTimeTimeInputs'
        )]//div[contains(
            @class,
            'freebirdFormviewerViewItemsTimeSelect'
        )]
        """

        return bool(tree.xpath(xpath))

    def answer(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def serialize(self):
        # Time questions should only have one entry id
        entry_id = self.entry_ids[0]

        return {
            "{}_hour".format(entry_id): self.hour,
            "{}_minute".format(entry_id): self.minute,
        }


question = TimeQuestion
