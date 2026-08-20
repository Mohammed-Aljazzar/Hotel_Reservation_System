from django import forms 
from .models import PropertyBook, PropertyReview, Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'image', 'price', 'description', 'place', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
        }

class PropertyBookForm(forms.ModelForm):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    
    class Meta:
        model = PropertyBook
        fields = ['date_from','date_to','guest','childern']
        
    

class PropertyReviewForm(forms.ModelForm):
    class Meta:
        model = PropertyReview
        fields = ['rate','feedback']