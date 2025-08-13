from django import forms
from tasks.models import Event, EventDetail

class EventForm(forms.Form):
    title = forms.CharField(max_length=250, label="Task Title")
    description = forms.CharField(widget=forms.Textarea, label='Task Description')
    due_date = forms.DateField(widget=forms.SelectDateWidget, label="Due Date")
    assigned_to = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, 
        choices=[], 
        label='Assigned To'
    )

    # def __init__(self, *args, **kwargs):
    #     participants = kwargs.pop('Participant')
    #     super().__init__(*args, **kwargs)
    #     self.fields['assigned_to'].choices = [
    #         (participant.id, participant.name) for participant in participants
     #   ]
    def __init__(self, *args, **kwargs):
        # print(args, kwargs)
        participants = kwargs.pop("participants", [])
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices = [
            (pats.id, pats.name) for pats in participants]

class StyledFormMixin:
    """Mixin to apply style to form fields"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder': f"Enter {field.label.lower()}",
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": "border-2 border-gray-300 p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': "space-y-2"
                })
            else:
                field.widget.attrs.update({
                    'class': self.default_classes
                })

class EventModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'due_date', 'assigned_to'] 
        widgets = {
            'due_date': forms.SelectDateWidget,
            'assigned_to': forms.CheckboxSelectMultiple
        }
        
    # def __init__(self, *args, **kwargs):
    #     participants = kwargs.pop('Participant', Participant.objects.all())
    #     super().__init__(*args, **kwargs)
    #     self.fields['assigned_to'].queryset = participants
    #     self.apply_styled_widgets()

class EventDetailModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = EventDetail
        fields = ['priority', 'notes']










































# from django import forms
# from tasks.models import Event, EventDetail, Participant




# class EventForm(forms.Form):
#     title = forms.CharField(max_length=250, label="Task Title")
#     description = forms.CharField(widget=forms.Textarea, label='Task Description')
#     due_date = forms.DateField(widget=forms.SelectDateWidget, label="Due Date")
#     assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[], label='Assigned To')

#     def __init__(self, *args, **kwargs):
#             # print(args, kwargs)
#             participants = kwargs.pop('participants', Participant.objects.all())
#             super().__init__(*args, **kwargs)
#             self.fields['assigned_to'].choices = [
#             (pats.id, pats.name) for pats in participants]
#              # Customize the assigned_to field queryset
#             self.fields['assigned_to'].queryset = participants




# class StyledFormMixin:
#     """ Mixing to apply style to form field"""

#     default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"

#     def apply_styled_widgets(self):
#         for field_name, field in self.fields.items():
#             if isinstance(field.widget, forms.TextInput):
#                 field.widget.attrs.update({
#                     'class': self.default_classes,
#                     'placeholder': f"Enter {field.label.lower()}"
#                 })
#             elif isinstance(field.widget, forms.Textarea):
#                 field.widget.attrs.update({
#                     'class': f"{self.default_classes} resize-none",
#                     'placeholder':  f"Enter {field.label.lower()}",
#                     'rows': 5
#                 })
#             elif isinstance(field.widget, forms.SelectDateWidget):
#                 print("Inside Date")
#                 field.widget.attrs.update({
#                     "class": "border-2 border-gray-300 p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
#                 })
#             elif isinstance(field.widget, forms.CheckboxSelectMultiple):
#                 print("Inside checkbox")
#                 field.widget.attrs.update({
#                     'class': "space-y-2"
#                 })
#             else:
#                 print("Inside else")
#                 field.widget.attrs.update({
#                     'class': self.default_classes
#                 })











# # Django Model Form


# class EventModelForm(StyledFormMixin, forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['title', 'description', 'due_date', 'assigned_to']
#         widgets = {
#             'due_date': forms.SelectDateWidget,
#             'assigned_to': forms.CheckboxSelectMultiple
#         }
        
#     """ Widget using mixins """
#     def __init__(self, *arg, **kwarg):
#         super().__init__(*arg, **kwarg)
#         self.apply_styled_widgets()



# class EventDetailModelForm(StyledFormMixin, forms.ModelForm):
#     class Meta:
#         model = EventDetail
#         fields = ['priority', 'notes']

#     def __init__(self, *arg, **kwarg):
#         super().__init__(*arg, **kwarg)
#         self.apply_styled_widgets()
















# class EventModelForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['title', 'description', 'due_date', 'assigned_to']
#         widgets = {
#             'title': forms.TextInput(),
#             'due_date': forms.SelectDateWidget,
#             'assigned_to': forms.CheckboxSelectMultiple
#         }

            


# # class EventForm(forms.ModelForm):
# #     class Meta:
# #         model = Event
# #         fields = ['name', 'description', 'date', 'time', 'location', 'category']
# #         widgets = {
# #             'date': forms.DateInput(attrs={'type': 'date'}),
# #             'time': forms.TimeInput(attrs={'type': 'time'}),
# #             'description': forms.Textarea(attrs={'rows': 3}),
# #         }

# # class ParticipantForm(forms.ModelForm):
# #     class Meta:
# #         model = Participant
# #         fields = ['name', 'email', 'events']
# #         widgets = {
# #             'events': forms.CheckboxSelectMultiple(),
# #         }

# # class CategoryForm(forms.ModelForm):
#     # class Meta:
#     #     model = Category
#     #     fields = ['name', 'description']
#     #     widgets = {
#     #         'description': forms.Textarea(attrs={'rows': 3}),
#     #     }