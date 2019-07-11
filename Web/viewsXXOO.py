from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

#添加图书
from Web import settings
from book import models
from book.models import Book
from user.models import User

collections=[]
shoppingcars=[]

def book_add(request):
    if request.method == 'GET':
        return render(request, 'bookadd.html')
    # else:
    #     # title = request.POST.get('title')
    #     # content = request.POST.get('content')
    #     # author_id = request.POST.get('author')
    #     #
    #     # article = Article.objects.create(title=title, content=content, author_id=author_id)
    #     # user = User.objects.get(pk=author_id)
    #     # # print(user.article_set)
    #     # # article1 = Article.objects.get(pk=2)
    #     # # user.article_set.add(article1)
    #     #
    #     # # user.article_set.filter(id=article.id).delete()
    #     # # print(type(user.article_set))
    #     # user.article_set.filter(id=6).delete()  # 删除
    #     # return redirect(reverse('articles:show', kwargs={'id': author_id}))
    else:
        bookcover = request.FILES.get('bookcover')
        # bookcover = request.POST.get('bookcover')
        bookauthor = request.POST.get('bookauthor')
        bookcontent = request.POST.get('bookcontent')
        # book = Book.objects.create(bookcover=bookcover, bookauthor=bookauthor, bookcontent=bookcontent)
        # book.save()
        # book.bookcover.pic = (("books/" + bookcover.name),)
        book = Book.objects.create(bookcover=bookcover, bookauthor=bookauthor, bookcontent=bookcontent)
        if book and bookcover:
            return render(request, 'bookadd.html', context={'msg': "上传成功"})
    return render(request, 'bookadd.html', context={'msg': "上传失败"})

#展示图书
# def book_show(request):
#     books = Book.objects.all()
#     return render(request, 'bookshopXXX.html', context={'books': books})

#分页
def book_show(request):
    # books = models.Book.objects.all()
    # paginator = Paginator(books,3)  # Show 25 contacts per page
    # page = request.GET.get('page')
    # try:
    #     book_list = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     book_list = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     book_list = paginator.page(paginator.num_pages)
    #
    # return render(request, 'bookshopXXX.html', {'book_list': book_list})

    books = Book.objects.all()
    paginator = Paginator(books, 2)  # Paginator(对象列表，每页几条记录)
    # print(paginator.count)  # 总的条目数  总的记录数
    # print(paginator.num_pages)  # 可以分页的数量  总的页码数
    # print(paginator.page_range)  # 页面的范围

    # 方法： get_page()
    page = request.GET.get('page', 1)
    page = paginator.get_page(page)  # 返回的是page对象
    # page.has_next()  # 有没有下一页
    # page.has_previous()  # 判断是否存在前一页
    # page.next_page_number() # 获取下一页的页码数
    # page.previous_page_number() # 获取前一页的页码数

    # 属性：
    # object_list   当前页的所有对象
    #  number       当前的页码数
    # paginator     分页器对象

    return render(request, 'bookshop.html', context={'page': page})



def book_collectionshoppingcar(request):
    books = Book.objects.all()
    return render(request, 'bookcollectionshoppingcar.html', context={'books': books})

#图书收藏
def book_collection(request):
    # pass
    if request.is_ajax():
        bookname = request.GET.get('bookname')
        book = Book.objects.filter(bookname=bookname).first()
        if book.is_collection is False:
            if book.bookname not in collections:
                collections.append(book.bookname)
                book.is_collection = True
                book.save()
                data = {
                    'status': 201
                }
                return JsonResponse(data)
        if book.is_collection is True:
            if book.bookname in collections:
                collections.remove(book.bookname)
                book.is_collection = False
                book.save()
                data = {
                    'status': 200
                }
                return JsonResponse(data)
    return render(request, 'bookcollectionshoppingcar.html')


# def book_shoppingcar(request):
#     # pass
#     if request.is_ajax():
#         id = request.GET.get('bookid')
#         book = Book.objects.get(pk=id)
#         if book.is_buy is False:
#             if book.bookname not in shoppingcars:
#                 shoppingcars.append(book.bookname)
#                 book.is_buy = True
#                 book.save()
#                 data = {
#                     'status': 201
#                 }
#                 return JsonResponse(data)
#         if book.is_buy is True:
#             if book.bookname in shoppingcars:
#                 shoppingcars.remove(book.bookname)
#                 book.is_buy= False
#                 book.save()
#                 data = {
#                     'status': 200
#                 }
#                 return JsonResponse(data)
#     return render(request, 'bookcollectionshoppingcar.html')



















