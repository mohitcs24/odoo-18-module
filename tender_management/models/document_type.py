from odoo import models, fields

class DocumentType(models.Model):
    _name = 'document.type'
    _description = 'Document Type'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    is_required = fields.Boolean(string="Is Required")
    is_supporting = fields.Boolean(string="Is Supporting")
