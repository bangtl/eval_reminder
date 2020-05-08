from odoo import api, fields, models, _
import datetime


class EvalReminder(models.Model):
    _inherit = "hr.employee"

    x_applied_date = fields.Date(string="Applied Date", readonly=True)
    x_trial_end_date = fields.Date(string="Trial End Date")
    x_employee_code = fields.Char(string="Employee Code", required=True)
    x_level1_eval = fields.Many2one("hr.employee", string="Level 1 Evaluation",)
    x_level1_eval_count = fields.Integer(string="Level 1 Mail Count", default=0)
    x_level1_eval_status = fields.Boolean(string="Level 1 Evaluation Status")
    x_level2_eval = fields.Many2one("hr.employee", string="Level 2 Evaluation",)
    x_level2_eval_count = fields.Integer(string="Level 2 Mail Count", default=0)
    x_level2_eval_status = fields.Boolean(string="Level 2 Evaluation Status")
    x_level3_eval = fields.Many2one("hr.employee", string="Level 3 Evaluation",)
    # x_level3_eval_count = fields.Integer(string="Level 3 Mail Count")
    x_level3_eval_status = fields.Boolean(string="Level 3 Evaluation Status")
    x_self_eval = fields.Many2one("hr.employee", string="Self Evaluation")
    x_self_eval_status = fields.Boolean(string="Self Evaluation Status")

    def _run_job(self):
        # print("Scheduler is called.")
        for rec in self.env["hr.employee"].search([]):
            if rec.x_trial_end_date:
                # print("emp: ", rec.name)
                rdate = rec.x_trial_end_date - datetime.timedelta(days=10)
                # print(rdate)
                if datetime.date.today() >= rdate:
                    # print("founded", rec.name)
                    # print(rec.company_id.name)
                    # print(rec.company_id.email)
                    if not rec.x_self_eval_status:
                        template_id = self.env["ir.model.data"].get_object_reference(
                            "eval_reminder", "eval_reminder_email_template_level0"
                        )[1]
                        if template_id:
                            email_template_obj = self.env["mail.template"].browse(
                                template_id
                            )
                            values = email_template_obj.generate_email(
                                rec.id, fields=None
                            )
                            msg_id = self.env["mail.mail"].create(values)
                            if msg_id:
                                msg_id._send()

                    elif not rec.x_level1_eval_status:
                        template_id = self.env["ir.model.data"].get_object_reference(
                            "eval_reminder", "eval_reminder_email_template_level1"
                        )[1]
                        if template_id:
                            email_template_obj = self.env["mail.template"].browse(
                                template_id
                            )
                            values = email_template_obj.generate_email(
                                rec.id, fields=None
                            )
                            msg_id = self.env["mail.mail"].create(values)
                            if msg_id:
                                msg_id._send()
                                rec.x_level1_eval_count += 1

                    elif not rec.x_level2_eval_status:
                        template_id = self.env["ir.model.data"].get_object_reference(
                            "eval_reminder", "eval_reminder_email_template_level2"
                        )[1]
                        if template_id:
                            email_template_obj = self.env["mail.template"].browse(
                                template_id
                            )
                            values = email_template_obj.generate_email(
                                rec.id, fields=None
                            )
                            msg_id = self.env["mail.mail"].create(values)
                            if msg_id:
                                msg_id._send()
                                rec.x_level2_eval_count += 1

        return True
