import pytest

import googleform


@pytest.fixture(scope='function')
def test_form() -> googleform.GoogleForm:
    return googleform.get('https://docs.google.com/forms/d/1jzDkEha066GwSCcSrCg1yaJJLpJAk0_aIFwf6GQgmmU/viewform')


def test_integration(test_form: googleform.GoogleForm):
    """
    Test with a real live form,
    so we can catch change happening to the structure and name of classes
    """
    form_info = {
        "title": "Testing",
        "description": "This form is a test",
        "entry_ids": [
            'entry.1743417152',
            'entry.2006249624',
            'entry.849154821',
            'entry.1929660606',
            'entry.540883615',
        ],
    }

    assert test_form.title == form_info["title"]
    assert test_form.description == form_info["description"]
    assert [q.entry_ids[0] for q in test_form.questions] == \
        form_info["entry_ids"]

    for q in test_form.questions:
        print(q.id)
        print(q.__class__)
        print(q.title)
        print(q.description)

        if q.title == "Check boxes":
            print(q.options)
            assert ['Option 1', 'Option 2', 'Option 3'] == q.options
            q.answer(q.options[0])

        if q.title == "Choose from the list":
            print(q.options)
            q.answer(q.options[0])

        if q.title == "Answer that":
            print(q.options)
            q.answer(q.options[0])

        if q.title in ['Say whatever you want', 'Give me the long answer']:
            q.answer("whatever")

    test_form.submit()
