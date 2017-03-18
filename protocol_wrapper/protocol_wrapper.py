from __future__ import print_function


class ProtocolWrapper(object):
    def __init__(self,
                 header='\x61',
                 footer='\x62',
                 dle='\xAB',
                 after_dle_func=lambda x: x):
        self.header = header
        self.footer = footer
        self.dle = dle
        self.after_dle_func = after_dle_func

        self.state = self.WAIT_HEADER
        self.frame = ''

    # internal state
    (WAIT_HEADER, IN_MSG, AFTER_DLE) = range(3)

    def input(self, byte):
        """ Receive a byte.
            If this byte completes a frame, the
            frame is returned. Otherwise, None
            is returned.
        """
        if self.state == self.WAIT_HEADER:
            if byte == self.header:
                self.state = self.IN_MSG
                self.frame = ''

            return None
        elif self.state == self.IN_MSG:
            if byte == self.footer:
                self.state = self.WAIT_HEADER
                return self.frame
            elif byte == self.dle:
                self.state = self.AFTER_DLE
            else:
                self.frame += byte
            return None
        elif self.state == self.AFTER_DLE:
            self.frame += self.after_dle_func(byte)
            self.state = self.IN_MSG
            return None
        else:
            raise AssertionError()


bytes_input = ''.join(chr(b) for b in [
    0x70, 0x24,
    0x61, 0x99, 0xAF, 0xD1, 0x62,
    0x56, 0x62,
    0x61, 0xAB, 0xAB, 0x14, 0x62,
    0x7
])

pw = ProtocolWrapper()

result = (pw.input(byte) for byte in bytes_input)
for r in result:
    if r:
        print('Got frame:', r.encode('hex'))
