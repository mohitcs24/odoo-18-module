from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    late_line = fields.One2many(
        'employee.late.line', 'employee_id', string='Late Entries'
    )

    pending_hour = fields.Float(
        string="Pending Hour",
        compute='_compute_pending_hour',
        store=True
    )

    @api.depends('late_line.duration')
    def _compute_pending_hour(self):
        for employee in self:
            total_hours = 2.0  # total allowed late time
            used_hours = sum(employee.late_line.mapped('duration'))
            employee.pending_hour = max(total_hours - used_hours, 0.0)


class EmployeeLateLine(models.Model):
    _name = 'employee.late.line'
    _description = 'Late Line Entry'

    employee_id = fields.Many2one('hr.employee', string='Employee', ondelete="cascade")
    date = fields.Date(string='Date')
    status = fields.Selection([
        ('on_time', 'On Time'),
        ('half_day', 'Half Day'),
        ('late', 'Late'),
    ], string='Status', default='on_time')
    duration = fields.Float(string='Late Duration (hours)')
    reason = fields.Char(string="Reason")


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'





