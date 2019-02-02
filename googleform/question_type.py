from enum import Enum

import _internal_util


class QUESTION_TYPE(Enum):
    SHORT_TEXT = "stext"
    LONG_TEXT = "ltext"

    RADIO_LIST = "radiolist"
    RADIO_SCALE = "radioscale"

    CHECKBOX = "checkbox"

    TIME = "time"
    DURATION = "duration"

    DATE = "date"
    DATE_YEAR_MODIFIER = "y"
    DATE_TIME_MODIFIER = "t"
    DATE_YEAR = DATE + DATE_YEAR_MODIFIER
    DATE_TIME = DATE + DATE_YEAR_MODIFIER
    DATE_YEAR_TIME = DATE + DATE_YEAR_MODIFIER + DATE_TIME_MODIFIER

    DROPDOWN = "dropdown"


def get_question_type(question_tree):
    xpaths = {
        # Text Questions
        QUESTION_TYPE.SHORT_TEXT:
            _internal_util.get_freebird_class_div("TextShortText"),
        QUESTION_TYPE.LONG_TEXT:
            _internal_util.get_freebird_class_div("TextLongText"),

        # List Select Questions
        QUESTION_TYPE.RADIO_LIST:
            """.//content[@role='presentation']
                /div[not(@class='freebirdMaterialScalecontentContainer')]
            """,
        QUESTION_TYPE.RADIO_SCALE:
            ".//div[@class='freebirdMaterialScalecontentContainer']",

        QUESTION_TYPE.CHECKBOX:
            _internal_util.get_freebird_class_div("CheckboxChoice"),
        QUESTION_TYPE.DROPDOWN:
            _internal_util.get_freebird_class_div("SelectSelect"),

        QUESTION_TYPE.DURATION:
            """.//div[contains(
                @class,
                'freebirdFormviewerViewItemsTimeTimeInputs'
            ) and not(
                .//div[contains(
                    @class,
                    'freebirdFormviewerViewItemsTimeSelect'
                )]
            )]""",
        QUESTION_TYPE.TIME:
            """.//div[contains(
                @class,
                'freebirdFormviewerViewItemsTimeTimeInputs'
            )]//div[contains(
                @class,
                'freebirdFormviewerViewItemsTimeSelect'
            )]
            """,
    }

    for question_type, xpath in xpaths.items():
        if question_tree.xpath(xpath):
            return question_type

    date_xpath = _internal_util.get_freebird_class_div("DateDateInput")
    time_xpath = _internal_util.get_freebird_class_div("DateTimeInputs")
    year_xpath = _internal_util.get_freebird_class_div("DateYearInput")

    question_type = None
    if question_tree.xpath(date_xpath):
        question_type = QUESTION_TYPE.DATE
        if question_tree.xpath(year_xpath):
            question_type += QUESTION_TYPE.DATE_YEAR_MODIFIER
        if question_tree.xpath(time_xpath):
            question_type += QUESTION_TYPE.DATE_TIME_MODIFIER

    return question_type
