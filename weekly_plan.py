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
{{{{[[embed]]: ((((Aq3fgyLxo))))}}}}
{{{{[[query]]: {{and: [[Daily Design]] {today} }}}}}}
## [[DoingToday]]
    Daily Practice
    Morning Journal
    Add todos from linked references
    List and rank tasks
    Daily Design
## [[DoneToday]]
# Journal
    ## [[Morning Journal]] {{{{word-count}}}}
        [[Meditation Reflection]]
        [[What did I read about?]]
        [[Writing Exercise: Free Write]]
        [[What am I grateful for?]]
        [[What's on my mind?]]
            [[What am I excited about?]]
            [[What am I worried about?]] / [[What's bothering me?]]
            [[Is there anything I'm forgetting?]]
        [[What do I feel like creating?]]
        [[Daily Design]]
        [[Health Sitrep]]
    ## [[Evening Reflection]] {{{{word-count}}}}
        [[Evening Brain Dump]]
        [[How are you feeling today?]]
        [[What could you have done better?]]
        [[Amazing things that happened]]
        [[What did you learn today?]]
        [[Tomorrow's Tasks]] {tomorrow}
        [[Tonight's Play]]
        [[Positivity Score]]
        [[Daily Design Recap]]
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
