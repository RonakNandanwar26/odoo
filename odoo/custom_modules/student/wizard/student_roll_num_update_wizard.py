from odoo import api,models,fields


class StudentRollNumUpdateWizard(models.TransientModel):
    _name = 'student.roll.num.update.wizard'

    roll_num = fields.Integer()


    def update_roll_number(self):
        print("Successfully Update ROll Number")
        
        self.env['student.profile'].browse(self._context.get("active_ids")).update({"roll_number":self.roll_num})
        return True

