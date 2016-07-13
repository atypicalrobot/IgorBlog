from django.views.generic.list import ListView
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from igor.contact.forms import ContactForm

# Create your views here.

from igor.contact.models import Address

class ContactListView(ListView):

    model = Address

    template_name = "contact.html"

    # def get_context_data(self, **kwargs):
    #     context = super(SectionListView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['tania.manolee@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "contact/email.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')