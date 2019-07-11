from django.urls import path
from book.views import *

app_name = 'user'

urlpatterns = [
    path('bookadd', book_add, name='bookadd'),
    path('bookshow',book_show, name='bookshow'),
    # path('booklisting', book_listing, name='booklisting'),
    path('bookcollection', book_collection, name='bookcollection'),
    # path('bookshoppingcar', book_shoppingcar, name='bookshoppingcar'),
    path('bookcollectionshoppingcar', book_collectionshoppingcar, name='bookcollectionshoppingcar'),

]