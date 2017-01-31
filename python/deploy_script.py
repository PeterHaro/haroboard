from expand import Expander
from css_generator import CSSGenerator

if __name__ == "__main__":
    CSSGenerator = CSSGenerator()
    CSSGenerator.run()
    Expander = Expander("../public/templates/configuration.json")
    Expander.walk_and_parse()
