from datetime import datetime

from django.db.models import Sum
from recipes.models import IngredientInRecipe


def set_shopping_list(self, request, user):
    ingredients = IngredientInRecipe.objects.filter(
        recipe__shopping_cart__user=user
    ).values(
        'ingredient__name',
        'ingredient__measurement_unit'
    ).annotate(amount=Sum('amount'))
    today = datetime.today()
    shopping_list = (
        f'Список покупок для: {user}\n\n'
        f'Дата: {today():%Y-%m-%d}\n\n'
    )
    shopping_list += '\n'.join([
        f'- {ingredient["ingredient__name"]} '
        f'({ingredient["ingredient__measurement_unit"]})'
        f' - {ingredient["amount"]}'
        for ingredient in ingredients
    ])
    shopping_list += f'\n\nFoodgram ({today():%Y})'
    return shopping_list
