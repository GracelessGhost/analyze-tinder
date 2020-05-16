#!/usr/bin/env python3

"""
Based on code from https://repl.it/repls/WildAwfulDiscussions
"""

import json
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

# Year
def year(s):
    return s[:4]

# Main
def main():
    # Variables
    num_days_active = 0
    swipe_right = 0
    swipe_left = 0
    matches = 0
    message_sent = 0
    message_received = 0
    app_open = 0
    most_matches_in_day = 0
    most_passes_in_day = 0
    most_likes_in_day = 0
    most_messages_in_day = 0
    most_messages_received_in_day = 0
    most_app_open_in_day = 0

    # Read data
    f = open('data.json', 'r', encoding='utf8')
    data = json.load(f)
    first_day = list(data['Usage']['swipes_likes'].keys())[0] # String
    for key in data['Usage']['swipes_likes']:
        swipe_right += data['Usage']['swipes_likes'][key]
        if int(data['Usage']['swipes_likes'][key]) > most_likes_in_day:
            most_likes_in_day = int(data['Usage']['swipes_likes'][key])

    for key in data['Usage']['swipes_passes']:
        swipe_left += data['Usage']['swipes_passes'][key]
        if int(data['Usage']['swipes_passes'][key]) > most_passes_in_day:
            most_passes_in_day = int(data['Usage']['swipes_passes'][key])

    for key in data['Usage']['matches']:
        matches += data['Usage']['matches'][key]
        if int(data['Usage']['matches'][key]) > most_matches_in_day:
            most_matches_in_day = int(data['Usage']['matches'][key])

    for key in data['Usage']['messages_sent']:
        message_sent += data['Usage']['messages_sent'][key]
        if int(data['Usage']['messages_sent'][key]) > most_messages_in_day:
            most_messages_in_day = int(data['Usage']['messages_sent'][key])

    for key in data['Usage']['messages_received']:
        message_received += data['Usage']['messages_received'][key]
        if int(data['Usage']['messages_received'][key]) > most_messages_received_in_day:
            most_messages_received_in_day = int(
                data['Usage']['messages_received'][key])

    for key in data['Usage']['app_opens']:
        app_open += data['Usage']['app_opens'][key]
        if int(data['Usage']['app_opens'][key]) > 0:
            num_days_active += 1
        if int(data['Usage']['app_opens'][key]) > most_app_open_in_day:
            most_app_open_in_day = int(data['Usage']['app_opens'][key])

    # Do some math
    total_swipes = swipe_right + swipe_left
    first_day = dt.date(int(first_day[:4]), int(first_day[5:7]), int(first_day[8:]))
    num_days = dt.date.today() - first_day
    num_days = num_days.days # Convert to int
    swipes_per_day = total_swipes / num_days_active
    app_open_per_day = app_open / num_days

    # Print data
    print('\n')
    print('You joined Tinder on', first_day)
    print('Number of days since joining =', num_days)
    print('Number of days in which you opened Tinder =', num_days_active)
    print('\n')
    print('Total number of swipes =', total_swipes)
    print('Total times you swiped right =', swipe_right)
    print('Total times you swiped left =', swipe_left)
    print('Total number of matches =', matches)
    print('Total number of messages sent =', message_sent)
    print('Total number of messages recieved =', message_received)
    print('Total number of times opening Tinder =', app_open)
    print('\n')
    print('Match percent rate =', str(round(((matches / swipe_right) * 100), 2)) + '%')
    print('Ratio of swipe left to swipe right =', str(swipe_left // swipe_right) + ":1")
    print('Average swipes per day =', round(swipes_per_day, 2))
    print('Average times opening Tinder per day =', round(app_open_per_day, 2))
    print('\n')
    print('Most times opening Tinder in a day =', most_app_open_in_day)
    print('Most matches in a day =', most_matches_in_day)
    print('Most likes in a day =', most_likes_in_day)
    print('Most passes in a day =', most_passes_in_day)
    print('Most messages sent in a day =', most_messages_in_day)
    print('Most messages received in a day =', most_messages_received_in_day)

    # Graphs
    dates = list(data['Usage']['matches'].keys())
    x_axis = [dt.datetime.strptime(d,"%Y-%m-%d").date() for d in dates]
    y_axis = list(data['Usage']['matches'].values())

    fig, ax = plt.subplots(3, 1)
    fig.suptitle('My Tinder Data')
    plt.ylabel('Date')
    fig.tight_layout()
    plt.subplots_adjust(top=0.9, hspace=0.4)

    ax[0].plot(x_axis, y_axis)
    ax[0].tick_params('x', labelrotation=20)
    ax[0].set_ylabel('Matches')

    y_axis2 = np.array(list(data['Usage']['swipes_likes'].values()))

    ax[1].plot(x_axis, y_axis)
    ax[1].plot(x_axis, y_axis2)
    ax[1].tick_params('x', labelrotation=20)
    ax[1].set_ylabel('Likes and Matches')

    y_axis = np.array(list(data['Usage']['app_opens'].values()))

    ax[2].plot(x_axis, y_axis)
    ax[2].tick_params('x', labelrotation=20)
    ax[2].set_ylabel('App Opens')


    plt.show()

if __name__ == '__main__':
    main()