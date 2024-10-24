from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Product  # Ensure you import Product model correctly

# Define a global cart to store added products
cart = []

def home(request):
    global cart

    # Initialize variables
    total_items = 0
    subtotal = 0
    total_amount = 0
    
    # Add product to cart
    if request.method == 'POST':
        if 'addProduct' in request.POST:
            product_name = request.POST['product_name']
            quantity = int(request.POST['quantity'])
            price = float(request.POST['price'])
            total_amount_for_product = quantity * price

            # Create a product dictionary and add to cart
            product = {
                'name': product_name,
                'quantity': quantity,
                'price': price,
                'total_amount': total_amount_for_product
            }
            cart.append(product)

        # Remove product from cart
        elif 'removeProduct' in request.POST:
            product_name = request.POST['product_name']
            cart = [product for product in cart if product['name'] != product_name]
        
        elif 'clearCart' in request.POST:
            # Clear the cart
            cart.clear() # Clear the cart
            return render(request, 'pos/pos.html', {'cart': []}) 

        # Process the sale (checkout)
        elif 'processSale' in request.POST:
            subtotal = sum(product['total_amount'] for product in cart)
            vat = subtotal * 0.12  # Calculate 12% VAT
            total_amount = subtotal + vat  # Total amount including VAT

            # Clear the cart after processing the sale
            products_for_receipt = cart.copy()
            cart.clear()  # Clear the cart for the next transaction

            # Render the receipt template and pass data to it
            return render(request, 'pos/receipt.html', {
                'products': products_for_receipt,
                'subtotal': subtotal,
                'vat': vat,
                'total_amount': total_amount,
            })

    # Calculate total items, subtotal, and total amount
    for product in cart:
        total_items += product['quantity']
        subtotal += product['total_amount']
    
    total_amount = subtotal  # You can add tax calculation here if needed

    context = {
        'products': cart,
        'total_items': total_items,
        'subtotal': subtotal,
        'total_amount': total_amount,
    }

    return render(request, 'pos/pos.html', context)





