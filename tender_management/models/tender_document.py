

from odoo import models, fields

class TenderDocument(models.Model):
    _name = 'tender.document'
    _description = 'Tender Document'

    name = fields.Char(string="Name", required=True)
    tender_id = fields.Many2one('tender.project', string="Tender Project")
    type_id = fields.Many2one('document.type', string="Document Type", domain=[('is_required', '=', True)])
