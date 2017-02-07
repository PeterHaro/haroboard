class HTMLGenerator(object):
    def __init__(self, config):
        self.indent_with_tabs = False  # Ident with tabs or spaces
        self.number_of_spaces_per_indent_level = 4  # TODO: REPLACE WITH CONFIG

    def generate_supported_language_domains(self, alternative_languages):
        # Should be inside head, thus only 1 indent level
        retval = []
        for language_code in alternative_languages:
            retval.append(
                "<link rel=\"alternate\"  hreflang=\"" + language_code + "\" href=\"{{__('page_url')}}/" + language_code + "\"/>")
        return retval
