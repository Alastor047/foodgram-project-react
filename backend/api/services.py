from datetime import today


def set_shopping_list(user, ingredients):
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
