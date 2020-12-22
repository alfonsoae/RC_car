import pigpio


class HardServo(pigpio.pi):
    __slots__ = ['gpio', 'freq', 'min_duty', 'max_duty', '_trim', '_angle', 'min_angle', 'max_angle']

    def __init__(self, gpio, freq, min_duty, max_duty, default_angle=90, min_angle=0, max_angle=180 ):
        super(HardServo, self).__init__()

        self._trim = default_angle
        self._angle = default_angle
        self.min_angle = min_angle
        self.max_angle = max_angle

        self.gpio = gpio
        self.freq = freq
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.set_mode(gpio, pigpio.OUTPUT)

    @property
    def trim(self):
        return self._trim

    @trim.setter
    def trim(self, set_trim):
        if self.max_angle >= set_trim >= self.min_angle:
            self._trim = set_trim

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, set_angle):
        if self.max_angle >= set_angle >= self.min_angle:
            self._angle = set_angle
            self.hardware_PWM(self.gpio, self.freq, self._duty())

    def _duty(self):
        return int( ((self.angle*10) / self.max_angle + self.min_duty)*10000 )

    def update(self, delta_angle=None):
        try:
            self.angle += delta_angle
        except TypeError:
            self.angle = self.trim

    def clean(self):
        self.hardware_PWM(self.gpio, 0, 0)
