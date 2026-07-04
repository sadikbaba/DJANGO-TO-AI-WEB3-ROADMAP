from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"
    paginate_by = 4

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search:
            return Product.objects.filter(name__icontains=search)
        return Product.objects.all()
    

class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"