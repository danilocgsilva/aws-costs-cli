from aws_costs_api.AWSCosts import AWSCosts
from aws_costs_cli.functions import getServiceTranslation

class CSV:

    def __init__(self):
        self.separator = ","
        self.awsCosts = None
        self.spread = None
        self.serviceTranslationBag = None

    def setSeparator(self, separator: str):
        self.separator = separator
        return self

    def setAWSCostsClass(self, awsCostsClass: AWSCosts):
        self.awsCosts = awsCostsClass
        return self
    
    def setSpread(self, serviceTranslationBag):
        self.spread = True
        self.serviceTranslationBag = serviceTranslationBag

    def get(self) -> str:
        if self.awsCosts is None:
            raise Exception("You must set the AWS Costs class first using setAWSCostsClass() method.")
        
        if self.spread:
            return self._getSpread()
        else:
            return self._getAll()
            
    def _getAll(self) -> str:

        rawData = self.awsCosts.getCosts()
        
        stringData = ""
        
        for cellData in rawData["ResultsByTime"]:
            stringData += cellData["TimePeriod"]["Start"] + " - " + cellData["TimePeriod"]["Start"] + self.separator
            stringData += str(cellData["Total"]["BlendedCost"]["Amount"]) + "\n"

        return stringData
    
    def _getSpread(self) -> str:
        
        string = ""
        
        for key_service in self.serviceTranslationBag:
            self.awsCosts.setUniqueService(getServiceTranslation(key_service))
            results_by_time = self.awsCosts.getCosts()["ResultsByTime"]
            for single_result in results_by_time:
                single_result = self.__shrink_data(single_result, key_service)
                string += single_result["period"] + self.separator + single_result["service"] + self.separator + str(single_result["amount"]) + "\n"
            
        return string
        
        
    def __shrink_data(self, raw: dict, key_service: str) -> dict:
        return {
            "service": key_service,
            "period": raw["TimePeriod"]["Start"],
            "amount": float(raw["Total"]["BlendedCost"]["Amount"]),
            "unit": raw["Total"]["BlendedCost"]["Unit"]
        }
