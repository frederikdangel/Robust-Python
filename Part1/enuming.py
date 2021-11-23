from enum import auto, Enum, unique


# want to preserve uniqueness in your Enum
@unique
class MotherSauce(Enum):
    def _generate_next_value_(name, start, count, last_values):
        """
            to control what values are set when calling auto()
        Args:
            start (int):
            count (int):
            last_values ():

        Returns:
            the capitalized name
        """
        return name.capitalize()

    BÉCHAMEL = "Béchamel"
    VELOUTÉ = "Velouté"
    ESPAGNOLE = "Espagnole"
    TOMATO = "Tomato"
    HOLLANDAISE = "Hollandaise"
    SENF = auto()
    BARBECUE = auto()


# access:
print(MotherSauce.HOLLANDAISE)
print(list(MotherSauce))