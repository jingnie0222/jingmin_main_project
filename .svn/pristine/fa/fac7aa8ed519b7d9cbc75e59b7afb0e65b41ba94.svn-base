from django import forms


class FrontPressForm(forms.Form):
    code = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control col-md-9',
                'style': 'width:70%',
                'rows': '3',
            }),
        label='测试分支地址',
        required=True,
    )

    type = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control col-md-9',
                'style': 'width:70%'
            }),
        label='种类',
        required=True,
        choices=(
            ('0', 'wap'),
            ('1', 'pc'),
        ),
    )

    data_path = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control col-md-9',
                'style': 'width:70%',
                'rows': '3',
            }),
        label='数据文件路径',
        required=True,
    )