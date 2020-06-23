from django import forms

class MyForm(forms.Form):
    # text = forms.CharField(label='文字入力', max_length=100, help_text='100characters max')
    # gender = forms.IntegerField(label='数量')
    gender = forms.ChoiceField(choices = (
            (0, '男性'),
            (1, '女性'),
        ),  
        widget=forms.widgets.Select(attrs={
                'class' : 'btn btn-lg btn-block btn-outline-primary',
                'id': 'select1'}),
    )

    grade = forms.ChoiceField(widget = forms.Select(attrs={
        'class': "btn btn-lg btn-block btn-primary",
        'id': 'select2'
    }), 
        choices = ([('1','First-class'), ('2','Second-class'),('3','Third-class'), ]), initial='3')

    fare = forms.IntegerField(
        label='ドル', 
        initial=0,
        min_value=0,
        max_value=2500,
        widget=forms.TextInput(attrs={
                'class' : 'btn btn-lg btn-block btn-outline-primary',
                'id': 'select3'
        }),
    )
        
    # fields.IntegerRangeField(range(0, 2550))

# forms.TextInput(attrs={'class' : 'myfieldclass'}),
# widget はHTMLの属性を与える
"""
def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = TextInput(attrs={
            'id': 'myCustomId',
            'class': 'myCustomClass',
            'name': 'myCustomName',
            'placeholder': 'myCustomPlaceholder'})
"""