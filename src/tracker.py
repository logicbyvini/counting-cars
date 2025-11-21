import math

class Tracker:
    def __init__(self, max_dist=50):
        """
        max_dist: Distância máxima (em pixels) para considerar que é o mesmo objeto.
        """
        self.center_points = {}  # Armazena {id: (cx, cy)}
        self.id_count = 0
        self.max_dist = max_dist

    def update(self, detections):
        """
        detections: lista de [x1, y1, x2, y2]
        Retorna: lista de [id, (cx, cy, bbox)]
        """
        objects_bbs_ids = []

        # 1. Calcular centróides das novas detecções
        current_center_points = []
        for rect in detections:
            x1, y1, x2, y2 = rect
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)
            current_center_points.append((cx, cy, rect))

        # 2. Se for o primeiro frame, registrar todos
        if self.id_count == 0:
            for cx, cy, rect in current_center_points:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([self.id_count, (cx, cy, rect)])
                self.id_count += 1
            return objects_bbs_ids

        # 3. Tentar associar centróides novos com antigos (pela menor distância)
        new_center_points = {}
        
        for cx, cy, rect in current_center_points:
            object_exists = False
            
            for object_id, old_center in self.center_points.items():
                old_cx, old_cy = old_center
                
                # Cálculo da Distância Euclidiana
                dist = math.hypot(cx - old_cx, cy - old_cy)

                if dist < self.max_dist:
                    self.center_points[object_id] = (cx, cy)
                    objects_bbs_ids.append([object_id, (cx, cy, rect)])
                    new_center_points[object_id] = (cx, cy)
                    object_exists = True
                    break
            
            # Se não encontrou ninguém perto, é um carro novo
            if not object_exists:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([self.id_count, (cx, cy, rect)])
                new_center_points[self.id_count] = (cx, cy)
                self.id_count += 1

        # Limpa IDs que não existem mais para economizar memória
        self.center_points = new_center_points.copy()

        return objects_bbs_ids
