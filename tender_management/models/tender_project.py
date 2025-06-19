from odoo import models, fields, api

class TenderProject(models.Model):
    _name = 'tender.project'
    _description = 'Tender Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Enables chatter

    name = fields.Char(
        string='Tender Number', required=True, copy=False, readonly=True,
        index=True, default='New', tracking=True
    )
    partner_id = fields.Many2one('res.partner', string="Contact Name", required=True, tracking=True)

    bid_end_datetime = fields.Datetime(string="Bid End Date/Time", tracking=True)
    bid_opening_date = fields.Datetime(string="Bid Opening Date", tracking=True)
    bid_offer_validity_days = fields.Integer(string="Bid Offer Validity Days", tracking=True)

    ministry_state_name = fields.Char(string="Ministry/State Name", tracking=True)
    department_name = fields.Char(string="Department Name")
    organisation_name = fields.Char(string="Organisation Name")
    office_name = fields.Char(string="Office Name")
    buyer_email = fields.Char(string="Buyer Email")

    item_category = fields.Char(string="Item Category")
    contract_period_months = fields.Integer(string="Contract Period - Months")
    contract_period_days = fields.Integer(string="Contract Period - Days")

    min_avg_annual_turnover = fields.Float(string="Minimum Average Annual Turnover (3 Years)")

    years_past_experience_required = fields.Boolean(
        string="Years of Past Experience Required (Same/Similar Service)"
    )
    past_experience_similar_services = fields.Boolean(string="Past Experience of Similar Services Required")
    mse_exemption_years_experience = fields.Boolean(string="MSE Exemption for Years of Experience")
    startup_exemption_years_experience = fields.Boolean(string="Startup Exemption for Years of Experience")

    document_ids = fields.One2many('tender.document', 'tender_id', string="Documents")
    supporting_document_ids = fields.One2many('tender.supporting.document', 'tender_id', string="Supporting Documents")

    show_uploaded_docs_to_all = fields.Boolean(string="Show Bidder Documents to All Bidders")
    bid_to_ra_enabled = fields.Boolean(string="Bid to RA Enabled")
    bid_type = fields.Char(string="Type of Bid")
    time_allowed_technical_clarifications = fields.Char(string="Time Allowed for Technical Clarifications")

    estimated_bid_value = fields.Float(string="Estimated Bid Value", tracking=True)
    evaluation_method = fields.Char(string="Evaluation Method")
    financial_doc_price_breakup = fields.Boolean(string="Price Breakup in Financial Document Required")
    arbitration_clause = fields.Boolean(string="Arbitration Clause")
    mediation_clause = fields.Boolean(string="Mediation Clause")

    advisory_bank = fields.Char(string="Advisory Bank")
    emd_amount = fields.Float(string="EMD Amount", tracking=True)

    epbg_required = fields.Boolean(string="ePBG Required")
    mii_compliance = fields.Boolean(string="MII Compliance")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_evaluation', 'In Evaluation'),
        ('submitted', 'Submitted'),
        ('lost', 'Lost'),
        ('win', 'Win'),
    ], string="Tender State", default='draft', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('tender.project') or 'New'
        return super(TenderProject, self).create(vals)
