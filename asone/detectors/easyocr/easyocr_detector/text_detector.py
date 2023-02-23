import easyocr
import numpy as np


class TextDetector:
    def __init__(self, detect_network, use_cuda=True):
        self.use_cuda = use_cuda
        self.detect_network = detect_network

    def detect(self, image: list, languages: list = ['en']) -> list:
        """_summary_
        Args:
            image : Image 
            languages (list, optional): List of languages. Defaults to ['en'].
        Returns:
            list: numpy array of extracted text and img info(heigh, width)
        """

        reader = easyocr.Reader(languages, detect_network=self.detect_network ,gpu=self.use_cuda)
        horizontal_list, free_list = reader.detect(image) 
        formated_output = []
        for bbx in horizontal_list[0]:
            bbx.extend([0, 80])
            formated_output.append(bbx)
        return   np.array(formated_output), free_list