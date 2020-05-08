# -*- coding: utf-8 -*-
{
    "name": "Eval Reminder",
    "version": "13.0.0",
    "summary": """Automatically Send Mail To Responsible User When Employee's Evaluation Date is approaching""",
    "description": """Automatically Send Mail To Responsible User When Employee's Evaluation Date is approaching""",
    "category": "Employees",
    "depends": ["hr"],
    "data": [
        "views/eval_reminder_view.xml",
        "views/eval_reminder_cron.xml",
        "data/eval_reminder_email_template.xml",
    ],
}
