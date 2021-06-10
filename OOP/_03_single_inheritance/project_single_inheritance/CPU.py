from Resource import Resource


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated)
        if not isinstance(cores, int) or cores <= 0:
            raise ValueError("Number of cores must be a positive integer")
        if not isinstance(power_watts, int) or power_watts <= 0:
            raise ValueError("Power must be a positive integer")
        self.socket = str(socket)
        self._power_watts = power_watts
        self._cores = cores

    @property
    def cores(self):
        return self._cores

    @property
    def power_watts(self):
        return self._power_watts
