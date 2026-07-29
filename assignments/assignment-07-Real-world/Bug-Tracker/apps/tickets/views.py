from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TicketForm
from .models import Ticket

@login_required
def ticket_create_view(request):

    if request.method == "POST":

        form = TicketForm(request.POST)

        if form.is_valid():

            ticket = form.save(commit=False)

            ticket.reporter = request.user

            ticket.save()

            return redirect("core:dashboard")

    else:

        form = TicketForm()

    return render(
        request,
        "tickets/ticket_create.html",
        {
            "form": form,
        },
    )


@login_required
def ticket_list_view(request):

    tickets = Ticket.objects.all()

    return render(
        request,
        "tickets/ticket_list.html",
        {
            "tickets": tickets,
        },
    )

@login_required
def ticket_detail_view(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        pk=ticket_id,
    )

    return render(
        request,
        "tickets/ticket_detail.html",
        {
            "ticket": ticket,
        },
    )

@login_required
def ticket_edit_view(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        pk=ticket_id,
    )

    if request.method == "POST":

        form = TicketForm(
            request.POST,
            instance=ticket,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "tickets:detail",
                ticket.pk,
            )

    else:

        form = TicketForm(
            instance=ticket,
        )

    return render(
        request,
        "tickets/ticket_edit.html",
        {
            "form": form,
            "ticket": ticket,
        },
    )

@login_required
def ticket_delete_view(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        pk=ticket_id,
    )

    if request.method == "POST":

        ticket.delete()

        return redirect("tickets:list")

    return render(
        request,
        "tickets/ticket_delete.html",
        {
            "ticket": ticket,
        },
    )