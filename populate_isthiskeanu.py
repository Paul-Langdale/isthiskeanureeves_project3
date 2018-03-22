import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isthiskeanureeves_project.settings')

import django
django.setup()
from isthiskeanureeves.models import Category, Page, UserProfile, User

def populate():


      categories = {"Top keanu":{"title": "Top keanu","img": "youngkeanu.jpg"},
                  "Kea-New":{"title": "Kea-New","img": "bluekeanu.jpg"},
                  "KEAN-NOT HIM":{"title": "KEAN-NOT HIM","img": "notkeanu.jpg"}}

      for category, category_data in  categories.items():
                       c = add_category(category_data["title"], category_data["img"])



      
def add_category(name, image):
       c = Category.objects.get_or_create(name=name, img=image)[0]
       #c.rating = rating //OUT
       c.save()
       return c

# Starts execution here
if __name__ == '__main__':
    print("Starting isthiskeanureeves population script...")
    populate()
