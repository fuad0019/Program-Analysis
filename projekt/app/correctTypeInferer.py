# take as input type
# return if Integer --> int
# return if string --> String


def inferTypeAndValue(type, value):
    if type == "string":
        return "String", f'"{value}"'
    if type == "integer":
        return "int", int(value)


def inferValue(type, value):
    if type == "string":
        return f'"{value}"'
    if type == "integer":
        return int(value)
