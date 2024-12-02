from django.contrib import admin
from .models import Data, ModelTwo, ModelThree

class DataAdmin(admin.ModelAdmin):
    list_display = (
        'age',
        'weight',
        'height',
        'hip',
        'smoking',
        'smoking_packet_per_year',
        'alcohol',
        'education',
        'working_status',
        'exercise',
        'diabetes_mellitus',
        'asthma',
        'hypertension',
        'gender',
        'message',
        'display_probability_model1',
    )

    def display_probability_model1(self, obj):
        if obj.probability_model1:
            return [round(float(prob), 4) for prob in obj.probability_model1]
        else:
            return "Not Calculated"
    display_probability_model1.short_description = "Model 1 Probability"

class ModelTwoAdmin(admin.ModelAdmin):
    list_display = (
        'data',
        'low_contraction_stress',
        'contraction_stress',
        'gait_speed',
        'display_probability_model2',
    )

    def display_probability_model2(self, obj):
        if obj.data.probability_model2:
            return [round(float(prob), 4) for prob in obj.data.probability_model2]
        else:
            return "Not Calculated"
    display_probability_model2.short_description = "Model 2 Probability"

class ModelThreeAdmin(admin.ModelAdmin):
    list_display = (
        'model_two',
        'low_grip_strength',
        'grip_strength',
        'display_probability_model3',
    )

    def display_probability_model3(self, obj):
        if obj.model_two.data.probability_model3:
            return [round(float(prob), 4) for prob in obj.model_two.data.probability_model3]
        else:
            return "Not Calculated"
    display_probability_model3.short_description = "Model 3 Probability"


admin.site.register(Data, DataAdmin)
admin.site.register(ModelTwo, ModelTwoAdmin)
admin.site.register(ModelThree, ModelThreeAdmin)
