from django import forms

class PasteForm(forms.Form):
    title = forms.CharField(max_length=150, label="Paste Title", required=False, 
                            widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}))
    author = forms.CharField(max_length=150, label="Your Name", required=False, 
                             widget=forms.TextInput(attrs={'placeholder': 'Author Name', 'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Paste Content', 'class': 'form-control'}),
                              label="Paste Content", required=True)
    language = forms.CharField(
        max_length=150, label="Paste Language", required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Language', 'class': 'form-control'}))
