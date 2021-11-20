from aws_costs_api.AWSCosts import AWSCosts

class CSV:

    def __init__(self):
        self.separator = ","

    def setSeparator(self, separator: str):
        self.separator = separator
        return self

    def setAWSCostsClass(self, awsCostsClass: AWSCosts):
        self.awsCosts = awsCostsClass
        return self

    def get(self) -> str:
        rawData = self.awsCosts.getCosts()

        stringData = ""

        for cellData in rawData["ResultsByTime"]:
            stringData += cellData["TimePeriod"]["Start"] + " - " + cellData["TimePeriod"]["Start"] + self.separator
            stringData += cellData["Total"]["BlendedCost"]["Amount"] + "\n"

        return stringData
