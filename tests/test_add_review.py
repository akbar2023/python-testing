import pytest

from restaurant_reviews import RestaurantReviews  # n'oubliez pas le __init__.py dans le dossier test afin d'importer la Classe

def test_add_valid_review():
  rr = RestaurantReviews