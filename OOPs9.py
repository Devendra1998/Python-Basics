# ************** Multilevel Inheritqance*****************

class Dad:
    basketball=1


class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I can dance {self.dance} no of times"

class Grandson(Son):

    # Quiz- IF we print harry.basketball. what will be the output? Ans-1


    dance = 6

    def isdance(self):
     return f"Jackson Yeah!"\
        f"Yes i dance very nicely {self.dance} no of times"

darry=Dad()
larry=Son()
harry=Grandson()

print(harry.basketball)


# Exercise
# Electronic Devices
# Pocket Gadget
# Phone