from flask import Blueprint 
from . import db
from .models import Product
from os.path import join

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dbseed/')
def dbseed():
    
    print('Adding products...')
    # Products
    product1 = Product(
        name='Berkel Coffee',
        description='Embrace the rich aroma and vibrant flavor of Berkel Coffee, a meticulously crafted blend of single-origin coffee beans. Sourced from the sun-kissed hills of Brazil, these beans are handpicked at the peak of ripeness, ensuring an exceptional cup every time. Expertly roasted and packed locally, Berkel Coffee delivers a smooth, balanced taste with notes of chocolate, nuts, and caramel.',
        image='img/berkel.jpeg',
        price=18.99,
        size='250g',
        origin="South America",
        is_blend=True,
        aroma='A rich, chocolatey fragrance and subtle nutty undertones.',
        notes='chocolate'
    )

    product2 = Product(
        name='Onyx',
        description="Unleash the captivating essence of Colombian coffee with Onyx, a harmonious blend of premium Arabica beans. Cultivated in the high altitudes of Colombia's lush coffee regions, these beans are renowned for their exceptional quality and complex flavor profile. Onyx boasts a rich aroma, a bright acidity, and a lingering sweetness, offering a true taste of Colombian coffee excellence.",
        image='img/onyx.jpeg',
        price=15,
        size='1kg',
        origin="South America",
        is_blend=False,
        aroma='Characterized by a bright, citrusy fragrance with subtle floral notes.',
        notes='floral'
    )

    product3 = Product(
        name='Sacred Blend',
        description="Embark on a sensory journey with Sacred Blend, an Ethiopian coffee experience that awakens the senses. Harvested from the ancient coffee forests of Ethiopia, these beans carry a rich heritage and a distinctive flavor profile. Sacred Blend delivers a complex interplay of floral notes, citrusy acidity, and a hint of berries, culminating in a captivatingly aromatic cup.",
        image='img/sacred-blend.jpeg',
        price=23,
        size='500g',
        origin='Africa',
        is_blend=True,
        aroma='Floral hints, bright citrus notes, and a touch of berry sweetness.',
        notes='floral'
    )

    product4 = Product(
        name='Nossa Family',
        description="Discover the warmth and aroma of Nossa Family, a Guatemalan coffee blend that embodies the spirit of community. Grown in the fertile volcanic highlands of Guatemala, these beans are cultivated by generations of coffee-growing families, each passing down their knowledge and passion. Nossa Family showcases a smooth, balanced flavor with notes of chocolate, nuts, and a hint of molasses.",
        image='img/nossa.webp',
        price=9,
        size='250g',
        origin='South America',
        is_blend=True,
        aroma='A rich, chocolatey fragrance complemented by nutty and molasses undertones.',
        notes='chocolate'
    )

    product5 = Product(
        name='Caffiet',
        description="Experience the invigorating energy of Caffiet, a Honduran coffee blend that fuels your day. Cultivated in the vibrant coffee regions of Honduras, these beans are known for their robust flavor and invigorating aroma. Caffiet delivers a bold, full-bodied taste with notes of dark chocolate, roasted nuts, and a lingering sweetness, providing a caffeine boost that awakens your senses.",
        image='img/mockup-subhead.jpeg',
        price=15,
        size='1kg',
        origin='Asia',
        is_blend=False,
        aroma='Dark chocolate notes, roasted nut undertones, and a lingering sweet essence.',
        notes='chocolate'
    )

    product6 = Product(
        name='MockUP',
        description="Immerse yourself in the vibrant flavors of MockUP, a Kenyan coffee blend that ignites the taste buds. Grown in the highlands of Kenya, where coffee is deeply rooted in the culture, these beans are handpicked and processed with meticulous care. MockUP presents a complex and aromatic cup with notes of blackberries, citrus, and a hint of floral essence.",
        image='img/lorum-ipsum.avif',
        price=17,
        size='500g',
        origin='South America',
        is_blend=False,
        aroma='Blackberry notes, citrusy hints, and a touch of floral essence.',
        notes='fruity'
    )

    product7 = Product(
        name='Dragon House',
        description="Embrace the bold and adventurous flavors of Dragon House, a Mexican coffee blend that sparks the imagination. Cultivated in the diverse coffee-growing regions of Mexico, these beans are known for their unique flavor profiles and rich cultural heritage. Dragon House delivers a smoky, earthy taste with notes of dark chocolate, spice, and a hint of cherry.",
        image='img/dragon.webp',
        price=24,
        size='250g',
        origin='Central America',
        is_blend=False,
        aroma='Smoky earthy tones, rich dark chocolate, and a hint of cherry sweetness.',
        notes='fruity'
    )

    product8 = Product(
        name='Campos',
        description="Discover the elegance and sophistication of Campos, a Peruvian coffee blend that captivates the senses. Grown in the high altitudes of Peru, where coffee cultivation is a way of life, these beans are carefully handpicked and processed to preserve their exceptional quality. Campos showcases a smooth, balanced flavor with notes of chocolate, nuts, and a hint of citrus.",
        image='img/campos.avif',
        price=21.50,
        size='1kg',
        origin='Africa',
        is_blend=True,
        aroma='Smooth chocolate, nutty undertones, and a touch of citrus freshness.',
        notes='chocolate'
    )

    product9 = Product(
        name='Byron Bay',
        description="Embark on a journey to the heart of Africa with Byron Bay, a Rwandan coffee blend that embodies the spirit of adventure. Cultivated in the lush coffee-growing regions of Rwanda, these beans are known for their complex flavor profiles and vibrant aromas. Byron Bay delivers a bright, acidic cup with notes of berries, citrus, and a hint of floral essence.",
        image='img/byron-bay.jpg',
        price=17.10,
        size='500g',
        origin='Africa',
        is_blend=True,
        aroma='Vibrant berries, citrusy notes, and a touch of floral essence.',
        notes='floral'
    )

    product10 = Product(
        name='Bean There',
        description="Experience the rich and complex flavors of Bean There, a Tanzanian coffee blend that tantalizes the palate. Grown in the diverse coffee-growing regions of Tanzania, these beans are handpicked and processed with traditional methods, preserving their unique characteristics. Bean There showcases a bold, full-bodied taste with notes of dark chocolate, spice, and a hint of fruit.",
        image='img/FLATLAY-BAG.webp',
        price=19.99,
        size='250g',
        origin='Australia',
        is_blend=True,
        aroma='Bold dark chocolate, spicy undertones, and a hint of fruity sweetness.',
        notes='floral'
    )

    product11 = Product(
        name='CupAJoe',
        description="Indulge in the comforting and familiar aroma of CupAJoe, a Ugandan coffee blend that evokes a sense of nostalgia. Cultivated in the fertile highlands of Uganda, these beans are known for their smooth, balanced flavor and approachable taste profile. CupAJoe delivers a comforting cup with notes of chocolate, nuts, and a hint of caramel.",
        image='img/ventura.png',
        price=28.10,
        size='1kg',
        origin='Australia',
        is_blend=False,
        aroma='Comforting chocolate, nutty undertones, and a hint of caramel sweetness.',
        notes='chocolate'
    )

    product12 = Product(
        name='So Wrong It\'s Right',
        description="Embrace the unexpected with So Wrong It's Right, a Vietnamese coffee blend that challenges expectations. Grown in the vibrant coffee regions of Vietnam, these beans are known for their unique flavor profile and bold aroma. So Wrong It's Right delivers a smoky, earthy taste with notes of dark chocolate, spice, and a hint of robusta intensity.",
        image='img/yellow.jpeg',
        price=12.50,
        size='500g',
        origin='Asia',
        is_blend=True,
        aroma='Smoky earthy tones, rich dark chocolate, spicy undertones, and a hint of robusta intensity.',
        notes='chocolate'
    )

    # Commit products to the database. I found it cleaner to use an loop
    for product in [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12]:
      db.session.add(product)
    db.session.commit()

    # Commit changes to the database
    try:
        db.session.commit()
        print('Data loaded successfully!')
    except Exception as e:
        db.session.rollback()
        print(f'There was an issue adding products to the database: {e}')

    return 'DATA LOADED'
