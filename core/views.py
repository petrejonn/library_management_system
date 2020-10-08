from datetime import datetime
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView

from .models import Book, BookCategory, Borrow, LibraryUser, Department
from .forms import BorrowCreateForm


class HomeView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'dashboard/book/list.html'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'dashboard/book/create.html'
    success_url = reverse_lazy('core:home')
    fields = ['title', 'author', 'ISBN', 'copies',
              'publisher', 'copies_available', 'category', 'image']


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'dashboard/book/update.html'
    success_url = reverse_lazy('core:home')
    fields = ['title', 'author', 'ISBN', 'copies',
              'publisher', 'copies_available', 'category', 'image']


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'dashboard/book/delete.html'
    success_url = reverse_lazy('core:home')


class UserListView(LoginRequiredMixin, ListView):
    model = LibraryUser
    template_name = 'dashboard/user/list.html'


class UserCreateView(LoginRequiredMixin, CreateView):
    model = LibraryUser
    template_name = 'dashboard/user/create.html'
    success_url = reverse_lazy('core:user_list')
    fields = ['reg_no', 'first_name', 'last_name',
              'other_name', 'department', 'photo', 'phone']


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = LibraryUser
    template_name = 'dashboard/user/update.html'
    success_url = reverse_lazy('core:user_list')
    fields = ['reg_no', 'first_name', 'last_name',
              'other_name', 'department', 'photo', 'phone']


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = LibraryUser
    template_name = 'dashboard/user/delete.html'
    success_url = reverse_lazy('core:user_list')


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'dashboard/department/list.html'


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    template_name = 'dashboard/department/create.html'
    success_url = reverse_lazy('core:department_list')
    fields = ['name']


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    template_name = 'dashboard/department/update.html'
    success_url = reverse_lazy('core:department_list')
    fields = ['name']


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = 'dashboard/department/delete.html'
    success_url = reverse_lazy('core:department_list')


class CategoryListView(LoginRequiredMixin, ListView):
    model = BookCategory
    template_name = 'dashboard/category/list.html'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = BookCategory
    template_name = 'dashboard/category/create.html'
    success_url = reverse_lazy('core:category_list')
    fields = ['title']


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = BookCategory
    template_name = 'dashboard/category/update.html'
    success_url = reverse_lazy('core:category_list')
    fields = ['title']


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = BookCategory
    template_name = 'dashboard/category/delete.html'
    success_url = reverse_lazy('core:category_list')


class BorrowListView(LoginRequiredMixin, ListView):
    model = Borrow
    template_name = 'dashboard/borrow/list.html'


class BorrowCreateView(LoginRequiredMixin, CreateView):
    form_class = BorrowCreateForm
    template_name = 'dashboard/borrow/create.html'
    success_url = reverse_lazy('core:borrow_list')

    def get_initial(self):
        book = get_object_or_404(Book, id=self.kwargs.get("pk"))
        return {"book": book}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.issuing_staff = self.request.user
        self.object.book.copies_available = self.object.book.copies_available - 1
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class BorrowDetailView(LoginRequiredMixin, UpdateView):
    model = Borrow
    fields = []
    template_name = 'dashboard/borrow/detail.html'
    success_url = reverse_lazy('core:borrow_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.recieving_staff = self.request.user
        self.object.status = "Returned"
        self.object.date_returned = datetime.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
