from aws_costs_api.AWSCosts import AWSCosts
from aws_costs_cli.functions import getServiceTranslation, serviceTranslationBag

class SpreadCalculator:

    def __init__(self):
        self.cleint = None
        self.format = None

    def set_client(self, client: AWSCosts):
        self.client = client
        self.by_date_service_data = {}

    def set_translation_bag(self, translation_bag):
        self.translation_bag = translation_bag

    def get_data(self, connectionString = None) -> dict:
        self.__hidrate_raw_data(connectionString)
        self.__add_summarization_data()
        return self.by_date_service_data
    
    def set_csv_format(self):
        self.format = "csv"
        
    def __hidrate_raw_data(self, connectionString = None):
        for key_service in self.translation_bag:
            self.client.setUniqueService(getServiceTranslation(key_service))
            results_by_time = self.client.getCosts(connectionString)["ResultsByTime"]

            for single_result in results_by_time:
                single_result = self.__shrink_data(single_result, key_service)

                if not single_result["period"] in self.by_date_service_data:
                    self.by_date_service_data[single_result["period"]] = {}

                self.by_date_service_data[single_result["period"]][key_service] = single_result["amount"]

    def __add_summarization_data(self):
        for date in self.by_date_service_data:
            date_sum = 0
            for service_key in self.by_date_service_data[date]:
                date_sum += self.by_date_service_data[date][service_key]
            self.by_date_service_data[date]["TOTAL"] = date_sum

    def __shrink_data(self, raw: dict, key_service: str) -> dict:

        return {
            "service": key_service,
            "period": raw["TimePeriod"]["Start"],
            "amount": float(raw["Total"]["BlendedCost"]["Amount"]),
            "unit": raw["Total"]["BlendedCost"]["Unit"]
        }
