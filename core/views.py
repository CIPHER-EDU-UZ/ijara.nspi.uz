from django.shortcuts import render, redirect
from django.contrib import messages
from openpyxl import load_workbook
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.views.generic.list import ListView

def upload_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')

        if not excel_file.name.endswith('.xlsx'):
            messages.error(request, 'Please upload a valid Excel file (.xlsx)')
        else:
            try:
                workbook = load_workbook(excel_file)
                sheet = workbook.active

                for row in sheet.iter_rows(min_row=2, values_only=True):
                    if len(row) >= 8:
                        Shahar, Mahallasi, Manzil, Ijarachi, Telefon, Yigit, Qiz, Holati, *extra = row
                        
                        # Set empty cells to None
                        if not any(cell for cell in row):
                            Shahar = Mahallasi = Manzil = Ijarachi = Telefon = Yigit = Qiz = Holati = None
                        
                        Home.objects.create(
                            Shahar=Shahar, Mahallasi=Mahallasi, Manzil=Manzil,
                            Ijarachi=Ijarachi, Telefon=Telefon, Yigit=Yigit,
                            Qiz=Qiz, Holati=Holati
                        )
                    else:
                        messages.error(request, 'Row does not contain enough values')

                messages.success(request, 'Data from Excel file imported successfully')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')

    return render(request, 'upload_excel.html')

# class Home(ListView):
#     paginate_by = 25
#     template_name = 'index.html'
#     model = Home
#     context_object_name = 'ijara' 


class HomeListView(ListView):
    paginate_by = 25
    template_name = 'index.html'
    model = Home
    context_object_name = 'ijara'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ArizaForm()  # Add the form to the context
        return context

    def post(self, request, *args, **kwargs):
        form = ArizaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home_list view after successful submission
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(request, self.index.html, context)

home_list_view = HomeListView.as_view()

def test(request):
    ts = Test.objects.all()
    return render(request, 'test.html', {'ts':ts})