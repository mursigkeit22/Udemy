from Resource import Resource


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, ):
        super().__init__(name, manufacturer, total, allocated)
        if not isinstance(capacity_GB, int) or capacity_GB <= 0:
            raise ValueError("Capacity must be a positive integer")
        self._capacity_GB = capacity_GB

    @property
    def capacity_GB(self):
        return self._capacity_GB


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        if not isinstance(rpm, int) or rpm <= 0:
            raise ValueError("rpm must be a positive integer")
        if size != 2.5 or size != 3.5:
            raise ValueError("Size must be 2.5 or 3.5 inches.")
        self._rpm = rpm
        self._size = size

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self.interface = str(interface)
