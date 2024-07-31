class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_style):
        
        # Validate name
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.name = name

        # Validate cooking_lvl
        if not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError("cooking_lvl must be an integer between 1 and 5")
        self.cooking_lvl = cooking_lvl

        # Validate cooking_time
        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise ValueError("cooking_time must be a non-negative integer")
        self.cooking_time = cooking_time

        # Validate ingredients
        if not isinstance(ingredients, list) or not all(isinstance(ingredient, str) for ingredient in ingredients):
            raise TypeError("ingredients must be a list of strings")
        self.ingredients = ingredients

        # Validate description
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        self.description = description

        # Validate recipe_style
        valid_styles = {"starter", "lunch", "dessert"}
        if not isinstance(recipe_style, str) or recipe_style not in valid_styles:
            raise TypeError("recipe_style must be a string")
        self.recipe_style = recipe_style

    # __str__ method formats the attributes into a readable format
    def __str__(self):
        return (f"Recipe Name: {self.name}\n"
                f"Cooking Level: {self.cooking_lvl}\n"
                f"Cooking Time: {self.cooking_time} minutes\n"
                f"Ingredients: {', '.join(self.ingredients)}\n"
                f"Description: {self.description}\n"
                f"Recipe Style: {self.recipe_style}")