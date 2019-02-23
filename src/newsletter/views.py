from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from .forms import SignUpForm, ContactForm


# Create your views here.
def home(request):
    title = "Welcome"
    # if request.user.is_authenticated():
    #     title = "Hello, %s"%(request.user)
    #add a form
    # if request.method == "POST":
    #     print(request.POST)
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
    context = {
        "title": title, #for using key in templates in {{ key }}
        "form": form,
    }
    return render(request, "home.html", context)


def contact(request):
    title = "Contact us!"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
        subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'yourotheremail@gmail.com']
        contact_message = "{}:\n{} \nvia {}".format(
            form_full_name,
            form_message,
            form_email)
        print(form_email, form_message, form_full_name)
        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=False,
        )

    context = {
        "form": form,
        "title": title
    }
    return render(request, "forms.html", context)
