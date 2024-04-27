from django.contrib import admin
from django.urls import path,include
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.home import ProductAPI,CustomerAPI,OrderAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductAPI)
router.register(r'customer', CustomerAPI)
router.register(r'order', OrderAPI)


urlpatterns = [
    path('api/',include(router.urls)),
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    
    
    
    # ****************************** API *****************************************#
    # Product API
    # path('api/product',ProductAPI.as_view({'get': 'list','post':'create'}),name = 'product_api'),
    
    # Customer API 
    # path('api/customer',CustomerAPI.as_view({'get':'list'}),name = 'customer_api'),
    
    
    # Order API
    # path('api/order',OrderAPI.as_view({'get':'list'}),name = 'Order_api')
]
