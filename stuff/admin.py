from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet

from stuff.models import DependentChild, ParentWithDependentChildren


class DependentChildAdminForm(forms.ModelForm):
    """
    Form to test child dependency on parent object's validation
    """
    def clean(self):
        parent = self.cleaned_data.get('parent')
        if parent.contingent_field > 1 and (self.cleaned_data.get('dependent_field') 
                                            not in ("Snail Racing", "Underwater Golf")):
                raise ValidationError("You're doing it wrong")
        return super(DependentChildAdminForm, self).clean()


class DependentChildInlineFormSet(BaseInlineFormSet):
    """
    Alternate way of testing the permissions issue (may be at the
    formset level and not the form level)
    """
    def clean(self):
        for child_dict in self.cleaned_data:
            if (self.instance.contingent_field > 1 and 
                child_dict.get('dependent_field') not in ("Snail Racing", "Underwater Golf")):
                raise ValidationError("You're doing it wrong")
        return super(DependentChildInlineFormSet, self).clean()


class DependentChildInline(admin.TabularInline):
    model = DependentChild
    form = DependentChildAdminForm
    # uncomment this to test at the formset level
    #formset = DependentChildInlineFormSet


class ParentWithDependentChildrenAdminForm(forms.ModelForm):
    def clean_some_required_info(self):
        info = self.cleaned_data.get('some_required_info')
        if info.startswith('M'):
            raise ValidationError("Absolutely not!")
        return info


class ParentWithDependentChildrenAdmin(admin.ModelAdmin):
    form = ParentWithDependentChildrenAdminForm
    inlines = [DependentChildInline]
    
    
admin.site.register(ParentWithDependentChildren, ParentWithDependentChildrenAdmin)