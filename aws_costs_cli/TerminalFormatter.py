from aws_costs_cli.FormatSingle import FormatSingle

class TerminalFormatter:

    def __init__(self):
        self.all_data_services = None

    def get(self, results: dict):
        amount = 0

        for result in results["ResultsByTime"]:
            formatSingle = FormatSingle(result)
            amount += formatSingle.getAmount()
            self.__showData(formatSingle)

        self.__finishes(str(amount), formatSingle.getAmountUnit())

    def set_all_data_services(self, all_data_services: dict):
        self.all_data_services = all_data_services
        return self

    def print_spread(self):
        for time in self.all_data_services:
            print(time + ":")
            for service in self.all_data_services[time]:
                print("    " + service + ": " + str(self.all_data_services[time][service]))

    def __showData(self, format: FormatSingle):
        print(
            "Month and day: " + format.getMonthDay()
        )
        print(
            str(format.getAmount()) + " " + format.getAmountUnit()
        )
        print("----")



    def __finishes(self, amount, unit):
        print("Total from last month: " + amount + " " + unit)
        print("---//---")
        print("Above, the last month day by day cost from AWS account.")
