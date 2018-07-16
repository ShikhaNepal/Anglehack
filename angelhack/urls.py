from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

def get_index():
    return "Hello world"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='login.html'),name='login'),
    path('appointment', TemplateView.as_view(template_name='appointment.html'),name='appointment'),
    path('demo', TemplateView.as_view(template_name='demo.html'),name='demo'),
    path('emergency', TemplateView.as_view(template_name='emergency.html'),name='emergency'),
    path('history', TemplateView.as_view(template_name='history.html'),name='history'),
    path('john', TemplateView.as_view(template_name='john.html'),name='john'),
    path('medicine', TemplateView.as_view(template_name='medicine.html'),name='medicine'),
    path('overview', TemplateView.as_view(template_name='overview.html'),name='overview'),
    path('card', TemplateView.as_view(template_name='card.html'),name='card'),
]
urlpatterns += [
    # path('charts/',TemplateView.as_view(template_name='s/charts.js',content_type='application/javascript'),name='echarts'),
    path('main/',TemplateView.as_view(template_name='s/main.css',content_type='text/css'),name='main'),
    path('font/',TemplateView.as_view(template_name='s/font.css',content_type='text/css'),name='font'),
    path('second/',TemplateView.as_view(template_name='s/second.css',content_type='text/css'),name='second'),
]


