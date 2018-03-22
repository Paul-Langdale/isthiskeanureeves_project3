import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isthiskeanureeves_project.settings')

import django
django.setup()
from isthiskeanureeves.models import Category, Page, UserProfile, User

def populate():
    keanothim = [{"user": "2250052l","title": "Not Keanu"}]
    keanew = [{"user": "2250052l","title": "Young Keanu"}]
    topkeanu = [{"user": "2250052l","title": "Best Keanu"}]
	
    categories = {"topkeanu":{"title": "Top Keanu"},
    "keanew":{"title": "Kea New"},
    "keanothim":{"title": "Kea Not Him"}}

    for category, category_data in  categories.items():
	    c = add_category(category_data["title"])#, category_data["img"])



      
#def add_category(name, image):
def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]#, img=image)[0]
	#c = Category.objects.get_or_create(name=name, img=image)[0]
    #c.rating = rating //OUT
    c.save()
    return c

# Starts execution here
if __name__ == '__main__':
    print("Starting isthiskeanureeves population script...")
    populate()