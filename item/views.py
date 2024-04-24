from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import NewItemForm, EditItemForm
from django.contrib.auth.decorators import login_required
from django.db import connection


# Create your views here.

def indexing():
    indexes = [
        Item.Index(fields=['type', 'name']),
    ]
    return indexes

def get_detail(req, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(type=item.type, name=item.name)
    return render(req, 'item/detail.html', {'item': item, 'related_items': related_items})

def detail(req, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(type=item.type, is_sold=False).exclude(pk=pk)[0:5]
    return render(req, 'item/detail.html', {'item': item, 'related_items': related_items})

@login_required
def new(req):
    if req.method == "POST":
        form = NewItemForm(req.POST, req.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.posted_by = req.user
            item.save()
            return redirect('item:detail', pk=item.id)

    else: 
        form = NewItemForm()
    return render(req, 'item/form.html', {'form': form, 'title': "Add Item"})

@login_required
def delete(req, pk):
    # Use a prepared SQL statement to delete the pants
    sql_delete = "DELETE FROM item_item WHERE id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql_delete, [pk])
    return redirect('dashboard:index')


# def delete(req, pk):
#     item = get_object_or_404(Item, pk=pk, posted_by=req.user)
#     item.delete()

#     return redirect('dashboard:index')

@login_required
def edit(req, pk):
    item = get_object_or_404(Item, pk=pk, posted_by=req.user)

    if req.method == 'POST':
        form = EditItemForm(req.POST, req.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(req, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

# bearta.josh newaccountplease