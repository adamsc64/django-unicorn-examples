from django_unicorn.components import UnicornView, QuerySetType
from django.shortcuts import render
from django.contrib.auth.models import User

from myapp.models import Resource, ResourceType


def index(request):
    return render(request, "myapp/index.html")


class TestView(UnicornView):
    resource: Resource = None
    resource_types: QuerySetType[ResourceType] = None

    def mount(self):
        self.request.user = self.get_or_create_user_in_session()

        company = self.request.user.userprofile.company
        self.resource_types = ResourceType.objects.filter(company=company)
        self.resource = Resource.objects.get(id=1)

    def save(self):
        self.resource.save()

    def get_or_create_user_in_session(self):
        # Check if user ID is stored in the session
        user_id = self.request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                return user
            except User.DoesNotExist:
                pass

        # If no user ID in session or user does not exist, get or create default user
        user = self.get_or_create_default_user()
        self.request.session['user_id'] = user.id
        return user


    def get_or_create_default_user(self):
        # Try to get the user with id=1
        try:
            user = User.objects.get(id=1)
        except User.DoesNotExist:
            # If the user does not exist, create it
            user = User.objects.create_user(username='defaultuser', password='defaultpassword')
            user.id = 1
            user.save()
        return user