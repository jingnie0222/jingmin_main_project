from django import forms
from .models import LizhiAccuResult


class ListFilter(forms.Form):
    lizhi_type = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'width:60%',
            }),
        label='立知分类',
        required=True,
        choices=(
            ('99', '全部'),
            ('0', '未标记'),
            ('1', '图谱'),
            ('2', 'VR'),
            ('3', '立知短答案'),
            ('4', '立知长答案'),
            ('5', '优质问答'),
        ),
        # default='0',
    )

    focus_member = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'forms-control',
                'style': 'width:60%',
            }),
        label='关注人',
        required=False,
    )


class CaseDetailStatus(forms.ModelForm):
    status = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'width:100%',
            }),
        label='处理状态',
        required=True,
        choices=(
            ('0', '未解决'),
            ('1', '已解决'),
            ('2', '无问题'),
        )
    )

    precision = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'width:100%',
            }),
        label='判定结果',
        required=True,
        choices=(
            ('0', '未处理'),
            ('1', '错误'),
            ('2', '需要改进'),
            ('3', '效果正常'),
        ),
    )

    solve_time = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'style': 'width:100%',
            }
        ),
        label='预计解决时间',
        required=False,
        initial=''
    )

    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'forms-control',
                                     'rows': '2',
                                     # 'placeholder': '每行一个',
                                     'style': 'width:100%', }),
        label='备注',
        max_length=107374,
        required=False,
    )

    lizhi_type = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'width:100%',
            }),
        label='立知分类',
        required=True,
        choices=(
            ('0', '未标记'),
            ('1', '图谱'),
            ('2', 'VR'),
            ('3', '立知短答案'),
            ('4', '立知长答案'),
            ('5', '优质问答'),
        ),
        # default='0',
    )

    focus_member = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'forms-control',
                'style': 'width:100%',
            }),
        label='关注人',
        required=False,
    )

    itest_record_title = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'forms-control',
                'style': 'width:100%',
            }),
        label='问题记录标题',
    )

    # is_next = forms.ChoiceField(
    #     widget=forms.CheckboxInput(
    #         attrs={
    #             'style': 'display:none',
    #         }
    #     ),
    #     choices=(
    #         (True, True),
    #         (False, False),
    #     ),
    #     required=False,
    # )

    class Meta:
        model = LizhiAccuResult
        fields = [
            'status', 'precision', 'solve_time',
            'comments', 'lizhi_type', 'focus_member',
            'itest_record_title',
        ]
