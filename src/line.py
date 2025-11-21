import cv2

class LineRegion:
    def __init__(self, p1, p2):
        """
        p1: (x, y) ponto inicial da linha
        p2: (x, y) ponto final da linha
        """
        self.p1 = p1
        self.p2 = p2

    def draw(self, frame):
        """
        Desenha a linha no frame.
        """
        cv2.line(frame, self.p1, self.p2, (0, 0, 255), 3)
        return frame
