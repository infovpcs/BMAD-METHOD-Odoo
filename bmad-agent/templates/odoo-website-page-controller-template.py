from odoo import http
from odoo.http import request

class MyWebsitePageController(http.Controller):
    _inherit = 'website.main_object' # Optional: useful for website context

    @http.route('/my_custom_page', type='http', auth='public', website=True, methods=['GET'], sitemap=True)
    def my_custom_page(self, **kw):
        """
        Renders a custom website page.
        
        This method fetches data (if needed) and passes it to the QWeb template
        for rendering. This is a public page accessible to all.
        """
        # Example: Fetch some data to pass to the template
        # records = request.env['my.model'].sudo().search([])
        
        values = {
            'page_title': 'My Custom Website Page',
            'dynamic_content': 'This content is loaded from the controller!',
            # 'records': records,
        }
        return request.render('my_module.my_website_page_template', values)

    # Example of a POST route for form submission
    # @http.route('/my_custom_page/submit', type='http', auth='public', website=True, methods=['POST'], csrf=False)
    # def my_custom_page_submit(self, **post):
    #     # Process form data
    #     name = post.get('name')
    #     email = post.get('email')
    #     # Do something with the data, e.g., create a record
    #     request.env['res.partner'].sudo().create({'name': name, 'email': email})
    #     return request.redirect('/my_custom_page/thank_you')


# views/my_website_page_template.xml
# (This is just a conceptual example, the actual XML would be in an XML file)
# <template id="my_website_page_template" name="My Custom Website Page">
#     <t t-call="website.layout">
#         <div id="wrap" class="oe_structure oe_empty">
#             <section class="s_title pb24 pt24" data-vcss="0001" data-snippet="s_title" data-name="Title">
#                 <div class="container">
#                     <h1 class="s_title_default" t-out="page_title"></h1>
#                 </div>
#             </section>
#             <section class="s_text_block" data-vcss="0001" data-snippet="s_text_block" data-name="Text">
#                 <div class="container">
#                     <p t-out="dynamic_content"></p>
#                 </div>
#             </section>
#             <!-- Example of displaying records -->
#             <!-- <section t-if="records">
#                 <div class="container">
#                     <ul>
#                         <li t-foreach="records" t-as="record">
#                             <span t-field="record.name"/>
#                         </li>
#                     </ul>
#                 </div>
#             </section> -->
#         </div>
#     </t>
# </template> 