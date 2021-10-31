from fractions import Fraction


class Recipe:
    def __init__(self, recipe, ingredients):
        self.ingredients = ingredients
        self.recipe = recipe


def adjust_recipe(recipe, servings):
    """

    Args:
        recipe (): a 'Recipe' indicating what needs to be adjusted.
        servings (): the number of servings

    Returns: a recipe with serving size and ingredients adjusted for the new servings

    """
    # create a copy of the ingredients
    new_ingredients = list(recipe.get_ingredients())
    recipe.clear_ingredients()

    for ingredient in new_ingredients:
        ingredient.adjust_proportion(Fraction(servings, recipe.servings))
    return Recipe(servings, new_ingredients)