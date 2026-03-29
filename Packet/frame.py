import re

class PDU:
    def __init__(self, payload):
        if type(self) == PDU:
            raise TypeError("Z PDU nelze vytvářet přímé instance.")
        self._payload = str(payload)

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        self._payload = str(value)

    def isValid(self):
        raise NotImplementedError()

class EthFrame(PDU):
    def __init__(self, dmac, smac, type, payload, fcs=None):
        super().__init__(payload)
        
        if not self.isValidMac(dmac) or not self.isValidMac(smac):
            raise ValueError("Invalid MAC")

        self._dmac = dmac
        self._smac = smac
        self._type = type
        
        if fcs is None:
            self.recalculateFcs()
        else:
            self._fcs = fcs

    @staticmethod
    def isValidMac(mac):
        pattern = r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$"
        return bool(re.match(pattern, mac))

    def calculateFcs(self):
        data_to_hash = f"{self._dmac}{self._smac}{self._type}{self.payload}"
        return sum(ord(char) for char in data_to_hash)

    def recalculateFcs(self):
        self._fcs = self.calculateFcs()

    @PDU.payload.setter
    def payload(self, value):
        super(EthFrame, EthFrame).payload.fset(self, value)
        self.recalculateFcs()

    def isValid(self):
        return self._fcs == self.calculateFcs()

    def corruptData(self):
        self._payload = "ERR_DATA_CORRUPT"
        self._fcs = -1

    def __str__(self):
        return f"[EthFrame] SRC: {self._smac} DST: {self._dmac} TYPE: {self._type} DATA: {self.payload} FCS: {self._fcs}"