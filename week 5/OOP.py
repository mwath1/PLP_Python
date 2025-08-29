#base class
class smartphone:
    def __init__(self,name,model,specs):
        self.name = name
        self.model=model
        self.specs=specs
    
    def present(self):
        print(f"This is {self.model} also a {self.name}")

    def phone_specs(self):
        print(f"{self.model}comes with  the latest {self.specs}")

#inherits from base class
class flagship(smartphone):
    def __init__(self,name,model,specs,S_series):
        super().__init__(name,model,specs)
        self.S_series = S_series

    def phone_specs(self):
        print(f"{self.model} is one of the series latest and best performing flagship phone that boasts a{self.S_series}")

#Also inherits from base class
class budget(smartphone):
    def __init__(self, name, model, specs,A_series):
        super().__init__(name, model, specs)
        self.A_series = A_series

    def phone_specs(self):
         print(f"{self.model} is one of the series latest and best performing budget friendly phone that boasts a{self.A_series}")

#create oject(smartphones)
S_25ulra = flagship("Samsung galaxy","S_25ulra","IP68 dust tight and water resistant","android 15,up to 7 major updates,snapdragon 8 Elte chipset and GPU Adreno 830")
A36 = budget("Samsung galaxyA","A36","IP67 dust/water resistant","android 15,up to 6 major updates,snapdragon 6 Gen 3 chipset and GPU Adreno 710")

#using
print(S_25ulra.present())
print(S_25ulra.phone_specs())

print(A36.present())
print(A36.phone_specs())