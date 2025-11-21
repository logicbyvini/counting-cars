import cv2

class LineCounter:
    def __init__(self, line):
        self.line = line
        self.total = 0
        self.memory = {}

    def update(self, tracked):
        for track_id, (cx, cy, box) in tracked:
            if track_id not in self.memory:
                self.memory[track_id] = cy

            prev = self.memory[track_id]

            if prev < self.line.p1[1] and cy > self.line.p1[1]:
                self.total += 1

            self.memory[track_id] = cy

    def draw(self, frame):
        cv2.putText(frame, f"Cars: {self.total}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

