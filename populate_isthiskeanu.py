import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isthiskeanureeves_project.settings')

import django
django.setup()
from isthiskeanureeves.models import Category, Page, UserProfile, User
from django.template.defaultfilters import slugify
def populate():
    keanothim = [{"user": "2250052l","title": "Not Keanu"}]
    keanew = [{"user": "2250052l","title": "Young Keanu"}]
    topkeanu = [{"user": "2250052l","title": "Best Keanu"}]
	
    categories = {"topkeanu":{"title": "Top Keanu"},
    "keanew":{"title": "Kea New"},
    "keanothim":{"title": "Kea Not Him"}}

    for category, category_data in  categories.items():
	    c = add_category(category_data["title"])#, category_data["img"])




    users = [
            {"username": "2335980k",
             "email": "2335980k@student.gla.ac.uk",
             "password": "asd5849"
             },
             {"username": "HATEkeanu",
             "email": " ",
             "password": "a1234567"
             },
             {"username": "Yoshi",
             "email": " ",
             "password": "a1234567"
             },
             {"username": "fakekeanu",
             "email": " ",
             "password": "a1234567"
             },
             {"username": "hohohoho",
             "email": " ",
             "password": "a1234567"
             },
             {"username": "hoya",
             "email": "kkkk@gmail.com ",
             "password": "a1234567"
             },
             {"username": "keanuholic",
             "email": " ",
             "password": "a1234567"
             },
             {"username": "testprofile",
             "email": " ",
             "password": "a1234567"
             }]

    #for i in range(len(users)):
     #   new_user = users[i]
      #  u = add_user(new_user['username'],
       #              new_user['email'],
        #             new_user['password'])






      
#def add_category(name, image):
def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]#, img=image)[0]
	#c = Category.objects.get_or_create(name=name, img=image)[0]
    #c.rating = rating //OUT
    c.save()
    return c

#def add_user(username, email, password): // populate problem. ############################:
def add_user(username, email, password):
    user = User.objects.get_or_create(username=username, email=email)[0]
    user.set_password(password)
    user.save()
    slug_username = slugify(username)
    u = UserProfile.objects.get_or_create(username_slug=slug_username, user_id=user.id)[0]
    u.save()
    return u

# Starts execution here
if __name__ == '__main__':
    print("Starting isthiskeanureeves population script...")
    populate()
