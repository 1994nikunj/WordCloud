__Author__ = 'Nikunj Sharma'

try:
    import json
    import datetime
    import numpy as np
    from PIL import Image
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
except ImportError():
    print('ImportError: Missing Imports')

all_objects = []


class Cloud:
    def __init__(self,
                 input_file: str = None,
                 print_data: bool = True,
                 wc_print: bool = True,
                 wc_to_file: bool = True):
        self._input = input_file
        self._processed_input = None

        # Storing all class objects in a list to be later used for exit operation
        all_objects.append(self)

        self.read_input_file()

        self.generate_word_cloud()

        self.exit()

    # Open input file -> read and return data -> close file
    def read_input_file(self) -> None:
        with open(file=self._input, mode='r', encoding="utf8") as fr:
            raw = fr.read().split('\n')
            self._processed_input = ' '.join(raw)

    # Generating the wordCloud using the processed-input based on some parameters
    def generate_word_cloud(self) -> None:
        _mask = np.array(Image.open("Mask/heart.png"))

        word_cloud = WordCloud(mask=_mask,
                               colormap='plasma_r',
                               repeat=True,
                               background_color='White')

        word_cloud.generate(self._processed_input)

        # Using matplot library to plot the wordcloud
        plt.figure(figsize=(15, 15))
        plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

        file_name = datetime.datetime.today().strftime("%b-%d-%Y_%H-%M-%S") + '.png'
        word_cloud.to_file(filename='WordCloud/' + file_name)

    # Clearing memory from the instance vars, more relevant when data is large in magnitude
    # Even though python's internal garbage collector takes care of this, it's generally a good practice to clear
    # variables on the way or during exit to keep memory clean
    @staticmethod
    def exit():
        for _object in all_objects:
            _object = None

        exit('\nExiting: Happy coding! \nCode By: Nikunj Sharma')


if __name__ == '__main__':
    try:
        Cloud(input_file='input.txt')
    except Exception as e:
        print('Oops! Something went wrong: {}'.format(e))

else:
    pass
