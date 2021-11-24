import os
class Path:
    def templateWay(self):
        template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
        template_dir = os.path.join(template_dir, 'View')
        template_dir = os.path.join(template_dir, 'templates')

        return template_dir

    def staticWay(self):
        static_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
        static_dir = os.path.join(static_dir, 'View')
        static_dir = os.path.join(static_dir, 'static')

        return static_dir

s = Path()
print(s.templateWay())