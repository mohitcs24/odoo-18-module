
from odoo import models, fields

class TenderSupportingDocument(models.Model):
    _name = 'tender.supporting.document'
    _description = 'Tender Supporting Document'

    name = fields.Char(string="Name", required=True)
    file = fields.Binary(string="File")
    tender_id = fields.Many2one('tender.project', string="Tender Project")
    type_id = fields.Many2one('document.type', string="Document Type", domain=[('is_supporting', '=', True)])
