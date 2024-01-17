class RestaurantReviews:
    def __init__(self):
        self.reviews = {}

    def add_review(self, restaurant, review_text, rating):
        if rating < 1 or rating > 5:
            return "Invalid rating. It must be between 1 and 5."
        self.reviews[restaurant] = {'review_text': review_text, 'rating': rating}
        return f"Review added for {restaurant}."

    def get_review(self, restaurant):
        return self.reviews.get(restaurant, "Review not found.")

    def update_review(self, restaurant, new_review_text, new_rating):
        if restaurant not in self.reviews:
            return "Review not found."
        return self.add_review(restaurant, new_review_text, new_rating)
    
# Exercice : Faire le delete_review, et écrire les tests correspondants.
    # TDD possible
    def delete_review(self, restaurant):
        # Ecrire l'implementation
        if restaurant not in self.reviews:
            raise ValueError("Review not found to delete.")
        del self.reviews[restaurant]
        return f"Review deleted for {restaurant}."
    

class Menu:
    def __init__(self):
        self.menu = {}

    def add_menu_item(self, restaurant_name, item_name, description, price):
        if price <= 0:
            raise ValueError("Price must be positive.")
        if restaurant_name not in self.menu:
            self.menu[restaurant_name] = {}
        self.menu[restaurant_name][item_name] = {"description": description, "price": price}
        return "Menu item added for {}.".format(restaurant_name)