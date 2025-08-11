from tkinter import *
import numpy as np
import pandas as pd
# from gui_stuff import *

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

disease_description = {
    'Fungal infection': 'A skin infection caused by fungus, leading to itching, redness, and flaking.',
    'Allergy': 'An immune system reaction to foreign substances like pollen, food, or animal dander.',
    'GERD': 'Gastroesophageal Reflux Disease; a digestive disorder where stomach acid irritates the food pipe lining.',
    'Chronic cholestasis': 'A liver condition where bile cannot flow from the liver to the duodenum.',
    'Drug Reaction': 'Adverse effects caused by medication intake.',
    'Peptic ulcer diseae': 'Sores on the lining of the stomach or small intestine causing abdominal pain.',
    'AIDS': 'Acquired Immunodeficiency Syndrome; caused by HIV and severely weakens the immune system.',
    'Diabetes': 'A metabolic disorder characterized by high levels of blood sugar over a prolonged period.',
    'Gastroenteritis': 'An intestinal infection marked by diarrhea, cramps, nausea, and vomiting.',
    'Bronchial Asthma': 'A condition where airways become inflamed, narrow, and swell, producing extra mucus.',
    'Hypertension': 'High blood pressure condition that can lead to serious heart problems.',
    'Migraine': 'A neurological condition causing intense headaches often with nausea and sensitivity to light.',
    'Cervical spondylosis': 'Age-related wear affecting spinal disks in the neck.',
    'Paralysis (brain hemorrhage)': 'Loss of muscle function due to bleeding in the brain.',
    'Jaundice': 'Yellowing of the skin and eyes due to liver dysfunction.',
    'Malaria': 'A mosquito-borne infectious disease affecting red blood cells and liver.',
    'Chicken pox': 'A viral infection causing itchy skin rash with red spots and blisters.',
    'Dengue': 'A mosquito-borne viral disease causing fever, rash, and muscle pain.',
    'Typhoid': 'A bacterial infection from contaminated food or water, causing high fever and weakness.',
    'hepatitis A': 'A viral liver disease transmitted through ingestion of contaminated food and water.',
    'Hepatitis B': 'A liver infection caused by the hepatitis B virus (HBV), spread through body fluids.',
    'Hepatitis C': 'A liver disease caused by the hepatitis C virus, usually spread by blood contact.',
    'Hepatitis D': 'A liver infection that only occurs in people infected with hepatitis B.',
    'Hepatitis E': 'A liver disease caused by hepatitis E virus, mainly spread through contaminated water.',
    'Alcoholic hepatitis': 'Inflammation of the liver caused by excessive alcohol consumption.',
    'Tuberculosis': 'A contagious bacterial infection that mainly affects the lungs.',
    'Common Cold': 'A viral infection of the nose and throat, causing congestion, runny nose, and sneezing.',
    'Pneumonia': 'An infection that inflames the air sacs in one or both lungs.',
    'Dimorphic hemmorhoids(piles)': 'Swollen veins in the rectum or anus causing discomfort and bleeding.',
    'Heart attack': 'A condition where blood flow to the heart is blocked, causing tissue damage.',
    'Varicose veins': 'Swollen, twisted veins visible under the skin, usually in the legs.',
    'Hypothyroidism': 'A condition where the thyroid gland doesn’t produce enough thyroid hormone.',
    'Hyperthyroidism': 'A condition where the thyroid gland produces too much hormone.',
    'Hypoglycemia': 'A condition of abnormally low blood sugar (glucose) levels.',
    'Osteoarthristis': 'A type of arthritis that occurs when flexible tissue at the ends of bones wears down.',
    'Arthritis': 'Inflammation of the joints causing pain and stiffness.',
    '(vertigo) Paroymsal  Positional Vertigo': 'A condition causing dizziness when the head is moved in certain positions.',
    'Acne': 'A skin condition that occurs when hair follicles become plugged with oil and dead skin cells.',
    'Urinary tract infection': 'An infection in any part of the urinary system, usually the bladder or urethra.',
    'Psoriasis': 'A skin disease that causes red, itchy scaly patches, commonly on the knees, elbows, and scalp.',
    'Impetigo': 'A contagious bacterial skin infection forming pustules and yellow crusty sores.'
}


l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv(r"C:\Users\Admin\Desktop\disease prediction\Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

# print(df.head())

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv(r"C:\Users\Admin\Desktop\disease prediction\Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# ------------------------------------------------------------------------------------------------------


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X, np.ravel(y))

    from sklearn.metrics import accuracy_score
    y_pred = clf4.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Correct predictions:", accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get(), Symptom6.get()]

    # Reset l2 each time
    global l2
    l2 = [0] * len(l1)

    for k in range(0, len(l1)):
        for z in psymptoms:
            if z == l1[k]:
                l2[k] = 1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if predicted == a:
            h = 'yes'
            break

    t2.delete("1.0", END)
    t3.delete("1.0", END)

    if h == 'yes':
        predicted_disease = disease[a].strip()
        description = disease_description.get(predicted_disease, "Description not available.")
        t2.insert(END, predicted_disease)
        t3.insert(END, description)
    else:
        t2.insert(END, "Not Found")
        t3.insert(END, "")


# gui_stuff------------------------------------------------------------------------------------

root = Tk()
root.geometry("1444x1080")  # set window size to fit image
bg_img = PhotoImage(file=r"C:\Users\Admin\Desktop\PDFD\disease prediction\detect2.png") # your background image
bg_label = Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# entry variables
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)
Symptom6 = StringVar()
Symptom6.set(None)
Name = StringVar()

# Heading
w2 = Label(root, justify=CENTER, text="Human Disease Predictor using Machine Learning", fg="red",bg="pink")
w2.config(font=("times new roman", 30))
w2.grid(row=1, column=0, columnspan=2, padx=10)
w2 = Label(root, justify=RIGHT, text="A Project by AMIT Y K", fg="yellow",bg="red")
w2.config(font=("Aharoni", 24))
w2.grid(row=2, column=0, columnspan=2, padx=100)

# labels
NameLb = Label(root, text="Name of the Patient", fg="yellow", bg="black")
NameLb.grid(row=6, column=0, pady=20, sticky=W)


S1Lb = Label(root, text="Symptom 1", fg="yellow", bg="black")
S1Lb.grid(row=7, column=0, pady=20, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="yellow", bg="black")
S2Lb.grid(row=8, column=0, pady=20, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="yellow", bg="black")
S3Lb.grid(row=9, column=0, pady=20, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="yellow", bg="black")
S4Lb.grid(row=10, column=0, pady=20, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="yellow", bg="black")
S5Lb.grid(row=11, column=0, pady=20, sticky=W)

S6Lb = Label(root, text="Symptom 6", fg="yellow", bg="black")
S6Lb.grid(row=12, column=0, pady=20, sticky=W)


destreeLb = Label(root, text="RandomForest", fg="white", bg="blue")
destreeLb.grid(row=17, column=0, pady=40, sticky=W)


# entries
OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=1)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=1)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=9, column=1)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=10, column=1)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=11, column=1)

S6En = OptionMenu(root, Symptom6,*OPTIONS)
S6En.grid(row=12, column=1)
 

rnf = Button(root, text="Randomforest", command=randomforest,bg="green",fg="yellow")
rnf.grid(row=9, column=3,padx=10)


#textfileds
 
t2 = Text(root, height=1, width=40,bg="orange",fg="black")
t2.grid(row=17, column=1 , padx=10)
t3 = Text(root, height=5, width=60, bg="lightyellow", fg="black")
t3.grid(row=18, column=1, padx=10)



root.mainloop()
