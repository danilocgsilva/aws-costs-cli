from aws_costs_api.AWSCosts import AWSCosts

class CSV:

    def __init__(self):
        self.separator = ","
        self.awsCosts = None

    def setSeparator(self, separator: str):
        self.separator = separator
        return self

    def setAWSCostsClass(self, awsCostsClass: AWSCosts):
        self.awsCosts = awsCostsClass
        return self

    def get(self) -> str:
        if self.awsCosts is None:
            raise Exception("You must set the AWS Costs class first using setAWSCostsClass() method.")

        rawData = self.awsCosts.getCosts()
        
        stringData = ""
        
        for cellData in rawData["ResultsByTime"]:
            stringData += cellData["TimePeriod"]["Start"] + " - " + cellData["TimePeriod"]["Start"] + self.separator
            stringData += str(cellData["Total"]["BlendedCost"]["Amount"]) + "\n"

        return stringData
