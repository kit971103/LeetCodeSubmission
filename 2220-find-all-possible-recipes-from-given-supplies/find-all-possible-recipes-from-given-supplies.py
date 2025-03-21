class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:

        def missing_ingredients(
            ingredient_list: List[str], supplies_set: Set[str]
        ) -> List[str]:
            return [
                ingredient
                for ingredient in ingredient_list
                if ingredient not in supplies_set
            ]

        doable = []
        supplies_set = set(supplies)

        r_recipes = []
        r_ingredients = []
        updated = False

        while True:

            for recipe, ingredient_list in zip(recipes, ingredients):
                missing = missing_ingredients(ingredient_list, supplies_set)
                if missing == []:
                    doable.append(recipe)
                    supplies_set.add(recipe)
                    updated = True
                else:
                    r_recipes.append(recipe)
                    r_ingredients.append(missing)
            print(doable, r_recipes, r_ingredients)
            if not updated:
                print("returning")
                return doable

            updated = False
            recipes = r_recipes
            ingredients = r_ingredients
            r_recipes = []
            r_ingredients = []

        