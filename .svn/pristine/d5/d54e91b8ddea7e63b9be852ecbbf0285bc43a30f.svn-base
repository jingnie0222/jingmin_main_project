from django import forms


class mission_filter_forms(forms.Form):
    mission_query_from = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control col-md-9',
                'style': 'width:70%',
            }),
        label='取词来源',
        required=False,
        choices=(
            ('', '未选择'),
            ('web', '网页'),
            ('wap', '无线'),
        ),
    )

    mission_user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-9',
                'style': 'width:70%',
            }),
        label='执行人员',
        required=False,
    )

    mission_status = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control col-md-9',
                'style': 'width:70%'
            }),
        label='任务状态',
        required=False,
        choices=(
            ('', '未选择'),
            ('Running', '进行中'),
            ('Finish', '已结束'),
            ('Waiting', '等待中'),
            ('Failed', '未成功'),
        ),
    )


class mission_add_forms(forms.Form):
    mission_type = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control',
                                   'style': 'width:60%'}),
        label='任务模式选择',
        required=True,
        choices=(('query_for_id', 'ID对应查询词'),
                 ('multi_id_query', 'ID交叉查询词'),
                 ),
    )
    vrid_mode = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control',
                                   'style': 'width:60%'}),
        label='VRID模式选择',
        required=True,
        choices=(('0', '预设方案'),
                 ('1', '地址读取'),
                 ('2', '网页输入'),
                 ),
    )

    vrid_preserved = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(
            attrs={'class': 'form-control',
                   'size': '6',
                   'style': 'width:60%',
                   'form-type': 'query_for_id multi_id_query', }),
        label='预设分类选择(按住Ctrl键可多选)',
        required=False,
        choices=(('0', '内部VR(1开头)'),
                 ('1', '外部VR(2,4开头)'),
                 ('2', '结构化(3开头)'),
                 ('3', '知立方(5开头)'),
                 ('4', '多命中VR(7开头00)'),
                 ('5', '多命中VR(7开头01-99)'),
                 ),
        error_messages={
            'invalid': '请至少选择一个',
        }
    )

    vrid_url = forms.URLField(
        widget=forms.URLInput(attrs={'class': 'forms-control',
                                     'style': 'width:60%'}),
        label='VRID获取地址(每行一个id)',
        required=False,
        initial="http://target.txt",
        max_length=100,
    )

    vrid_custom = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'forms-control',
                                     'rows': '5',
                                     'placeholder': '每行一个',
                                     'style': 'width:60%', }),
        label='VRID自定义(每行一个id)',
        required=False,
        max_length=2000,
    )

    query_from = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'width:60%',
            }),
        label='来源选取',
        required=True,
        choices=(
            ('web', '网页'),
            ('wap', '无线'),
        ),
    )

    query_count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'style': 'width:60%',
                                        'placeholder': '最大100',
                                        'form-type': 'query_for_id', }),
        label='取词数(最大100)',
        required=True,
        initial=10,
        max_value=100,
        min_value=1,
    )

    query_count_for_7 = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control',
                   'style': 'width:60%',
                   'placeholder': '最大50',
                   'form-type': 'query_for_id', }),
        label='子取词数(最大50)(对7开头01-99生效)',
        required=True,
        initial=5,
        max_value=50,
        min_value=1,
    )

    query_count_for_multi = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control',
                   'style': 'width:60%',
                   'placeholder': '最大5000',
                   'form-type': 'multi_id_query', }),
        label='取词数(最大5000)',
        required=True,
        initial=10,
        max_value=5000,
        min_value=1,
    )

    result_format = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'forms-control',
                   'placeholder': '默认已带query,vrid',
                   'style': 'width:60%', }),
        label='选取字段',
        required=False,
    )

    result_order = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'forms-control',
                   'placeholder': '填需要倒排的字段',
                   'style': 'width:60%', }),
        label='排序字段',
        required=False,
    )

    result_encode = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'style': 'width:60%', }),
        label='结果编码',
        required=True,
        choices=(('utf8', 'utf8'), ('gbk', 'gbk')),
        initial='0',
    )
