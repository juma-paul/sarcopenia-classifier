from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from .models import Data, ModelTwo, ModelThree

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = [
            'age', 'weight', 'height', 'hip', 'smoking',
            'smoking_packet_per_year', 'alcohol', 'education',
            'working_status', 'exercise', 'diabetes_mellitus',
            'asthma', 'hypertension', 'gender',
        ]

    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('age', css_class='form-group col-md-6 mb-0'),
                Column('weight', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('height', css_class='form-group col-md-6 mb-0'),
                Column('hip', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('smoking', css_class='form-group col-md-6 mb-0'),
                Column('smoking_packet_per_year', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('alcohol', css_class='form-group col-md-6 mb-0'),
                Column('education', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('working_status', css_class='form-group col-md-6 mb-0'),
                Column('exercise', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('diabetes_mellitus', css_class='form-group col-md-6 mb-0'),
                Column('asthma', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('hypertension', css_class='form-group col-md-6 mb-0'),
                Column('gender', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Get Results', css_class='btn btn-info btn-lg')
        )

class ModelTwoForm(forms.ModelForm):
    class Meta:
        model = ModelTwo
        fields = ['low_contraction_stress', 'contraction_stress', 'gait_speed']

    def __init__(self, *args, **kwargs):
        super(ModelTwoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('low_contraction_stress', css_class='form-group col-md-4 mb-0'),
                Column('contraction_stress', css_class='form-group col-md-4 mb-0'),
                Column('gait_speed', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit', css_class='btn-primary')
        )

class ModelThreeForm(forms.ModelForm):
    class Meta:
        model = ModelThree
        fields = ['low_grip_strength', 'grip_strength']

    def __init__(self, *args, **kwargs):
        super(ModelThreeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('low_grip_strength', css_class='form-group col-md-6 mb-0'),
                Column('grip_strength', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit', css_class='btn-success')
        )

