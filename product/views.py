from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from product.models import Product


def home(request):
    products_list = Product.objects.all().order_by('title')
    paginator = Paginator(products_list, 1)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    print(page_number)
    return render(request, 'product/home.html', {'products': products})


@login_required(login_url="/account/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and \
                request.FILES['icon']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].lower().startswith('http://') or request.POST['url'].lower().startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.now()
            product.votes_total = 1
            product.hunter = request.user
            product.save()
            return redirect('/product/' + str(product.id))

        else:
            return render(request, 'product/create.html', {'error': 'All fields are required !'})
    else:
        return render(request, 'product/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/detail.html', {'product': product})


@login_required(login_url="/account/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/product/' + str(product.id))
