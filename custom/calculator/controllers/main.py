from odoo import http
from odoo.http import request


class Addition(http.Controller):

    @http.route('/calculator_form', typy='http', auth='public', website=True)
    def calculator_form(self, **kw):
        print(':::::)))))')
        return http.request.render('calculator.create_form', {})

    @http.route('/calculator/result', type='http', auth='public', website=True)
    def calculator_result(self, **kw):
        print('-------->>>>>>', kw)
        nums = http.request.env['addition.num'].sudo().create(kw)
        sum_nums = nums.add_num()

        return http.request.render('calculator.result', {
            'nums': nums,
            'sum_nums': sum_nums,
        })
