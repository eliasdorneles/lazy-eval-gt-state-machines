from __future__ import print_function


def protocol_wrapper(bytes_input,
                     header='\x61',
                     footer='\x62',
                     dle='\xAB',
                     after_dle_func=lambda x: x):
    it = iter(bytes_input)
    while True:
        byte = next(it)
        frame = ''

        if byte == header:
            # Capture the full frame
            #
            while True:
                byte = next(it)
                if byte == footer:
                    yield frame
                    break
                elif byte == dle:
                    byte = next(it)
                    frame += after_dle_func(byte)
                else:
                    frame += byte


bytes_input = ''.join(chr(b) for b in [
    0x70, 0x24,
    0x61, 0x99, 0xAF, 0xD1, 0x62,
    0x56, 0x62,
    0x61, 0xAB, 0xAB, 0x14, 0x62,
    0x7
])

for frame in protocol_wrapper(bytes_input):
    if frame:
        print('Got frame:', frame.encode('hex'))
