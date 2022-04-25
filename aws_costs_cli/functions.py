from aws_costs_cli.OutOfOptionException import OutOfOptionException

def spread(serviceTranslationBag: dict, awscosts) -> dict:

    by_date_service_data = {}
    for key_service in serviceTranslationBag:
        awscosts.setUniqueService(getServiceTranslation(key_service, serviceTranslationBag))
        results_by_time = awscosts.getCosts()["ResultsByTime"]
        for single_result in results_by_time:
            single_result = __shrink_data(single_result, key_service)

            if single_result["period"] in by_date_service_data:
                by_date_service_data[single_result["period"]][key_service] = single_result["amount"]
                by_date_service_data[single_result["period"]]["all"] += single_result["amount"]
            else:
                by_date_service_data[single_result["period"]] = {"all": 0}
    return by_date_service_data

def getServiceTranslation(shortServiceName: str, serviceTranslationBag: dict) -> str:

    if shortServiceName in serviceTranslationBag:
        return serviceTranslationBag[shortServiceName]
    else:
        message = "Option not known. Acceptable values are:\n"
        for key in serviceTranslationBag:
            message += key + "\n"
        raise OutOfOptionException(message)

def __shrink_data(raw: dict, key_service: str) -> dict:

    return {
        "service": key_service,
        "period": raw["TimePeriod"]["Start"],
        "amount": float(raw["Total"]["BlendedCost"]["Amount"]),
        "unit": raw["Total"]["BlendedCost"]["Unit"]
    }

