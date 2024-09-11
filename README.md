New Task For Odoo version 15 !
This Task contains Many Of Simple Codes And Some Useful Customization For practice
I Hope It Will Be Useful For Beginner odoo Developers !
 
The Task :
Create new Module from scratch called Exam_Your_Name that has Two Objects: **Object called 'exam' (filtered by Name and exam_type):
1- Name: Char, Required Dropdownlist from hr.employee.
2- exam_type: Relation object 'exam_type' can choose more than one record.
3- exam_num: get serial of exam_type that user choosed.
4- exam_length: Integer, readonly >> Compute field that get name length.
5- start_date: DateTime, Required,default value today
6- end_date: Datetime, Required
7- marks :Float,Readonly

* Views: Tree, Form
* Prevent user to create or update if start_date > end_date.
* Make workflow with Three States ('created', 'solved', 'finished')
- in the case of created make a button named solve that takes you to the state solved.
- in the case of solved make 2 buttons named back to created that return to the state created when you clicking it  and finish that takes you to the state finished.

- in the case of finished make 2 buttons named back to solved that return to the state solved when you clicking it.
  **Object exam_type(Group by serial):
1- Name: Char, Required.
2- serial: Integer
* Views: Tree, form
* workflow: Two state ('draft', 'finished')

=== the above two views should contain demo data with minimum 3 records.

* In the HR Module under Employees Menue create new menuitem called student evaluation  with new form,tree views and it should contains:
1- Name: Char, Required Dropdownlist from hr.employee.
2- student grade: Integer
3- final grade:Integer
4- student percentage:Integer,readonly with progressbar "this field should compute students percentages according to their grades"
5- evaluation :Selection :readonly has 5 options (Excellent,Vgood,Good,Fair,Poor) 
when the student percentage smaller than 50% the evaluation must be Poor.
when the student percentage from 50% to 65%  the evaluation must be Fair.
when the student percentage from 65% to 75%  the evaluation must be Good.
when the student percentage from 75% to 85%  the evaluation must be Vgood.
when the student percentage greater than or equal 85% the evaluation must be Excellent.

**Purchase Module (Vendor Bills form view):
 1- Create new field dropdownlist that get all products (domain can be sold only) and add it After Vendor field.
 2- Create New Menu called my product that get products view(products.template) with only form and tree view.
 Inheritance:
* Project Module
Create new field called exam (Char) under 'assigned to' field inside Task Menu.
*create new page called "others" in the task view after "Extra Info" page and add two field to it named partner Dropdownlist from res.partner and selection field called gender with two options (male,female).
*in the inventory module go to menu operation>>transfer form view in its notebook in the page "Operations" add new field after product called barcode readonly that takes its value from barcode in the product.template when user choose product its barcode should appear automatic in your new field.


Security:
Add Two Groups:
1- Manager: Full access in object ('exam', 'exam_type ')
2- Employee: Read and write in object ('exam', 'exam_type ')
3- general:  Read in object ('exam', 'exam_type ')


reports:
**create new report from scrath for exam object that prints all its data fields.
**add in its hedaer (My new report with h1 headings) and description paragraph.
**add in its footer two signatures with Manager sig:     and   Employee sig:

** in the Sale module go to menu orders>>quotations (sale.order) add two fields integer (called qunt and deg)  after customer and add them in the qutation / order report before quantityt
