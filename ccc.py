from osv import osv
from osv import fields

class TEST(osv.osv):

    _name = 'sale.order'
    _description = 'test.test'
    _columns = {
            'name':fields.text('TERMS OF PAYMENT', size=64, required=False, readonly=False),
            'obd':fields.text('OUR BANK DETAILS', size=64, required=False, readonly=False),
            'ybd':fields.char('YOUR BANK DETAILS', size=64, required=False, readonly=False),
            'items':fields.char('ITEMS', size=64, required=False, readonly=False), 
            'trans':fields.char('TRANSPORTERS', size=64, required=False, readonly=False)
        }
TEST()