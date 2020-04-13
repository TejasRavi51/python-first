import os

File_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(File_path)
Template_dir = os.path.join(BASE_DIR, "templates")

class Template:
    template_name = "" 
    context = None
    def __init__(self, template_name = "", context = None, *args, **kwargs):
        self.template_name = template_name
        self.context = context

    def get_template(self):
        Template_path = os.path.join(Template_dir, self.template_name)
        if not os.path.exists(Template_path):
            raise Exception("This path doesnot exist")
        template_string = ""
        with open(Template_path, "r") as f:
            template_string = f.read()
        return template_string

    def render(self, context=None):
        render_ctx = context
        if self.context != None:
            render_ctx = self.context
        if not isinstance(render_ctx, dict):
            render_ctx = {}
        template_string = self.get_template()
        return template_string.format(**render_ctx) # {"name": "Tejas"} -> name="Tejas"