from .base import Question


class DurationQuestion(Question):
    def __init__(self, question_tree):
        super().__init__(question_tree)

        self.hours = None
        self.minutes = None
        self.seconds = None

    @staticmethod
    def is_this_question(tree):
        xpath = """.//div[contains(
            @class,
            'freebirdFormviewerViewItemsTimeTimeInputs'
        ) and not(
            .//div[contains(
                @class,
                'freebirdFormviewerViewItemsTimeSelect'
            )]
        )]"""

        return bool(tree.xpath(xpath))

    def answer(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def serialize(self):
        # Duration questions should only have one entry id
        entry_id = self.entry_ids[0]

        return {
            "{}_hour".format(entry_id): self.hours,
            "{}_minute".format(entry_id): self.minutes,
            "{}_second".format(entry_id): self.seconds,
        }


question = DurationQuestion
