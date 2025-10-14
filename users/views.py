from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

# 🔐 Vista Home protegida
@login_required
def home_view(request):
    """
    Esta vista será la página principal después del login.
    Solo usuarios autenticados pueden acceder.
    """
    return render(request, 'home.html')

class MyLogoutView(LogoutView):
    next_page = 'login'  # a dónde redirigir después del logout

    # Permite que logout funcione con GET
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)