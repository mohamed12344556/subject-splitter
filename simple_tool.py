import os
import json
import pandas as pd

# قراءة جميع أوراق العمل من ملف Excel
excel_file = "schedule.xlsx"
sheets = pd.read_excel(excel_file, sheet_name=None)

# إنشاء مجلد للملفات المحولة
output_folder = "transformed_data"
os.makedirs(output_folder, exist_ok=True)

# تحويل كل ورقة عمل إلى ملف Excel و JSON و SQL منفصل
for sheet_name, df in sheets.items():
    # طلب إدخال قيمة `plans_number`
    plans_number = int(input(f"Enter plan number for '{sheet_name}': "))

    transformed_data = []
    for i, row in df.iterrows():
        day = row["اليوم/الوقت"]
        times_subjects = list(row.items())[1:]  # تجاوز عمود 'اليوم/الوقت'

        transformed_row = {
            "plans_id": i + 1,
            "plans_number": plans_number,
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

    # تحويل البيانات المحولة إلى DataFrame
    transformed_df = pd.DataFrame(transformed_data)

    # اسم مجلدات الإكسل وال JSON وال SQL المُحفظة لهذه الورقة
    excel_output_folder = os.path.join(output_folder, "excel_files")
    json_output_folder = os.path.join(output_folder, "json_files")
    sql_output_folder = os.path.join(output_folder, "sql_files")
    os.makedirs(excel_output_folder, exist_ok=True)
    os.makedirs(json_output_folder, exist_ok=True)
    os.makedirs(sql_output_folder, exist_ok=True)

    # اسم ملفات الإكسل وال JSON وال SQL المُحفظة لهذه الورقة
    new_excel_file = os.path.join(excel_output_folder, f"{sheet_name}_transformed.xlsx")
    new_json_file = os.path.join(json_output_folder, f"{sheet_name}_transformed.json")
    new_sql_file = os.path.join(sql_output_folder, f"{sheet_name}_transformed.sql")

    # حفظ البيانات الجديدة في ملف Excel جديد
    transformed_df.to_excel(new_excel_file, index=False)

    # حفظ البيانات الجديدة في ملف JSON جديد مع تجنب الترميز Unicode
    with open(new_json_file, "w", encoding="utf-8") as json_file:
        json.dump(transformed_data, json_file, ensure_ascii=False)

    # إنشاء بيانات SQL INSERT
    sql_inserts = []
    for row in transformed_data:
        # تحديد قيمة `plans_id` إلى NULL
        row_values = [
            value if key != "plans_id" else "NULL" for key, value in row.items()
        ]
        sql_values = ", ".join(
            [f"'{value}'" if value != "NULL" else value for value in row_values]
        )
        sql_inserts.append(f"INSERT INTO `plans` VALUES ({sql_values});\n")

    # حفظ البيانات الجديدة في ملف SQL
    with open(new_sql_file, "w", encoding="utf-8") as sql_file:
        sql_file.writelines(sql_inserts)

    # طباعة رسالة التأكيد
    print(f"Data saved to {new_excel_file}, {new_json_file}, and {new_sql_file}")
