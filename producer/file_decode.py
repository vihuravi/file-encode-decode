import base64
from file_encode_decode.consumer.file_encode import file_encode

def file_decode(f_image):
    v = f_image.encode('utf-8')
    with open('best.xlsx', 'wb') as file_save:
        file_image=base64.decodebytes(v)
        file_save.write(file_image)

f = file_encode()
file_decode(f)