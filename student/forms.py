from django import forms
from django.forms import ClearableFileInput
from django.shortcuts import render


from .models import Student, Project, WorkingExperience, VolunteerExperience, Language, Skill


from dal import autocomplete

# ClearableFileInput.template_name = 'django_overrides/forms/widgets/clearable_file_input.html'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user', )
        widgets = {
            'soft_skills': autocomplete.ModelSelect2Multiple(url='soft-autocomplete'),
            'hard_skills': autocomplete.ModelSelect2Multiple(url='hard-autocomplete'),
            'programming_language': autocomplete.ModelSelect2Multiple(url='plang-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields["programming_language"].queryset = Skill.objects.filter(skill_type="programming_language")
        self.fields["soft_skills"].queryset = Skill.objects.filter(skill_type="soft")
        self.fields["hard_skills"].queryset = Skill.objects.filter(skill_type="hard")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('__all__')
        widgets = {
            'technologies': autocomplete.ModelSelect2Multiple(url='tech-autocomplete'),
            'collaborators': autocomplete.ModelSelect2Multiple(url='users-autocomplete'),
        }

        #
    # def __init__(self, *args, **kwargs):
    #     super(ProjectForm, self).__init__(*args, **kwargs)
    #     # self.fields["collaborators"].widget = forms.widgets.CheckboxSelectMultiple()


class WorkingExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkingExperience
        exclude = ('user',)


class VolunteerExperienceForm(forms.ModelForm):
    class Meta:
        model = VolunteerExperience
        exclude = ('user',)


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        exclude = ('user',)

class StudentSearch(forms.ModelForm):
  pass

