from sklearn.linear_model import LinearRegression


X = [
    [2, 8, 3],  
    [4, 7, 2],
    [5, 6, 2],
    [6, 6, 1],
    [8, 5, 1],
    [9, 5, 2],
    [10, 4, 1]
]


y = [50, 60, 65, 70, 80, 85, 90]


model = LinearRegression()
model.fit(X, y)

print("📘 Student Marks Predictor Ready!\n")

while True:
    study = input("⏳ Enter study hours (or 'q' to quit): ")
    if study.lower() == 'q':
        print("\n👋 Thanks for using Student Marks Predictor!")
        break

    sleep = input("😴 Enter sleep hours: ")
    breaks = input("☕ Enter number of breaks: ")

    try:
        study = float(study)
        sleep = float(sleep)
        breaks = int(breaks)

        pred = model.predict([[study, sleep, breaks]])
        print(f"📊 Predicted Marks: {pred[0]:.2f}\n")

    except ValueError:
        print("⚠️ Please enter valid numbers!\n")
