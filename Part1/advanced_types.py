from typing import Union, Literal, NewType
from dataclasses import dataclass


class HotDog:
    def is_plated(self):
        pass

    def put_on_plate(self):
        pass

    def add_napkins(self):
        pass


class Pretzel:
    pass


def dispense_snack(user_input: str) -> Union[HotDog, Pretzel]:
    if user_input == "Hot Dog":
        return dispense_hot_dog()
    elif user_input == "Pretzel":
        return dispense_pretzel()
    raise RuntimeError("Should never reach this code, as an invalid input has been entered")


def dispense_hot_dog():
    return HotDog()


def dispense_pretzel():
    return Pretzel()


@dataclass
class Snack:
    name: str
    condiments: set[str]


@dataclass
class Error:
    error_code: int
    disposed_of: bool


@dataclass
class LError:
    error_code: Literal[1, 2, 3, 4, 5]
    disposed_of: bool


@dataclass
class LSnack:
    name: Literal[Literal["Pretzel", "Hot Dog", "Veggie Burger"]]
    condiments: set[Literal["Mustard", "Ketchup"]]


# my_snack = Snack("Hotdog", {"Mustard", "Ketchup"}, 5, False)

snack: Union[Snack, Error] = Snack("Hotdog", {"Mustard", "Ketchup"})
my_snack = Error(5, True)

LError(0, False)
LSnack("Invalid", set())
LSnack("Pretzel", {"Mustard", "Relish"})


# show how to use NewType


ReadyToServeHotDog = NewType("ReadyToServeHotDog", HotDog)


def prepare_for_serving(hot_dog: HotDog) -> ReadyToServeHotDog:
    assert not hot_dog.is_plated(), "Hot dog should not already be plated"
    hot_dog.put_on_plate()
    hot_dog.add_napkins()
    return ReadyToServeHotDog(hot_dog)