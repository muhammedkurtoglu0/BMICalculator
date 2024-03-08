import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=400, height=300)

label = tkinter.Label(text="Weight (kg)")
label.config(pady=20)
label2 = tkinter.Label(text="Height (m)")
label2.config(pady=20)

entry = tkinter.Entry()
entry.place(x=135,y=50)

entry2 = tkinter.Entry()
entry2.place(x=135,y=100)

entry.focus()


def calcute_bmi():
    weight = float(entry.get())
    height = float(entry2.get())
    bmi = weight / height ** 2

    if bmi < 18.5:
        print(f"Your BMI is {bmi}. Underweight")
    elif bmi >= 18.5 and bmi < 24.9:
        print(f"Your BMI is {bmi}. Normal")
    elif bmi >= 25.0 and bmi < 30.0:
        print(f"Your BMI is {bmi}. Overweight")
    elif bmi >= 30.0:
        print(f"Your BMI is {bmi}. Obese")


button = tkinter.Button(text="Calcute", command=calcute_bmi)
button.place(x=175, y=130)

label.pack()
label2.pack()
tkinter.mainloop()