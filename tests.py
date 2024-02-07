from docx import Document
import time
from jinja2 import Template
from docxtpl import DocxTemplate
from pydocxy.render_template import RenderTemplate

start_time = time.time()
document = DocxTemplate("/home/dev/Desktop/Contract/sample.docx")


employee_data = {
    "date":"01/10/1402",
    "start_date":"01/10/1402",
    "end_date":"01/12/1402",
    "company_name":"شرکت پایدار ساز شیمی",
    "company_phone": "(021)44044766",
    "company_address": "تهران، خیابان کاشانی، برج یاران طبقه 8، واحد 801",
    "postal_code": "148-1774323",
    "employee_name": "علی مقیمی ",
    "employee_father_name": "اردشیر",
    "employee_national_code": "00213123456",
    "employee_city":"تهران",
    "employee_address":"تهران، خیابان کاشانی بلوار فردوس خیابان وفاآذر ",
    "employee_postal_code":"148324333",
    "tehran_office":True,
    "employee_is_freelance":False,
    "factory_address":True,
    "allow_employee": True,
    "base_payment":"۵۲۰۰۰۰۰۰",
    "hagh_maskan":"9000000",
    "overtime_ok":False,
}
temp = RenderTemplate()
salam = document.render(employee_data)
#document = temp.render_template(doc=document,variables=employee_data)
#if document:
document.save("/home/dev/Desktop/Contract/Test700020.docx")
end_time = time.time()
runtime = end_time - start_time
print(f"Script runtime: {runtime:.5f} seconds")
