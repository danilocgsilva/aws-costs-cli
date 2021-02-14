class FormatSingle:

    def __init__(self, singleData: dict):
        self.data = singleData

    def getMonthDay(self):
        fullData = self.data["TimePeriod"]["Start"]
        return fullData[5:]

    def getAmount(self):
        stringAmountData = self.data["Total"]["BlendedCost"]["Amount"]
        return float(stringAmountData)

    def getAmountUnit(self):
        return self.data["Total"]["BlendedCost"]["Unit"]
