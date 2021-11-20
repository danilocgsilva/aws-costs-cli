from aws_costs_cli.FormatSingle import FormatSingle

class TerminalFormatter:

    def get(self, results: dict):
        amount = 0

        for result in results["ResultsByTime"]:
            formatSingle = FormatSingle(result)
            amount += formatSingle.getAmount()
            self.__showData(formatSingle)

        self.__finishes(str(amount), formatSingle.getAmountUnit())

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
