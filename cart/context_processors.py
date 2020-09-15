from .cart import Cart


def cart(request):
    """
    return dictionary that gets added to the request context.
    Available globally to all templates
    """
    return {'cart': Cart(request)}


