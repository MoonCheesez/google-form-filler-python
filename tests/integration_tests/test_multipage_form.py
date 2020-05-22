#-*- coding: utf-8 -*-

import pytest

import googleform


@pytest.fixture(scope='function')
def test_form() -> googleform.GoogleForm:
    return googleform.get('https://docs.google.com/forms/d/e/1FAIpQLScubyZo07YYHuDT_J1yWEnp8awE260r78Dyu3SS2w18XCglCw/viewform')


def test_multipage(test_form: googleform.GoogleForm):
    """
    Test with a real live multi page form,
    so we can catch change happening to the structure and name of classes
    """

    print(test_form.title)
    for q in test_form.questions:
        print(q.title)
        if q.title == 'תאריך12 מילוי השאלון':
            from datetime import datetime
            now = datetime.now()
            q.answer(day=now.day, month=now.month, year=now.year)
        if q.title == 'שם מלא של הילד':
            q.answer('אודי חמודי הוא ילד נחמד')
        if q.title == 'ת.ז.':
            q.answer('12345678')
        if q.title == 'הריני מצהיר בזאת על היעדר תסמינים של ילדי:':
            print(q.options)
            [q.answer(o) for o in q.options]

    next_page = test_form.next()
    print(next_page.title)
    next_page = next_page.next()
    print(next_page.title)
    for q in next_page.questions:
        print(q.title)
        q.answer("ישראל פרוכטר")
    next_page.submit()
