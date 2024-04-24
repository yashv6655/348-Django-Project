from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from item.models import Item
# Create your views here.

from django.db import connection

def index(req):
    # Build the raw SQL query
    sql_query = """
        SELECT * 
        FROM item_item 
        WHERE posted_by_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(sql_query, [req.user.id])
        # Fetch all the rows from the result set
        rows = cursor.fetchall()

    items = []
    for row in rows:
        item = Item(
            id=row[0],
            type_id=row[1],
            name=row[2],
            description=row[3],
            price=row[4],
            is_sold=row[5],
            posted_by_id=row[6],
            image=row[7]
        )
        items.append(item)

    queryset = Item.objects.raw(sql_query, [req.user.id])

    return render(req, 'dashboard/index.html', {'items': queryset})

# @login_required
# def index(req):
#     items = Item.objects.filter(posted_by=req.user)
#     print(items)
#     return render(req, 'dashboard/index.html', {'items': items})