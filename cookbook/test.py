from datetime import datetime
from recipe import Recipe
from book import Book  # Ensure you have a file named `book.py` with the Book class

def test_book_and_recipe():
    # Create some Recipe instances
    recipe1 = Recipe(
        name="Spaghetti Carbonara",
        cooking_lvl=2,
        cooking_time=20,
        ingredients=["spaghetti", "egg", "parmesan", "bacon"],
        description="A classic Italian pasta dish.",
        recipe_style="lunch"
    )

    recipe2 = Recipe(
        name="Caesar Salad",
        cooking_lvl=1,
        cooking_time=10,
        ingredients=["romaine lettuce", "croutons", "parmesan", "Caesar dressing"],
        description="", # Accepts empty description
        recipe_style="starter"
    )

    # Create a Book instance with an empty recipes list
    book = Book(
        name="My Recipe Book",
        last_update=datetime.now(),
        creation_date=datetime.now(),
        recipes_list={}
    )

    # Add recipes to the book
    book.add_recipe(recipe1)
    book.add_recipe(recipe2)

    # Test get_recipe_by_name
    print("\nTesting get_recipe_by_name:")
    recipe = book.get_recipe_by_name("Spaghetti Carbonara")
    if recipe:
        print(recipe) 

    # Test get_recipes_by_type
    print("\nTesting get_recipes_by_type:")
    lunch_recipes = book.get_recipes_by_type("lunch")
    for rec in lunch_recipes:
        print(rec)  

    # Test adding a recipe that already exists
    print("\nTesting adding an existing recipe:")
    book.add_recipe(recipe1)  # Print a message indicating the recipe already exists

    # Test with an invalid recipe type
    try:
        print("\nTesting get_recipes_by_type with invalid type:")
        book.get_recipes_by_type("dessert")  # Valid type for testing
        book.get_recipes_by_type("invalid")  # Invalid type for testing
    except ValueError as e:
        print(e)  # Should print the ValueError message

if __name__ == "__main__":
    test_book_and_recipe()