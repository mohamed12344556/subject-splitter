import pandas as pd
import re

# قائمة القيم التي تريد البحث عنها ووضعها في الأعمدة المناسبة
values_list = [
    "لغة عربيه",
    "لغة انجليزية",
    "لغة تانيه",
    "تاريخ",
    "جغرافيا",
    "فلسفة ومنطق",
    "علم نفس واجتماع",
    "فيزياء",
    "كيمياء",
    "جيولوجيا",
    "احياء",
    "رياضيات باحتة",
    "رياضيات تطبيقيه",
]

# اسم الملف الذي تريد معالجته
file_name = "recommendation_data.xlsx"

# اسم العمود الذي تريد فصله
column_to_split = "مواد.الضعف."

# اسماء الاعمدة التي ستنشأ
new_columns = ["مادة_ضعف_{}".format(value) for value in values_list]

# قراءة الملف
df = pd.read_excel(file_name)

# إنشاء أعمدة جديدة مبنية على قائمة القيم
for value, new_column in zip(values_list, new_columns):
    # استخدام regex لفصل القيم بشكل صحيح
    pattern = r"\b{}\b".format(re.escape(value))
    df[new_column] = df[column_to_split].apply(
        lambda x: value if re.search(pattern, str(x)) else ""
    )

# حفظ البيانات المعدلة إلى ملف جديد إذا أردت
df.to_excel("edited_data.xlsx", index=False)
print("Done(;")

# عرض النتيجة
# print(df)
