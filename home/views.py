from home.models import Category, Newsletter, Product
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def send_letter_home(request):
#     if request.method == 'POST':
#         request.POST.get('sender_name')
#         subject = 'Welcome to DataFlair'
#         message = 'Hope you are enjoying your Django Tutorials'
#         recepient = str(sub['Email'].value())
#         send_mail(subject, message, EMAIL_HOST_USER, ['nurmatov.rahimjon@mail.ru'], fail_silently = False)
#         return render(request, 'subscribe/success.html', {'recepient': recepient})
#     return render(request, 'subscribe/index.html')

# Create your views here.
def homePage(request):
    news = Newsletter.objects.all()[:3]
    products = Product.objects.all()[:12]
    special_product_list = []
    for product in products:
        if product.special_product:
            special_product_list.insert(0, product)
    context = {'products': products, 'special_products': special_product_list[:4], 'news': news }
    return render(request, 'home/index.html', context)

def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    best_products_list = []
    for item in products:
        if item.best_seller:
            best_products_list.insert(0, item)
    context = {'categories': categories, 'page': page, 'products': products, 'best_seller': best_products_list[:4]}
    return render(request, 'home/products.html', context)

def contact(request):
    return render(request, 'home/contactus.html')

def about(request):
    return render(request, 'home/aboutus.html')

def newsletter(request):
    news = Newsletter.objects.all()
    context = {'news': news[1:], 'main_news': news[0], 'latest_news': news[0:3]}
    return render(request, 'home/newsletter.html', context)

def product_detail(request, product_id):
    categories = Category.objects.all()
    products = Product.objects.all()
    product = Product.objects.get(pk=product_id)
    print(product.name)
    category = product.category
    similar_products = []
    for item in products:
        if product.category == item.category and product.id != item.id:
            similar_products.append(item)
    images = [product.image_link1, product.image_link2, product.image_link3, product.image_link4]
    best_products_list = []
    for item in products:
        if item.best_seller:
            best_products_list.insert(0, item)
    context = {'categories': categories, 'product': product, 'images': images, 'similar_products': similar_products[:3], 'category': category, 'best_seller': best_products_list[:4]}
    return render(request, 'home/product-detail.html', context)

def news_info(request, news_id):
    news = Newsletter.objects.all()
    n_info = Newsletter.objects.get(pk=news_id)
    context = {'n_info': n_info, 'latest_news': news[:3]}
    return render(request, 'home/news-info.html', context)

def category(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    c_products = Product.objects.filter(category = category)
    c_check = bool(c_products)
    paginator = Paginator(c_products, 2)
    page = request.GET.get('page')
    try:
        c_products = paginator.page(page)
    except PageNotAnInteger:
        c_products = paginator.page(1)
    except EmptyPage:
        c_products = paginator.page(paginator.num_pages)
    best_products_list = []
    for item in c_products:
        if item.best_seller:
            best_products_list.insert(0, item)
    context = {'categories': categories, 'page': page, 'c_products': c_products, 'category': category, 'c_check': c_check, 'best_seller': best_products_list[:4]}
    return render(request, 'home/category.html', context)