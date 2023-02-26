from django.shortcuts import render, redirect
from django.contrib.auth.hashers import Argon2PasswordHasher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import Customer
from . forms import  FormCustomer, FormUser
from cart.models import Order, OrderItem
from cart.cart import Cart
from store.models import Product


def login_signup(request):
    result_signup = ''
    form_user = FormUser()
    form_customer = FormCustomer()
    if request.POST.get('btnSignup'):
        form_user = FormUser(request.POST)
        form_customer = FormCustomer(request.POST)
        if form_user.is_valid() and form_customer.is_valid():
            if form_user.cleaned_data['password'] == form_user.cleaned_data['confirm_password']:
                #User
                user = form_user.save()
                user.set_password(user.password)
                user.save()

                #Customer
                customer = form_customer.save(commit=False)
                customer.user = user
                customer.dien_thoai = form_customer.cleaned_data['dien_thoai']
                customer.dia_chi = form_customer.cleaned_data['dia_chi']
                customer.save()

                result_signup = '''
                    <div class="alert alert-success" role="alert">
                        Bạn đã đăng ký thành công, vui lòng đăng nhập để tiếp tục!!!
                    </div>
                '''
        else:
            result_signup = '''
                <div class="alert alert-danger" role="alert">
                    Đăng ký không thành công, vui lòng kiểm tra dữ liệu nhập!
                </div>
            '''

    # Đăng nhập
    if request.POST.get('btnLogin'):
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        # if user is not None:
        if user:
            login(request, user)
            return redirect('store:index')


    return render(request, 'users/login.html', {
        'form_user': form_user,
        'form_customer': form_customer,
        'result_signup': result_signup
    })


def user_logout(request):
    logout(request)
    return redirect('user:login')

def myaccount(request):
    if not request.user:
        return redirect('user:login')

    result = ''

    if request.POST.get('btnUpdateUser'):
        ho = request.POST.get('last_name')
        ten = request.POST.get('first_name')
        dt = request.POST.get('mobile')
        dc = request.POST.get('address')

        s_customer = request.user
        customer = Customer.objects.get(user__id=s_customer.id)
        customer.user.last_name = ho
        customer.user.first_name = ten
        customer.dien_thoai = dt
        customer.dia_chi = dc
        customer.save()

        s_customer.last_name = ho
        s_customer.first_name = ten

        result = '''
            <div class="col-md-12">
                <div class="alert alert-success" role="alert">
                    Bạn đã cập nhật thành công!!!
                </div>
            </div>
            '''

    cart = Cart(request)
    orders = Order.objects.filter(username=request.user.username)
    dict_orders = {}
    for order in orders:
        items = (OrderItem.objects.filter(order=order.id).values())
        for item in items:
            product = Product.objects.get(id=item['product_id'])
            item['product_name'] = product.name
            item['product_image'] = product.image
            item['total_price'] = order.total
        else:
            dict_order_items = {
                order.id: items
            }

            dict_orders.update(dict_order_items)
    # print(dict_orders)

    return render(request, 'users/my-account.html',{
        'result': result,
        'cart': cart,
        'orders': orders,
        'items': items,
        'dict_orders': dict_orders
    })
        