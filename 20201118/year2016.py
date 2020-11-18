import datetime


def solution(a, b):
    answer = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    date = datetime.datetime.strptime("2016-{}-{}".format(a, b), "%Y-%m-%d")
    date = date.weekday()
    return answer[date]
