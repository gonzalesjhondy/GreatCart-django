from category.models import category

def menu_links(request): #fetch all category from the database
    links = category.objects.all()
    return dict(links=links) 