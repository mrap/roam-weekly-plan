# -*- coding: utf-8 -*-
import sys
import datetime


def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


def custom_strftime(fmt, t):
    return t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day))

def get_today():
    today = datetime.date.today()
    return tagged(custom_strftime("%B {S}, %Y", today))

def get_tomorrow():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    return tagged(custom_strftime("%B {S}, %Y", tomorrow))

def tagged(s):
    return '[[{s}]]'.format(s=s)

def next_week():
    today = datetime.date.today()
    next_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
    return [
        tagged(custom_strftime("%B {S}, %Y", next_monday + datetime.timedelta(days=i)))
        for i in range(0, 7)
    ]

def generate_template():
    week = next_week()
    template = """
{monday}
{tuesday}
{wednesday}
{thursday}
{friday}
{saturday}
{sunday}
    """.format(
        today=get_today(),
        tomorrow=get_tomorrow(),
        monday=week[0],
        tuesday=week[1],
        wednesday=week[2],
        thursday=week[3],
        friday=week[4],
        saturday=week[5],
        sunday=week[6],
    )
    return template


s = generate_template()
sys.stdout.write(s)
