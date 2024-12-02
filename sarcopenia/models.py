from django.db import models
import joblib

GENDER_CHOICES = (
    ('0', 'Female'),
    ('1', 'Male'),
)

SMOKING_CHOICES = (
    ('0.0', 'No'),
    ('1.0', 'Yes'),
)

ALCOHOL_CHOICES = (
    ('0', 'None'),
    ('social', 'Social'),
    ('regular', 'Regular'),
)

EDUCATION_CHOICES = (
    ('primary school', 'Primary School'),
    ('high school', 'High School'),
    ('university', 'University'),
    ('other', 'Other'),
    ('illiterate', 'None'),
)

WORKING_STATUS_CHOICES = (
    ('retired', 'Retired'),
    ('working', 'Working'),
    ('unemployed', 'Unemployed'),
)

EXERCISE_CHOICES = (
    ('0', 'None'),
    ('1-2/week', '1 - 2 Per Week'),
    ('3-4/week', '3 - 4 Per Week'),
)

DIABETES_CHOICES = (
    ('0', 'No'),
    ('1', 'Yes'),
)

ASTHMA_CHOICES = (
    ('0.0', 'No'),
    ('1.0', 'Yes'),
)

HYPERTENSION_CHOICES = (
    ('0', 'No'),
    ('1', 'Yes'),
)

LOW_CONTRACTION_STRESS_CHOICES = (
    ('0.0', 'No'),
    ('1.0', 'Yes'),
)

LOW_GRIP_STRENGTH_CHOICES = (
    ('0.0', 'No'),
    ('1.0', 'Yes'),
)

class Data(models.Model):
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    hip = models.FloatField()
    smoking = models.CharField(max_length=10, choices=SMOKING_CHOICES)
    smoking_packet_per_year = models.PositiveIntegerField()
    alcohol = models.CharField(max_length=15, choices=ALCOHOL_CHOICES)
    education = models.CharField(max_length=25, choices=EDUCATION_CHOICES)
    working_status = models.CharField(max_length=25, choices=WORKING_STATUS_CHOICES, null=True)
    exercise = models.CharField(max_length=25, choices=EXERCISE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    diabetes_mellitus = models.CharField(max_length=15, choices=DIABETES_CHOICES, null=True)
    asthma = models.CharField(max_length=15, choices=ASTHMA_CHOICES, null=True)
    hypertension = models.CharField(max_length=15, choices=HYPERTENSION_CHOICES, null=True)
    probability_model1 = models.JSONField(blank=True, null=True)
    probability_model2 = models.JSONField(blank=True, null=True)
    probability_model3 = models.JSONField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    additional_data_required = models.BooleanField(default=False)
    additional_model_used = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            model_path = self.get_model_path(1)
            features = self.get_features()
            probabilities = self.calculate_probabilities(model_path, features)
            self.probability_model1 = probabilities
            self.set_message_and_additional_requirements(probabilities[1], 1)
        super().save(*args, **kwargs)

    def calculate_probabilities(self, model_path, features):
        model = joblib.load(model_path)
        probabilities = model.predict_proba([features])[0].tolist()
        return probabilities

    def set_message_and_additional_requirements(self, probability, model_number):
        thresholds = {
            'female': {'model1': (0.65, 0.2), 'model2': (0.70, 0.25)},
            'male': {'model1': (0.67, 0.22), 'model2': (0.72, 0.27)}
        }

        gender_key = 'female' if self.gender == '0' else 'male'
        model_key = f'model{model_number}'

        self.additional_data_required = False

        if model_number == 3:
            if probability > 0.5:
                self.message = f"You have a probability of {probability:.2f}, indicating that you have sarcopenia."
            else:
                self.message = f"You have a probability of {probability:.2f}, indicating that you do not have sarcopenia."
        else:
            high_threshold, low_threshold = thresholds[gender_key][model_key]
            if probability > high_threshold:
                self.message = f"You have a probability of {probability:.2f}, indicating that you have sarcopenia."
            elif probability < low_threshold:
                self.message = f"You have a probability of {probability:.2f}, indicating that you do not have sarcopenia."
            else:
                self.message = "Further data required for a conclusive diagnosis."
                self.additional_data_required = True
                self.additional_model_used = f'model{model_number + 1}'


    def get_model_path(self, model_number):
        return f'ml_model/model{model_number}_{"female" if self.gender == "0" else "male"}.joblib'

    def get_features(self):
        return [
            self.age, self.weight, self.height, self.hip, self.smoking,
            self.smoking_packet_per_year, self.alcohol, self.education,
            self.working_status, self.exercise, self.diabetes_mellitus, self.asthma,
            self.hypertension
        ]

class ModelTwo(models.Model):
    data = models.OneToOneField(Data, on_delete=models.CASCADE, related_name='model_two_data')
    low_contraction_stress = models.CharField(max_length=15, choices=LOW_CONTRACTION_STRESS_CHOICES, null=True)
    contraction_stress = models.FloatField()
    gait_speed = models.FloatField()

    def save(self, *args, **kwargs):
        if not self.pk:
            model_path = self.data.get_model_path(2)
            features = self.data.get_features() + self.get_additional_features()
            probabilities = self.data.calculate_probabilities(model_path, features)
            self.data.probability_model2 = probabilities
            self.data.set_message_and_additional_requirements(probabilities[1], 2)
            self.data.save()
        super().save(*args, **kwargs)

    def get_additional_features(self):
        return [self.low_contraction_stress, self.contraction_stress, self.gait_speed]

class ModelThree(models.Model):
    model_two = models.OneToOneField(ModelTwo, on_delete=models.CASCADE, related_name='model_three_data')
    low_grip_strength = models.CharField(max_length=15, choices=LOW_GRIP_STRENGTH_CHOICES, null=True)
    grip_strength = models.FloatField()

    def save(self, *args, **kwargs):
        if not self.pk:
            model_path = self.model_two.data.get_model_path(3)
            features = self.model_two.data.get_features() + self.model_two.get_additional_features() + self.get_additional_features()
            probabilities = self.model_two.data.calculate_probabilities(model_path, features)
            self.model_two.data.probability_model3 = probabilities
            self.model_two.data.set_message_and_additional_requirements(probabilities[1], 3)
            self.model_two.data.save()
        super().save(*args, **kwargs)

    def get_additional_features(self):
        return [self.low_grip_strength, self.grip_strength]

