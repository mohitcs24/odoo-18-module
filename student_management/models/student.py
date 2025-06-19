from odoo import models, fields, api

class StudentStudent(models.Model):
    _name = 'student.management'
    _description = 'Student Management'
    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string ='Active')
    roll_number = fields.Char(string='Roll Number')
    #student_id = fields.Many2one('student.management', string="Student") 
    age = fields.Integer(string='Age')
    standard = fields.Selection([
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
        ('9', '9th'),
        ('10', '10th'),
        ('11', '11th'),
        ('12', '12th'),
    ], string='Standard')
    address = fields.Text(string='Address')

    place = fields.Char(string="Place")
    class_field = fields.Char(string="Class")  
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")
    guardian_name = fields.Char(string="Guardian Name")
    contact_number = fields.Char(string="Contact Number")
    email = fields.Char(string="Email")
    admission_date = fields.Date(string="Admission Date")
    student_id = fields.Char(string="Student ID")
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('alumni', 'Alumni')
    ], string="Status", default="active")

    subject_1 = fields.Char(string="Subject 1")
    subject_2 = fields.Char(string="Subject 2")
    subject_3 = fields.Char(string="Subject 3") 
    subject_4 = fields.Char(string="Subject 4") 
    sale_order_id  = fields.Many2one('sale.order',string='sale order')
    student_level = fields.Char(string="Student Level", compute="_compute_student_level", store=True, readonly=True)
    blood_group = fields.Char(string="Blood Group")
    disability = fields.Char(string="Disability")
    medical_condition = fields.Text(string="Medical Condition")
    allergies = fields.Text(string="Allergies")
    emergency_contact = fields.Char(string="Emergency Contact")
    doctor_name = fields.Char(string="Doctor Name")

    aadhar_card = fields.Binary(string="Aadhar Card")
    birth_certificate = fields.Binary(string="Birth Certificate")
    tc_copy = fields.Binary(string="Transfer Certificate Copy")
    report_card = fields.Binary(string="Report Card")
    other_documents = fields.Binary(string="Other Documents")

    note_1 = fields.Text(string="Note 1")
    note_2 = fields.Text(string="Note 2")
    note_3 = fields.Text(string="Note 3")
    note_4 = fields.Text(string="Note 4")

    def action_submit(self):
        for rec in self:
            rec.status = 'active'
        return True

    def action_reset(self):
        for rec in self:
            rec.name = ''
            rec.roll_number = ''
            rec.age = 0
            rec.standard = False
            rec.place = ''
            rec.class_field = ''
            rec.dob = False
            rec.gender = False
            rec.guardian_name = ''
            rec.contact_number = ''
            rec.email = ''
            rec.address = ''
            rec.admission_date = False
            rec.student_id = ''
            rec.status = 'inactive'
            rec.subject_1 = ''
            rec.subject_2 = ''
            rec.subject_3 = ''
            rec.subject_4 = ''
            rec.blood_group = ''
            rec.disability = ''
            rec.medical_condition = ''
            rec.allergies = ''
            rec.emergency_contact = ''
            rec.doctor_name = ''
            rec.aadhar_card = False
            rec.birth_certificate = False
            rec.tc_copy = False
            rec.report_card = False
            rec.other_documents = False
            rec.note_1 = ''
            rec.note_2 = ''
            rec.note_3 = ''
            rec.note_4 = ''
        return True

    def print_student_report(self):
        self.ensure_one()
        return self.env.ref('student_management.action_student_report_pdf').report_action(self.id)
    
    @api.onchange('active')
    def onchange_active(self):
        if self.active == True:
            self.name = 'name' + '1'
        else:
            self.name = "game"
            
    @api.onchange('sale_order_id')
    def onchange_sale_order(self):
        if self.sale_order_id and self.sale_order_id.partner_id:
            self.name = self.sale_order_id.partner_id.name
        else:
            self.name = ''
    
    @api.depends('age')
    def _compute_student_level(self):
        for rec in self:
            if rec.age:
                if rec.age < 18:
                    rec.student_level = 'Junior'
                else:
                    rec.student_level = 'Senior'
            else:
                rec.student_level = 'Unknown'


    def custom_method(self):
        for record in self:
            if record.sale_order_id:
                fields_demo_obj = self.env['all.fields.demo']
                field_dict = {'name':record.sale_order_id}
                fields_demo_obj.create(field_dict)

    # demo_ids = fields.One2many('all.fields.demo', 'student_id', string="Demo Records")
