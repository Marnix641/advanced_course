class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)


    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


    def add_time(t1, t2):
        secs = t1.to_seconds() + t2.to_seconds()
        return MyTime(0, 0, secs)


    def between(self, t1, t2):
        target = self.to_seconds()
        t1s = t1.to_seconds()
        t2s = t2.to_seconds()
        if t1s < t2s:
            lowerbound = t1s
            upperbound = t2s
        else:
            lowerbound = t2s
            upperbound = t1s

        inbetween = False
        if lowerbound <= target < upperbound:
            inbetween = True
        return inbetween




