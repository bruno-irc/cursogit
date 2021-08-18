def envia_lat_long_v4(latitude, longitude):
    frame_id = '\x01'

    DATA = '\x53\x42\x01\x0E' + latitude + '\x0F' + longitude + '\x10\x00\x11\x00\x13\x00\x16\x00'

    g = {
        'type': 'tx',
        'frame_id': frame_id,
        'dest_addr': Controlador,
        'data': DATA,
        'none': None
        #teste de git
        #teste branch
    }
    radio.send_xbee_frame(g)
