# http://blog.thedigitalcatonline.com/blog/2014/05/19/method-overriding-in-python/


""" Summary

Call the original implementation of a method you are overriding whenever possible. This makes the underlying API work as expected. When in need of skipping the call be sure to document the reasons.

Always use super() to call the original implementation of a method. This respects the resolution order in case of multiple inheritance and protects from changes in the class hierarchy.

If you call to the original implementation of a method do it as soon as you have all the data you need to run it.

"""


""" An example of basic overriding """


class Parent(object):
    def __init__(self, value=5):
        self.value = value

    def get_value(self):
        return self.value


class Child(Parent):
    def get_value(self):
        super().get_value()
        return self.value ** 2


c = Child()
print(c.get_value())
# 25


""" An example of pre-filtering """


import datetime


class Logger(object):
    def log(self, message):
        print(message)


class TimestampLogger(Logger):
    def log(self, message):
        message = f"{datetime.datetime.now().isoformat()} {message}"
        super().log(message)


l = Logger()
l.log("hi!")
# hi!

t = TimestampLogger()
t.log("hi!")
# 2019-01-25T10:02:37.316259 hi!


""" An example of post-filtering """


import os


class FileCat(object):
    def cat(self, filepath):
        with open(filepath) as f:
            lines = f.readlines()
        return lines


class FileCatNoEmpty(FileCat):
    def cat(self, filepath):
        lines = super().cat(filepath)
        nonempty_lines = [l for l in lines if l != "\n"]
        return nonempty_lines
