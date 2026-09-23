class calculator:
    def calculator(self,a,b,operation):
        if operation=="add":
            return a+b
        elif operation=="subtract":
            return a-b
        elif operation=="multiply":
            return a*b
        elif operation=="divide":
            if b==0:
                raise valueError("division by zer0!")
                return a/b
            else:
                raise valueError("Invalid operation")
                if _name_=="_main_":
                    calc=calculator()
                    print("10+5=",calc.calculate(10,5,"add"))
                    print("10-5=",calc.calculate(10,5,"subtract"))
                    print("10*5=",calc.calculate(10,5,"multiply"))
                    print("10/5=",calc.calculate(10,5,"divide"))