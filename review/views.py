from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from .models import Library, Reviews


def login_view(request):
    msg = ''
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            msg = 'User not exist..!'

        else:
            login(request, user)
            return redirect('library_list_admin')

    return render(request, 'login.html', {'msg': msg})


@login_required(login_url='login')
def library_list_admin_view(request):  # For listing libraries for admin
    libraries = Library.objects.all()
    return render(request, 'library_list_admin.html', {'libraries': libraries})


@login_required(login_url='login')
def library_add_view(request):  # For adding new libraries by admin
    if request.method == 'POST':
        library = Library()
        library.name = request.POST.get('name')
        library.city = request.POST.get('city')
        library.address = request.POST.get('address')
        library.save()
        return redirect('library_list_admin')
    return render(request, 'library_add.html', {})


@login_required(login_url='login')
def library_edit_view(request, id):  # For editing existing library
    library = msg = ''
    if id:
        try:
            library = Library.objects.get(id=id)
        except:
            pass
    if request.method == 'POST':
        library.name = request.POST.get('name')
        library.city = request.POST.get('city')
        library.address = request.POST.get('address')
        library.save()
        return redirect('library_list_admin')
    return render(request, 'library_edit.html', {'library': library})


@login_required(login_url='login')
def library_delete_view(request, id):  # For deleting a library
    if id:
        library = Library.objects.get(id=id)
        library.delete()
    return redirect('library_list_admin')


def logout_view(request):
    logout(request)
    return redirect('login')


def library_view(request):  # For viewing the library list for public
    libraries = Library.objects.all()
    return render(request, 'library_list.html', {'libraries': libraries})


def library_detail_view(request, id):  # For viewing the individual library and reviews
    library = ''
    reviews = ''
    if id:
        library = Library.objects.get(id=id)
        reviews = Reviews.objects.filter(library__id=library.id, is_approve=True)

    if request.method == 'POST':  # For posting new review as a guest
        new_review = Reviews()
        new_review.library = library
        new_review.guest = request.POST.get('guest')
        new_review.address = request.POST.get('address')
        new_review.email = request.POST.get('email')
        new_review.review = request.POST.get('review')
        new_review.phone = request.POST.get('phone')
        new_review.save()
    return render(request, 'library.html', {'library': library, 'reviews': reviews})


@login_required(login_url='login')
def admin_library_detail(request, id):  # Detailed view of library for admin can delete or approve reviews.
    library = ''
    reviews = ''
    if id:
        library = Library.objects.get(id=id)
        reviews = Reviews.objects.filter(library__id=library.id)

    if request.method == 'POST' and 'approve' in request.POST:
        id = request.POST.get('approve')
        review = Reviews.objects.get(id=id)
        review.is_approve = True
        review.save()
        reviews = Reviews.objects.filter(library__id=library.id)

    if request.method == 'POST' and 'delete' in request.POST:
        id = request.POST.get('delete')
        review = Reviews.objects.get(id=id)
        review.delete()
        reviews = Reviews.objects.filter(library__id=library.id)

    return render(request, 'admin_library.html', {'library': library, 'reviews': reviews})


@login_required(login_url='login')
def profile_view(request):  # For viewing the admin profile and updating
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.Address = request.POST.get('address')
        user.mobile = request.POST.get('phone')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
    return render(request, 'profile.html', {'user': user})
