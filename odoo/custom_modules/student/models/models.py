# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class Student(models.Model):
    _name = 'student.profile'
    _description = 'Student Profile'
    _log_access = True   ## if False it will not update crete and write details in database, if added in new model it will not crate those 4 columns
    # _table = 'Student_Profile'   # using this name odoo will create table

    # To add drag and drop feature in tree view, need to add one sequence, if there is order by set in model level then order by will override 
    # sequence on refresh 
    student_seq = fields.Integer()

    name = fields.Char() 
    student_img = fields.Image("Student Image")
    school_id = fields.Many2one('school.profile', string="School")
    roll_number = fields.Integer()
    bla_bla_num = fields.Char()
    status = fields.Selection([('enrolled','Enrolled'),
                               ('admitted','Admitted'),
                               ('left','Left')])

    # _sql_constraints handle validation on sql level and give message specified if any constraint is failed
    _sql_constraints = [
        ('name_unique','unique(name)','Name should be unique'),
        ('school_id_check','check(roll_number>10)','Roll Number should be greater then 10')
    ]

    def wiz_open(self):
        
        return self.env['ir.actions.act_window']._for_xml_id("student.student_roll_num_update_action")  # current_model_name.wizard_action_id
                        ######## or
        # return {'type':'ir.actions.act_window',
        #         'res_model' : 'student.roll.num.update.wizard', #  is a wizard model name
        #         'view_mode':'form',
        #         'target':'new'  # new for pop up and current for wizard to open in current screen
        #         }
    

    @api.model  # function called from the xml
    def add_bla_bla_num(self,id,name):
        for stud in self.search([('bla_bla_num','!=',False)]):
            stud.bla_bla_num = id + name + 'bla_bla' + str(stud.id)

    
    def tree_button_click(self):
        raise UserError("Button clicked")

class TestSqequence(models.Model):
    _name = 'test.sequence'
    _sequence = 'seq'

    name = fields.Char('Name')