import math


def calculateStats(numbers):
    hash1 = {"avg": None, "max": None, "min": None}
    if not numbers:
        hash1["avg"] = math.nan
        hash1["max"] = math.nan
        hash1["min"] = math.nan
    else:
        hash1["avg"] = sum(numbers) / len(numbers)
        hash1["max"]=max(numbers)
        hash1["min"]=min(numbers)
    return hash1


class EmailAlert:
    emailSent = None


class LEDAlert:
    ledGlows = None


class StatsAlerter():
    def __init__(self, maxThreshold, tuple_obj):
        self.maxThresh = maxThreshold
        self.email_obj = tuple_obj[0]
        self.led_obj = tuple_obj[1]

    def checkAndAlert(self, numbers):
        if max(numbers) > self.maxThresh:
            self.email_obj.emailSent = True
            self.led_obj.ledGlows = True
        else:
            self.email_obj.emailSent = False
            self.led_obj.ledGlows = False
