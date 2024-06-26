from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product,ProductSerializer
from store.models.customer import Customer,CustomSerializer
from store.models.orders import Order,OrderSerializers
from store.models.category import Category
from django.views import View
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)



class ProductAPI(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
    

class CustomerAPI(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomSerializer
    



class OrderAPI(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers