def temperature_converter(temperature, unit, threshold):
    if unit.lower() == 'f':
        new_temperature=(temperature - 32) * 5/9
        if new_temperature < threshold:
            print("Cold advisory")
            return "Cold advisory"
        print("Heat alert")
        return "Heat alert"
    elif unit.lower() == 'c':
        new_temperature=(temperature * 9/5) + 32
        if new_temperature < threshold:
            print("Cold advisory")
            return "Cold advisory"
        print("Heat alert")
        return "Heat alert"
    else:
        if temperature < threshold:
            print("Cold advisory")
            return "Cold advisory"
        print("Heat alert")
        return "Heat alert"


temperature_converter(-10, "c", 200)
