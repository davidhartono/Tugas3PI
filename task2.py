class BMI:
    def __init__(self, weight_kg, height_m):
        self.weight_kg = weight_kg
        self.height_m = height_m

    @property
    def Weight(self):
        return self.weight_kg

    @property
    def Height(self):
        return self.height_m

    def BMI_Value(self):
        return self.weight_kg / (self.height_m ** 2)

    def __eq__(self, other):
        return self.weight_kg == other.weight_kg and self.height_m == other.height_m


# Example usage
person1 = BMI(60, 1.65)
person2 = BMI(70, 1.75)

print("BMI of person1:", person1.BMI_Value())
print("BMI of person2:", person2.BMI_Value())
print("Are person1 and person2 equal?", person1 == person2)
