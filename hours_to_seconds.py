input_hours = int(input("Enter Hours Here: "))


def convert(input_hours):
    minutes = input_hours * 60
    seconds = minutes * 60

    return seconds


print(str(input_hours) + " hours are " + str(convert(input_hours)) + " seconds.")