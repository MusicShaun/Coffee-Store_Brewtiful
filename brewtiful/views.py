from flask import Blueprint, render_template, url_for, request, session, flash, redirect, current_app
from pprint import pprint
from .forms import PayWithForm, SendToForm
from datetime import datetime
from .models import Product, Order
from . import db
from email_validator import validate_email
import locale
locale.setlocale(locale.LC_ALL, 'en_AU.UTF-8') 
import sys
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()


# GLOBAL VARIABLES 
user_cart = []
cart_total = 0
countries = ['Australia', 'Austria', 'Burkina Faso', 'Comoros', 'Dominican Republic', 'Eswatini', 'Guyana', 'Guinea-Bissau', 'Iceland', 'Jordan', 'Kyrgyzstan', 'Lebanon', 'Liberia', 'Malawi', 'Marshall Islands', 'Mauritania', 'Micronesia', 'Mozambique', 'Nauru', 'Nicaragua', 'Niger', 'Papua New Guinea', 'Saint Lucia', 'Sierra Leone', 'Solomon Islands', 'South Sudan', 'Tajikistan', 'Togo', 'United Kingdom', 'Venezuela', 'Vietnam']
codes = ['+61', '+43', '+226', '+269', '+1-809', '+268', '+592', '+245', '+354', '+962', '+996', '+961', '+231', '+265', '+692', '+222', '+691', '+258', '+674', '+505', '+227', '+675', '+1-758', '+232', '+677', '+211', '+992', '+228', '+44', '+58', '+84']


# create a blueprint
bp = Blueprint('views', __name__)



# route index  
@bp.route('/')
def index():
    products = Product.query.all()
    blends = ['Blend', 'Single Origin']
    tastes = ['Chocolate', 'Citrus', 'Floral']
    origins = ["Australia", "South America", "Central America", "Africa", "Asia"]

    if 'cart_count' not in session:
        session['cart_count'] = 0

    return render_template(
        'index.html', 
        products=products, 
        blends=blends, 
        tastes=tastes, 
        origins=origins
        )


# route /product/<int:product>
@bp.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product_details(product_id):

    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        print('product_id :::')
        print(request.form.get('product_id'))
        print('quantity :::')
        print(int(request.form.get('quantity')))

    return render_template('product-details.html', product=product)





# ADD TO CART 
@bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    print('ADD TO CART :::')
    try:
        quantity = int(request.form.get('quantity')) # not using these for the assignment. The default quantity is 1
        print('Quantity', quantity)

        # Check for existing order and create if needed
        order = Order.query.get(session.get('order_id'))
        if order is None:
            order = Order(status=False, total_cost=0, date=datetime.now())
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id

        
        # Check if product already exists in order
        if product_id is not None and order is not None:
            product = Product.query.get(product_id)
            print('ORDER DETAILS :::  \n\n\n', order.products)
            if product not in order.products:
              try:
                session['cart_count'] += 1
                order.products.append(product)
                db.session.commit()
                return redirect(url_for('views.cart'))
              except:
                return 'There was an issue adding the item to your basket'
        else:
            flash('Item already in your basket')
            message = str(message)
            flash(message)
    except:
        print(sys.exc_info()[0])
        return 'There was an issue adding the item to your basket'

    return redirect(url_for('views.product_details', product_id=product_id))






# # CART 
@bp.route('/cart', methods=['GET', 'POST'])
def cart():
    print('\n\nCART :::')
    quantity = 1
    order_id = session.get('order_id')
    cart_list = []
    cart_total = 0

    #  check order exists and display in cart
    if order_id is not None:
        order = Order.query.get_or_404(order_id)
        print('ORDER ::: ', order)

        #  get products from orders to be displayed in cart
        products = {}
        for product in order.products:
            products[product.id] = {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'image': product.image,
                'quantity': quantity
                }

            #  get total cost of cart
            cart_total = 0
            for product in products.values():
                cart_total += product['price'] * 1 # product['quantity']
            print('CART TOTAL :::  \n\n\n', cart_total)

            # update total cost of order
            order.total_cost = cart_total
            db.session.commit()
            cart_list = list(products.values())
            print(cart_list)

    return render_template('cart.html',
        cart=cart_list, 
        cart_total=locale.currency(cart_total, grouping=True))



# DELETE FROM CART 
@bp.route('/delete_from_cart/<int:product_id>', methods=['GET', 'POST'])
def delete_from_cart(product_id):
    print('\n\nDELETE FROM CART :::')

    # get order from database
    order_id = session.get('order_id')
    order = Order.query.get_or_404(order_id)

    pprint(order.products)

    for product in order.products:
      if product.id == product_id:
            print('PRODUCT WILL BE DELETED')
            session['cart_count'] -= 1
            order.products.remove(product)
            db.session.commit()
            break
      else:
            print(sys.exc_info()[0])
            print('Product failed to delete')

    return redirect(url_for('views.cart'))



# CHECKOUT
@bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    print('\n\nCHECKOUT :::')
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        send_to_form = SendToForm()
        pay_with_form = PayWithForm()
        # Disable all three fields for this assignment as I am not using them
        for field in [pay_with_form.card_number, pay_with_form.expiry, pay_with_form.cvv]:
            field.render_kw = {'disabled': True}

        if request.method == 'POST': # I split my checks here for error handling as it was easier as a beginner to understand
            if send_to_form.validate_on_submit():
                order.status = True
                order.firstname = send_to_form.firstname.data
                order.surname = send_to_form.surname.data
                order.street = send_to_form.street.data
                order.suburb = send_to_form.suburb.data
                order.postcode = send_to_form.postcode.data
                order.country = send_to_form.country.data
                order.email = send_to_form.email.data
                order.phone = send_to_form.phone.data
                order.total_cost = order.total_cost 
                order.date = datetime.now()  

                try:
                    db.session.commit()
                    flash('Thank you! Your order has been submitted successfully.')
                    return redirect(url_for('views.order_completed'))

                except Exception as e:
                    print(f'Error: {e}')
                    return 'There was an issue completing your order.'

        return render_template('checkout.html', 
            cart_total=locale.currency(order.total_cost, grouping=True), 
            user_cart=order.products,
            countries=countries, 
            pay_with_form=pay_with_form, 
            send_to_form=send_to_form,
            codes=codes)




@bp.route('/order-completed', methods=['GET', 'POST'])
def order_completed():
    print(session)
    print('\n\nORDER COMPLETED :::')

    products = []
    address = {}
    order_id = session.get('order_id')
    print('ORDER ID ::: ', order_id)
    if order_id is not None:
        order = Order.query.get_or_404(session['order_id'])
        if order is not None:
            for product in order.products:
                products.append(product)
            
            # get address details 
            address = {
                'firstname': order.firstname,
                'surname': order.surname,
                'street': order.street,
                'suburb': order.suburb,
                'postcode': order.postcode,
                'country': order.country,
                'email': order.email,
                'phone': order.phone
            }

    # in case the user refreshes the page      
    if order_id is None:
       return redirect(url_for('views.index'))
    
    # clear session
    session.clear()

    return render_template('order-completion.html', products=products, address=address, order_id=order_id)




# CLEAR SESSION
@bp.route('/clear_session')
def clear_session():
    session.clear()
    return 'Session cleared!'