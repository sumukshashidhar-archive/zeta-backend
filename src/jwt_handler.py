import requests
import jwt


def decode(encoded_jwt):
    response = eval(requests.get("http://40.76.37.214:3000/key").text)
    if response['status'] == 200:
        publicKEY = bytes(response['key'], "ascii")
        print(publicKEY)
        claims = jwt.decode(encoded_jwt, publicKEY, algorithms="RS512")
        return (True, claims)
    else:
        return (False, 500)


if __name__ == "__main__":
    token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im5uMXZoOFV4cWNuNUY2VG1TaCIsInJvbGUiOiJkZXZpY2UiLCJpYXQiOjE2MDA0ODk3NjYsImV4cCI6MTYwMDU3NjE2NiwiaXNzIjoiU2lnbW9pZCBBdXRoZW50aWNhdGlvbiBTZXJ2aWNlIn0.4UBLjgsMxD8agzWVn6Ub-QG_KdvYHZoV7XwP0cf37Kn6Ej3xsYMDhpsFYY8r8HUCL3FhZwg1Whgl0ETOLHrDePe33VYhLsE7N2vlQmd48qm-MfEXYIvfR0PE42P-pR_XwhUYCLYcjCSwsjEqXiIUXzuVlX-LKxH2u15lDehYpyoRkQCfwiMhG_u2_7DJrtWCsvq4fLmrzl2AEU2jCj2Rm6ryu10mrpf-WjMbKqtRqwCFa9nIGUQI8jFL3y4c5vKSIVRo7fsPowWTM7Yq83UOeibK1ygTIJqEC7wxLnIj69oFBXYaznpfs9m3akQYar0l_j1iFMBp1a-fF6rq0PmnEHE50-jXShOMqv6UGPyxEbcFlCH4mVccmKqEFGKKfWFipYMhVmYBwwfzpOXzvBHv_UkSodoxROQc5i_8WpaSKMzFSyfKf90zanJr2FPJMtF75u1Ct_ijNIqq9Vzvi6DlKhYX91OPDc4NMb0W11IjDVOjrliL1qRR7rfJvUtU805K73HEhXZGXdwfLVQgSeSMwWmVUHDUVn70hMKGAMTn2w08SqV2ZGa14GbY0yGu11Mw5Yz4AsCVC4jiEYNx4dkX8_Wrbh53lIrI4fZlQl4-YnP8Z8oG80a0cSwOe_Qm5_U-Kl37vt-OVRiUmuuUD8bp6tt8UArJm6l5dFjB39MPMDk"
    decode(token)