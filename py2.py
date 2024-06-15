import pandas as pd

# قراءة البيانات من ملف Excel
df = pd.read_excel("schedule.xlsx")

# تحويل الجدول إلى الشكل المطلوب
transformed_data = []
for i, row in df.iterrows():
    day = row["اليوم/الوقت"]
    times_subjects = list(row.items())[1:]  # تجاوز عمود 'اليوم/الوقت'

    transformed_row = {
        "Name": "data",
        "plans_id": i + 1,
        "plans_number": 7,
        "plans_day": day,
        "plans_time_1": times_subjects[0][0],
        "plans_subject_1": times_subjects[0][1],
        "plans_time_2": times_subjects[1][0],
        "plans_subject_2": times_subjects[1][1],
        "plans_time_3": times_subjects[2][0],
        "plans_subject_3": times_subjects[2][1],
        "plans_time_4": times_subjects[3][0],
        "plans_subject_4": times_subjects[3][1],
    }
    transformed_data.append(transformed_row)

# تحويل القائمة إلى DataFrame
transformed_df = pd.DataFrame(transformed_data)

# حفظ البيانات الجديدة
transformed_df.to_excel("temp.xlsx", index=False)

# طباعة البيانات الجديدة
print(transformed_df)
