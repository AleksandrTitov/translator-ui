import pygal


class Visual(object):
    def __init__(self, dict_words, file_name="visual"):
        self.dict_words = dict_words
        self.file_name = file_name

    def mkPie(self):
        visual = pygal.Pie(
            show_legend=False,
            title=u'The visual view of the translated words'
        )
        visual.title = 'The visual view of the translated words'

        for word in self.dict_words:
            count = word[1][0]
            visual.add(word[0], count)

        return visual.render_data_uri()
