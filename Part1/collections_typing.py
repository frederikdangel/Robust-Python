from collections import defaultdict, UserDict, abc
from types import Union
from typing import Tuple, TypedDict, TypeVar, Generic, Iterator, _T_co

from intents import Cookbook

AuthorToCountMapping = dict[str, int]


def create_author_count_mapping(cookbooks: list[Cookbook]) -> AuthorToCountMapping:
    counter = defaultdict(lambda: 0)
    for book in cookbooks:
        counter[book.author] += 1
    return counter


Ingredient = tuple[str, int, str]  # (name, quantity, units)
Recipe = list[Union[int, Ingredient]]  # the list can be servings or ingredients


def adjust_recipe(recipe: Recipe, servings):
    return Tuple[recipe, servings]


class Range(TypedDict):
    min: float
    max: float


class NutritionInformation(TypedDict):
    value: int
    unit: str
    confidenceRange95Percent: Range
    standardDeviation: float


class RecipeNutritionInformation(TypedDict):
    recipes_used: int
    calories: NutritionInformation
    fat: NutritionInformation
    protein: NutritionInformation
    carbs: NutritionInformation


def get_nutrition_from_spoonacular(recipe_name: str):
    return RecipeNutritionInformation()


recipe_name = 'r_name'
nutrition_info: RecipeNutritionInformation = get_nutrition_from_spoonacular(recipe_name)

# variable Type
T = TypeVar('T')


def reverse(coll: list[T]) -> list[T]:
    return coll[::-1]


Node = TypeVar('Node')
Edge = TypeVar('Edge')


# directed graph
class Graph(Generic[Node, Edge]):
    def __init__(self):
        self.edges: dict[Node, list[Edge]] = defaultdict(list)

    def add_relation(self, node: Node, to: Edge):
        self.edges[node].append(to)

    def get_relation(self, node: Node) -> list[Edge]:
        return self.edges[node]


cookbooks: Graph[Cookbook, Cookbook] = Graph()
recipes: Graph[Recipe, Recipe] = Graph()
cookbook_recipes: Graph[Cookbook, Recipe] = Graph()
recipes.add_relation(Recipe('Pasta Bolognese'), Recipe('Pasta with Sausage and Basil'))
cookbook_recipes.add_relation(Cookbook('The Food Lab'), Recipe('Pasta Bolognese'))


def get_aliases(key):
    return key


class NutritionalInformation(UserDict):
    """
        Rather inherit from UserDict than from dict directly
    """
    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            pass
        for alias in get_aliases(key):
            try:
                return self.data[alias]
            except KeyError:
                pass
            raise KeyError(f"Could not find {key} or any of its aliases")


nutrition = NutritionalInformation()


def get_nutrition_information(param):
    return NutritionalInformation()


nutrition["arugula"] = get_nutrition_information("arugula")
# arugula is the same as rocket
print(nutrition.get("rocket", "No Ingredient Found"))


class AliasedIngredients(abc.Set):
    def __init__(self, ingr):
        self.ingredients = ingr

    def __contains__(self, value: str):
        return value in self.ingredients or any(alias in self.ingredients for alias in get_aliases(value))

    def __len__(self):
        return len(self.ingredients)

    def __iter__(self):
        return iter(self.ingredients)


ingredients = AliasedIngredients({'arugula', 'eggplant', 'pepper'})
for ingredient in ingredients:
    print(ingredient)

print(len(ingredients))
print('arugula' in ingredients)
print('rocket' in ingredients)
list(ingredients | AliasedIngredients({'garlic'}))