from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        # Retrieve the form data
        product_name = request.POST.get('product_name')
        quantity = int(request.POST.get('quantity'))
        price = float(request.POST.get('price'))

        # Perform calculations
        subtotal = quantity * price
        vat = subtotal * 0.12  # Calculate 12% VAT
        total_amount = subtotal + vat  # Total amount including VAT

        # Render the receipt template and pass data to it
        return render(request, 'pos/receipt.html', {
            'product_name': product_name,
            'quantity': quantity,
            'price': price,
            'subtotal': subtotal,
            'vat': vat,
            'total_amount': total_amount
        })

    return render(request, 'pos/pos.html')

def pos_view(request):
    if request.method == 'POST':
        if 'add_product' in request.POST:
            # Add product logic here
            pass
        elif 'remove_product' in request.POST:
            # Remove product logic here
            pass

    products = Product.objects.all()
    return render(request, 'pos.html', {'products': products})

def receipt_view(request):
    # Example data for receipt; replace with actual logic
    products = request.session.get('transaction_products', [])
    total_amount = sum(product['price'] * product['quantity'] for product in products)

    available_products = Product.objects.all()  # Get available products for display

    return render(request, 'receipt.html', {
        'products': products,
        'available_products': available_products,
        'total_amount': total_amount,
    })
