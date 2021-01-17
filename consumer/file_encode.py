import base64

def file_encode():
    with open('/file_encode_decode/consumer/Build-in function.xlsx', 'rb') as f:
        file = f.read()
        binary_code=base64.b64encode(file)
        binary_msg=binary_code.decode('utf-8')
        return binary_msg

# f_image = file_encode()
# file_decode(f_image)

