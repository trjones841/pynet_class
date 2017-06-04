#!/usr/bin/python2.7

"""

#189 days, 21:57:46.34 - 22:34:27 == 1640866634 timeticks

"""


def timeticks_2_time(timeticks):
    # Convert TimeTicks to days, hours:minutes.seconds
    d, h = divmod(timeticks, 8640000)
    h, m = divmod(h, 360000)
    m, s = divmod(m, 6000)
    s = s / 100

    print "\n%d days, %02d:%02d.%02d" % (d, h, m, s)
    time_list = [d, h, m, s]
    return time_list

    '''
    # Alternative Method
    import datetime
    s = uptime/100
    print datetime.timedelta(seconds=s)
    '''

def time_2_timeticks(d, h, m, s, l):

    time_tick = d*8640000+h*360000+m*6000+s*100+l
    return time_tick

if __name__ == "__main__":
    #timeticks_2_time(1640866634)
    #03:49:02
    t = time_2_timeticks(0, 3, 49, 2, 0)
    print "\ntimeticks: ", t
