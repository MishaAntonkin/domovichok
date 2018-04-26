def chunk_generator(data, piece):
    if not data:
        raise Exception('no data to slice')
    elif piece < 1:
        raise Exception('no sence to slice')
    for i, inx in enumerate(data[::piece]):
        yield data[i*piece:(i+1)*piece]