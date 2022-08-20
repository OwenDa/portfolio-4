""" Social Network: Forms.py """
from django import forms
from django.forms import ModelForm
from .models import SocialLink, HistoryItem


class SocialLinkForm(ModelForm):
    """ Form to add social links """
    add_link = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    # hidden field for use in detecting form (see views.py)

    class Meta:
        """ Table fields to use in form """
        model = SocialLink
        fields = ('site_name', 'link',)


class HistoryItemForm(ModelForm):
    """ Form to add/edit history items """
    # add_history = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    # hidden field for use in detecting form (see views.py)

    class Meta:
        """ Table fields to use in form """
        model = HistoryItem
        fields = (
            'history_heading',
            'history_details',
            'history_role',
            'year',)
