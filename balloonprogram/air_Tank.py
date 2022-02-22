from tank import Tank

class Airtank(Tank):
    def __init__(self, air_type):
        super().__init__(5)
        self._air_type = air_type
    pass

    def release(self, volume_ml):
        return super().release(volume_ml)