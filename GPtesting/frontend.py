from ProjectTestingRun.backend import get_activity_from_db
import random
from collections import Counter
import itertools
from ProjectTestingRun.backend import get_activity_from_db


# record = []

# @views.route('/regulation_toolbox/<zones_ID>')
def get_suggestion():
    suggestion = random.choice(get_activity_from_db())
    print(suggestion)

# def record_add_count(answer):
#     record.append(answer)
#     count_answer = Counter(record)
#     items = count_answer.items()
#     for item in items:
#         print(item)
#     return items
#
# def repeat_count(answer):
#     total = []
#     tryAgain = input('Would you like to try another activity? y/n')
#     while tryAgain == 'y':
#         get_suggestion(answer)
#         record_add_count(answer)
#     else:
#         print('Hope you are feeling better!')
#     return total
#
# def restart_process(answer):
#     get_suggestion(answer)
#     record_add_count(answer)
#     repeat_count(answer)
#     new_total = itertools.chain(repeat_count, record_add_count)
#     return new_total

