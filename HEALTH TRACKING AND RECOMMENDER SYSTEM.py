from tkinter import *
from PIL import ImageTk, Image

tk = Tk()
tk.title('HEALTH TRACKING AND RECOMMENDER SYSTEM')
tk.config(bg='#37C6FF')

Nameval = StringVar()
gender_var = StringVar()
Ageval = IntVar()
Heightval = IntVar()
Weightval = IntVar()
BP_level_val = IntVar()
HEART_BEAT = IntVar()


def submitdetails():
    print('DETAILS ARE:')
    print('NAME :', Nameval.get())
    print('GENDER :', gender_var.get())
    print('AGE :', Ageval.get())
    print('Height :', Heightval.get())
    print('Weight :', Weightval.get())
    print('BP level is :', BP_level_val.get())
    print('HEART BEAT is :', HEART_BEAT.get())


def BMICALUCLATOR():
    global BMI
    User_Height = Heightval.get() / 100
    User_Weight = Weightval.get()
    BMI = ((User_Weight) / (User_Height ** 2))
    print('The BMI index of User is :', BMI)


def BMIRECOMMENDER():
    if (BMI < 18.5):
        print("Your BMI is very LOW that means you are in UNDERWEIGHT situation")
        print("Make PROPER DIET with :")
        print('->Eating at least 5 portions of a variety of fruit and vegetables every day.')
        print(
            '->Basing meals on potatoes, bread, rice, pasta or other starchy carbohydrates. Choose wholegrain where possible.')
        print(
            '->Choosing unsaturated oils and spreads, such as sunflower or rapeseed, and eating them in small amounts')
        print('->Drinking plenty of fluids. The government recommends 6 to 8 glasses a day.')
        print('->But try not to have drinks just before meals to avoid feeling too full to eat.')
        print("Do EXCERCISES daily...")
    elif (BMI >= 18.5 and BMI <= 24.9):
        print("->Your BMI is VERYGOOD that means you are in HEALTHY situation")
        print("->Do EXCERCISES daily to keep your BMI healthy...")
    elif (BMI >= 25.0 and BMI <= 29.9):
        print("Your BMI is HIGH that means you are in OVERWEIGHT situation")
        print(
            "The best way to achieve this is to swap unhealthy and high-energy food choices – such as fast food, processed food and sugary drinks (including alcohol)")
        print("Make PROPER DIET with :")
        print("->plenty of fruit and vegetables")
        print(
            "->plenty of potatoes, bread, rice, pasta and other starchy foods (ideally you should choose wholegrain varieties)")
        print("->some meat, fish, eggs, beans and other non-dairy sources of protein")
        print("->just small amounts of food and drinks that are high in fat and sugar")
        print("Do EXCERCISES daily which is very important...")
    else:
        print("Your BMI is HIGH that means you are in OBESE situation")
        print("CONSULT A DOCTOR FOR QUICK REACTION..")
        print(
            "The best way to achieve this is to swap unhealthy and high-energy food choices – such as fast food, processed food and sugary drinks (including alcohol)")
        print("Make PROPER DIET with :")
        print("->plenty of fruit and vegetables")
        print(
            "->plenty of potatoes, bread, rice, pasta and other starchy foods (ideally you should choose wholegrain varieties)")
        print("->some meat, fish, eggs, beans and other non-dairy sources of protein")
        print("->just small amounts of food and drinks that are high in fat and sugar")
        print("Do EXCERCISES daily which is very important...")


def BPLEVELCALUCLATOR():
    BP_level = BP_level_val.get()
    if (BP_level <= 90):
        print("Your BP level is NOT good that is LOW BLOOD PRESSURE")
        print("->Low blood pressure is less common.")
        print("->Some medicines can cause low blood pressure as a side effect. ")
        print("->It can also be caused by a number of underlying conditions, including heart failure and dehydration.")
    elif (BP_level >= 90 and BP_level <= 120):
        print("Your BP level is GOOD and HEALTHY")
    else:
        print("Your BP level is NOT good that is HIGH BLOOD PRESSURE")
        print(
            "->High blood pressure is often related to unhealthy lifestyle habits, such as smoking, drinking too much alcohol, being overweight and not exercising enough.")
        print(
            "->Left untreated, high blood pressure can increase your risk of developing a number of serious long-term health conditions, such as coronary heart disease and kidney disease.")


def HEARTBEATLEVELCALUCLATOR():
    global i
    s = Toplevel()
    s.title('HEARTCHECKER')
    i = ImageTk.PhotoImage(Image.open(r"D:\sem 3\int 213\HEALTH-TRACKING-AND-RECOMMENDER-SYSTEM\HEARTRATECHECK.png")
    l = Label(s, image=i).pack()


def HEALTHQUOTE():
    global j
    s1 = Toplevel()
    s1.title('HEALTHY LIFE')
    j = ImageTk.PhotoImage(Image.open(r"D:\sem 3\int 213\HEALTH-TRACKING-AND-RECOMMENDER-SYSTEM\h2.jpg")
    l1 = Label(s1, image=j).pack()


def RECOMMENDER():
    global BMI_INDEX
    global BP_INDEX
    k = Toplevel()
    k.config(bg='#358597')
    k.title("HEALTH RECOMMENDER")

    # this is for TOPLEVEL HEADING
    f1 = Frame(k, width=1350, height=50, bd=8, relief="raise")
    f1.pack(side=TOP)
    lb1_f1 = Label(f1, text=" HEALTH RECOMMENDER SYSTEM", padx=16, pady=16, bd=16, fg='#000000',
                   font=("Bell MT", 48, 'bold'), bg="#FFBFB9", relief='raise', width=28, height=1)
    lb1_f1.pack()

    # this is for Getting DIET as per BMI
    BMI_INDEX = Button(k, text='BMI DIET RECOMMENDER :', command=BMIRECOMMENDER, bg="navajo white").pack(padx=15,
                                                                                                         pady=5,
                                                                                                         anchor=CENTER)
    # this is for results of entered BP levels
    BP_INDEX = Button(k, text='CHECK BP LEVELS :', command=BPLEVELCALUCLATOR, bg="navajo white").pack(padx=15, pady=5,
                                                                                                      anchor=CENTER)


# this is for MAIN HEADING
Tops = Frame(tk, width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)
lbl_T1 = Label(Tops, text="HEALTH TRACKING SYSTEM", padx=16, pady=16, bd=16, fg='#000000',
               font=("Algerian", 48, 'bold'), bg="navajo white", relief='raise', width=28, height=1)
lbl_T1.pack()

# this is for NAME
x = Label(tk, text='Name :', bg="navajo white").pack(padx=15, pady=5)
Name = Entry(tk, textvariable=Nameval, relief='raise').pack(padx=15, pady=5)
Nameval.set('xyz')  # default

# this is for AGE
y = Label(tk, text='age :', bg="navajo white").pack(padx=15, pady=5, anchor=CENTER)
Age = Entry(tk, textvariable=Ageval, relief='raise').pack(padx=15, pady=5, anchor=CENTER)

# this is for HEIGHT
p = Label(tk, text='Enter the Height in CM :', bg="navajo white").pack(padx=15, pady=5, anchor=CENTER)
Height = Entry(tk, textvariable=Heightval, relief='raise').pack(padx=15, pady=5, anchor=CENTER)

# this is for WEIGHT
q = Label(tk, text='Enter Weight in Kg :', bg="navajo white").pack(padx=15, pady=5, anchor=CENTER)
Weight = Entry(tk, textvariable=Weightval, relief='raise').pack(padx=15, pady=5, anchor=CENTER)

# this is for BP
a = Label(tk, text='BP level :', bg="navajo white").pack(padx=15, pady=5, anchor=CENTER)
BP_level = Entry(tk, textvariable=BP_level_val, relief='raise').pack(padx=15, pady=5, anchor=CENTER)

# this is for HEARTBEAT
b = Label(tk, text='PRESENT HEART BEAT :', bg="navajo white").pack(padx=15, pady=5, anchor=CENTER)
HEARTBEAT_level = Entry(tk, textvariable=HEART_BEAT, relief='raise').pack(padx=15, pady=5, anchor=CENTER)

# this is for MALE
Radiobutton(tk, text='Male', variable=gender_var, value='Male', bg="navajo white").pack(padx=15, pady=5, anchor=CENTER)

# this is for FEMALE
Radiobutton(tk, text='Female', variable=gender_var, value='Female', bg="navajo white").pack(padx=15, pady=5,
                                                                                            anchor=CENTER)

gender_var.set('Male')  # default value

# this is for SUBMIT ALL DETAILS
submit = Button(tk, text='SUBMIT', command=submitdetails, bg="navajo white").pack(padx=15, pady=5, anchor=CENTER)

# this is for getting BMI
BMI_INDEX = Button(tk, text='GET BMI :', command=BMICALUCLATOR, bg="navajo white").pack(padx=15, pady=5, anchor=CENTER)

# this is for checking heart beat by TOPLEVEL
HEARTBEAT_INDEX = Button(tk, text='CHECK HEART BEAT LEVELS :', command=HEARTBEATLEVELCALUCLATOR,
                         bg="navajo white").pack(padx=15, pady=5, anchor=CENTER)

# this is also a TOPLEVEL to get DIET and BP
HEALTH_RECOMMENDER = Button(tk, text='HEALTH RECOMMENDER', command=RECOMMENDER, bg="navajo white").pack(padx=15, pady=5,
                                                                                                        anchor=CENTER)

# this is for presenting quote
health = Button(tk, text='CLICK ME :-)', command=HEALTHQUOTE, bg="navajo white").pack(padx=15, pady=5, anchor=CENTER)

mainloop()
