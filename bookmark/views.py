from django.shortcuts import render, get_object_or_404, redirect
from .models import Bookmark

# Daftar Bookmark
def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'bookmark/bookmark_list.html', {'bookmarks': bookmarks})

# Tambah Bookmark
def bookmark_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        description = request.POST.get('description')
        Bookmark.objects.create(title=title, url=url, description=description)
        return redirect('bookmark-list')
    return render(request, 'bookmark/bookmark_form.html')

# Edit Bookmark
def bookmark_update(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        bookmark.title = request.POST.get('title')
        bookmark.url = request.POST.get('url')
        bookmark.description = request.POST.get('description')
        bookmark.save()
        return redirect('bookmark-list')
    return render(request, 'bookmark/bookmark_form.html', {'bookmark': bookmark})

# Hapus Bookmark
def bookmark_delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        bookmark.delete()
        return redirect('bookmark-list')
    return render(request, 'bookmark/bookmark_confirm_delete.html', {'bookmark': bookmark})
