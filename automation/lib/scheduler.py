"""Scheduler"""

import time
import threading
from .sun import Sun
from .execution_element import ExecutionElement
from .context import Context

class Scheduler(threading.Thread):
    """Scheduler"""
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_required = False
        self.context = Context()
        self.IsDay = Sun.IsDay()
        self.IsRunning = False

    def run(self):
        self.do_job()

    @property
    def IsRunning(self):
        return self.__IsRunning
    @IsRunning.setter
    def IsRunning(self, value):
        self.__IsRunning = value

    @property
    def IsDay(self):
        return self.__IsDay
    @IsDay.setter
    def IsDay(self, value):
        self.__IsDay = value

    @property
    def Context(self):
        return self.context

    def stop(self):
        """Stop thread"""
        if self.IsRunning:
            self.stop_required = True

    def do_job(self):
        """The task"""
        self.IsRunning = True
        while not self.stop_required:
            self.IsDay = Sun.IsDay()
            self.context["ColdLight"].AutomaticValue = self.IsDay
            self.context["WarmLight"].AutomaticValue = not self.IsDay
            time.sleep(1)
        self.stop_required = False
        self.IsRunning = False

sch = Scheduler()
sch.start()