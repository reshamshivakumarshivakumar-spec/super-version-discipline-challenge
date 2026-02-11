class Challenge:
    def __init__(self, title, description, points):
        self.title = title
        self.description = description
        self.points = points

    def __str__(self):
        return f'Challenge(title={self.title}, description={self.description}, points={self.points})'

    def is_completed(self, completed_points):
        return completed_points >= self.points

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'points': self.points,
        }