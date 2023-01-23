from .models import Visitor, Bedroom_size, Bedroom_type, Bedroom, Book, Review, Simple_Reviews
from django import forms
class VisitorForm(forms.Form):
    class Meta:
        model = Visitor
        fields = '__all__'

class Bedroom_typeForm(forms.Form):
    class Meta:
        model = Bedroom_type
        fields = '__all__'
        
class Bedroom_sizeForm(forms.Form):
    class Meta:
        model = Bedroom_size
        fields = '__all__'

class BedroomForm(forms.Form):
    class Meta:
        model = Bedroom
        fields = '__all__'

class BookForm(forms.Form):
    class Meta:
        model = Book
        fields = '__all__'
        
class ReviewForm(forms.Form):
    class Meta:
        model = Review
        fields = '__all__'
    
class Simple_reviewForm(forms.Form):
    class Meta:
        model = Simple_Reviews
        fields = '__all__'



    


