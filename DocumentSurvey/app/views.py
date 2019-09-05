from django.shortcuts import render, redirect, get_object_or_404
from .models import Document, AccessKey, DocumentGroup

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def _render(request, template, context=None):
    if context == None:
        context = {}
    context['request'] = request
    context['ip'] = get_client_ip(request)
    return render(request, template, context=context)

def authenticate(request):
    request.session.flush()
    error = None
    if request.method == "POST":
        key = request.POST.get("access-key", "")
        if key == "":
            error = "Please provide an access key."
        else:
            access_key = AccessKey.objects.filter(key=key)
            if access_key.exists():
                access_key = access_key[0]
                access_key.imprecise_uses += 1
                access_key.save()
                documents = Document.objects.filter(group=access_key.group).order_by("imprecise_views")
                if documents.count() == 0:
                    error = "No document to display!"
                else:
                    request.session["document"] = documents[0].id
                    return redirect("/document")
            else:
                error = "Please provide a valid access key."
    return _render(request, "core/authenticate.html", context={"error": error})

def document(request):
    document_id = request.session.get("document", None)
    if document_id == None:
        return redirect("/")
    document = get_object_or_404(Document, id=document_id)
    document.imprecise_views += 1
    document.save()
    return _render(request, "core/document.html", context={"document": document})

def index(request):
    document = request.session.get("document", None)
    if document == None:
        return redirect("/authenticate")
    else:
        return redirect("/document")