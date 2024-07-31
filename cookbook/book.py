from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        
        # Validate name
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.name = name

        # Validate last_update
        if not isinstance(last_update, datetime):
            raise TypeError("last_update must be a datetime")
        self.last_update = last_update

        # Validate creation_date
        if not isinstance(creation_date, datetime):
            raise TypeError("creation_date must be a datetime")
        self.creation_date = creation_date

        # Validate recipes_list
        if not isinstance(recipes_list, dict):
            raise TypeError("recipes_list must be a dict")
        self.recipes_list = recipes_list


    def get_recipe_by_name(self, name):
        recipe = self.recipes_list.get(name)
        if recipe is None:
            print(f"Recipe with name '{name}' not found.")
            return None

        if not isinstance(recipe, Recipe):
            print("Error: Found item is not a valid Recipe instance.")
            return None

        # Print the recipe details using __str__
        print(recipe)
        
        return recipe
    

    def get_recipes_by_type(self, recipe_type):
        # Validate recipe_type
        valid_types = {"starter", "lunch", "dessert"}
        if not isinstance(recipe_type, str) or recipe_type not in valid_types:
            raise ValueError(f"Invalid recipe type: '{recipe_type}'. Must be one of {valid_types}.")
    
        # Initialize an empty list for filtered recipes
        recipes = []
    
        # Filter recipes by type
        for recipe in self.recipes_list.values():
            if isinstance(recipe, Recipe) and recipe.recipe_style == recipe_type:
                recipes.append(recipe)
    
        return recipes


    def add_recipe(self, recipe):
        # Validate recipe
        if not isinstance(recipe, Recipe):
            raise TypeError("recipe must be an instance of Recipe")
        
        # Handle edge case
        if recipe.name in self.recipes_list:
            print(f"Recipe with name '{recipe.name}' already exists.")
            return
        
        # Add recipe to the book
        self.recipes_list[recipe.name] = recipe
        
        # Update last_update to the current time
        self.last_update = datetime.now()
        
        print(f"Recipe '{recipe.name}' added successfully.")