from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponseForbidden
from .models import Address
from .forms import AddressForm
from django.contrib.auth.decorators import login_required

# This is address view.
# To add addresses view.
@login_required
def address_view(request):
    form = AddressForm
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = request.user
            add.save()
            return HttpResponseRedirect(request.get_full_path())
    return render(request,'address.html',{'form':form,'addresses':request.user.address_set.all()})

# To delete addresses view.
@login_required
def address_delete(request,pk):
    add = get_object_or_404(Address,pk=pk)
    if add.user == request.user:
        add.delete()
        return HttpResponseRedirect('/addresses/')
    return HttpResponseForbidden("NOT ALLOWED")



# This gets executed when you click Checkout.
@login_required
def proceed_order(request):
    if request.method == 'POST':
        request.session['address'] = request.POST['address']
        return redirect('payment')
    return render(request,'proceed_order.html')
