from odoo import models, fields


class AdditionNum(models.Model):
    _name = 'addition.num'
    _description = 'Num Record'

    num1 = fields.Integer(string='عدد اول')
    num2 = fields.Integer(string='عدد دوم')

    def add_num(self):
        if self.num1 and self.num2:
            return self.num1 + self.num2
