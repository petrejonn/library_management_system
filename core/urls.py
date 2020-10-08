from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = "core"

urlpatterns = [
    path(r'', views.HomeView.as_view(), name='home'),
    path(r'dashboard/book/create/',
         views.BookCreateView.as_view(), name='book_create'),
    path(r'dashboard/book/update/<int:pk>',
         views.BookUpdateView.as_view(), name='book_update'),
    path(r'dashboard/book/delete/<int:pk>',
         views.BookDeleteView.as_view(), name='book_delete'),

    path(r'dashboard/category/list',
         views.CategoryListView.as_view(), name='category_list'),
    path(r'dashboard/category/create/',
         views.CategoryCreateView.as_view(), name='category_create'),
    path(r'dashboard/category/update/<int:pk>',
         views.CategoryUpdateView.as_view(), name='category_update'),
    path(r'dashboard/category/delete/<int:pk>',
         views.CategoryDeleteView.as_view(), name='category_delete'),

    path(r'dashboard/user/list',
         views.UserListView.as_view(), name='user_list'),
    path(r'dashboard/user/create/',
         views.UserCreateView.as_view(), name='user_create'),
    path(r'dashboard/user/update/<int:pk>',
         views.UserUpdateView.as_view(), name='user_update'),
    path(r'dashboard/user/delete/<int:pk>',
         views.UserDeleteView.as_view(), name='user_delete'),

    path(r'dashboard/department/list',
         views.DepartmentListView.as_view(), name='department_list'),
    path(r'dashboard/department/create/',
         views.DepartmentCreateView.as_view(), name='department_create'),
    path(r'dashboard/department/update/<int:pk>',
         views.DepartmentUpdateView.as_view(), name='department_update'),
    path(r'dashboard/department/delete/<int:pk>',
         views.DepartmentDeleteView.as_view(), name='department_delete'),

    path(r'dashboard/borrow/list',
         views.BorrowListView.as_view(), name='borrow_list'),
    path(r'dashboard/borrow/create/<int:pk>',
         views.BorrowCreateView.as_view(), name='borrow_create'),
    path(r'dashboard/borrow/detail/<int:pk>',
         views.BorrowDetailView.as_view(), name='borrow_detail'),


    path(r'accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path(r'accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
]
