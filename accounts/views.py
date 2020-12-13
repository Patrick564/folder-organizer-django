from django.views.generic.edit import CreateView

from .models import User
from .forms import CreateUserForm


class CreateAccountView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'create_account.html'
    success_url = '/login/'
