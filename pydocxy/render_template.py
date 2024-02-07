from docxtpl import DocxTemplate
import jinja2
from jinja2.exceptions import TemplateError ,TemplateSyntaxError


class RenderTemplate:
    def __init__(self):
        pass

    def render_template(self, doc: DocxTemplate, variables: dict):
        try:
            rendered_document = doc.render(variables)
            return rendered_document
        except TemplateSyntaxError as te:
            print(f"Jinja2 TemplateSyntaxError: {te}")
            return None
        except TemplateError as e:
            print(f"Jinja2 Template Error: {e}")
            return None

            
