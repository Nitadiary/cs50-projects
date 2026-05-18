from datetime import datetime, timedelta

def main():
    print("Drug reminder")
    regimens = []
    while True:
        drug = input("Drug name: ")
        if drug.lower() == "done":
            break
        dose = input("Dosage: ")
        times = input("Frequency: ").strip().split(",")
        days = int(input("Duration of use: "))
        regimens.append(c_regimen(drug, dose, times, days))
    schedule = []
    for r in regimens:
        schedule.extend(g_schedule(r))
    show_next(schedule)

def c_regimen(drug, dose, times, days):
    return {
        "drug" : drug,
        "dose" : dose,
        "times" : times,
        "days" : days
    }

def g_schedule(regimen):
    schedule = []
    today = datetime.today().date()
    for d in range(regimen["days"]):
        day = today + timedelta(days=d)
        for t in regimen["times"]:
            schedule.append({
                "date" : day.isoformat(),
                "time" : t,
                "drug" : regimen["drug"],
                "dose" : regimen["dose"]
                })
    return schedule

def show_next(schedule):
    now = datetime.now()
    schedule.sort(key=lambda x:datetime.strptime(x["date"]+ " " + x["time"], "%Y-%m-%d %H:%M"))
    for item in schedule:
        dt = datetime.strptime(item["date"] + " " + item["time"], "%Y-%m-%d %H:%M")
        if dt >= now:
            print(f"next dose: {item['date']} {item['time']} - {item['drug']} {item['dose']}")
            return
    print("No more dose to consume")

if __name__ == "__main__":
    main()
