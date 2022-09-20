from asyncio import events
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Events

class EventsFeaturedListView(ListView):
    template_name = "events/list.html"
    
    def get_queryset(self, *args, **kwargs):
        return Events.objects.featured()

class EventsFeaturedDetailView(DetailView):
    queryset = Events.objects.all().featured()
    template_name = "events/featured-detail.html"

#Class Based View
class EventsListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada #
    queryset = Events.objects.all()
    template_name = "events/list.html"
    
    #def get_context_data(self, *args, **kwargs):
    #    context = super(EventsListView, self).get_context_data(*args, **kwargs)
    #    print(context)
    #    return context

#Function Based View
def events_list_view(request):
    queryset = Events.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "events/list.html", context)

class EventsDetailSlugView(DetailView):
    queryset = Events.objects.all()
    template_name = "events/detail.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Product, slug = slug, active = True)
        try:
            instance = Events.objects.get(slug = slug, active = True)
        except Events.DoesNotExist:
            raise Http404("Não encontrado!")
        except Events.MultipleObjectsReturned:
            qs = Events.objects.filter(slug = slug, active = True)
            instance =  qs.first()
        return instance

#Class Based View
class EventsDetailView(DetailView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    #queryset = Events.objects.all()
    template_name = "events/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(EventsDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Events.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance



#Function Based View
def events_detail_view(request, pk = None, *args, **kwargs):
    instance = Events.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("Esse produto não existe!")

    context = {
        'object': instance
    }
    return render(request, "events/detail.html", context)

