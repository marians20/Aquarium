"""Scheduler"""

from time import sleep
from datetime import *
import threading
from .sun import Sun
from .execution_element import ExecutionElement
from .context import Context


class TimeInterval:
    """Abstractisation for a time interval"""

    def __init__(self, from_time, to_time):
        self.__FromTime = datetime.strptime(from_time, "%H:%M:%S").replace(tzinfo=Sun.tz)
        self.__ToTime = datetime.strptime(to_time, "%H:%M:%S").replace(tzinfo=Sun.tz)
    
    @property
    def FromTime(self):
        return self.__FromTime

    @FromTime.setter
    def FromTime(self, value):
        self.__FromTime = value

    @property
    def ToTime(self):
        return self.__ToTime

    @ToTime.setter
    def ToTime(self, value):
        self.__ToTime = value

    def Belongs(self, value):
        return self.FromTime <= value and self.ToTime >= value

class DailySchedule:
    def __init__(self, executionElement_id):
        self.__ExecutionElementId = executionElement_id
        self.__Intervals = [
            TimeInterval("07:00:00", "09:00:00"),
            TimeInterval("17:00:00", "22:00:00")
        ]

    @property
    def ExecutionElementId(self):
        return self.__ExecutionElementId

    @property
    def Intervals(self):
        return self.__Intervals

    def On(self):
        now = datetime.strptime(Sun.Now().strftime("%H:%M:%S"), "%H:%M:%S").replace(tzinfo=Sun.tz)
        for interval in self.Intervals:
                return True
        return False
        
class Scheduler(threading.Thread):
    """Scheduler"""
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_required = False
        self.context = Context()
        self.IsDay = Sun.IsDay()
        self.IsRunning = False
        self.Schedules = []
        for executionElement in self.context.ExecutionElements:
            if executionElement.Id != 0:
                sch = DailySchedule(executionElement.Id)
                self.Schedules.append(sch)

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
            self.set_automatic_values()
            sleep(1)
        self.stop_required = False
        self.IsRunning = False

    def set_automatic_values(self):       
        for scheduler in self.Schedules:
            if scheduler.On():
                self.Context[scheduler.ExecutionElementId].AutomaticValue = 1
            else:
                self.Context[scheduler.ExecutionElementId].AutomaticValue = 0

            print("Execution Element Id " + str(scheduler.ExecutionElementId) + " status is " + str(self.Context[scheduler.ExecutionElementId].AutomaticValue))
                

global sch
sch = Scheduler()
sch.start()