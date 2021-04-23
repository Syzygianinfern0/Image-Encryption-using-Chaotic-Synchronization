import cv2
import numpy as np

np.random.seed(0)


def quantizer(values):
    return np.floor(values)


def unpack_bits_to_uint8(bits):
    output = []
    for i in range(0, len(bits), 8):
        bit_8 = bits[i : i + 8]
        output.append(int("".join(str(x) for x in bit_8), 2))
    return np.array(output)


def deskewer(bits):
    deskewed = []
    for i in range(0, len(bits), 2):
        if bits[i] == 0 and bits[i + 1] == 1:
            deskewed.append(0)
        if bits[i] == 1 and bits[i + 1] == 0:
            deskewed.append(1)
    return np.array(deskewed)


def main():
    input_img = cv2.imread("lena_std.png", cv2.IMREAD_GRAYSCALE)
    input_img = cv2.resize(input_img, (64, 64))
    flattened_array = input_img.flatten()

    # random_stream = np.random.random(64 * 64 * 8 * 4) + 0.5
    random_stream = str(open(tcurve.txt).read())
    random_bits = quantizer(random_stream)
    deskewed_bits = deskewer(random_bits)
    deskewed_uint8 = unpack_bits_to_uint8(deskewed_bits)

    encrypted_stream = np.bitwise_xor(flattened_array, deskewed_uint8)
    encrypted_img = np.resize(encrypted_stream, (64, 64))
    encrypted_img = encrypted_img.astype(np.uint8)

    decrypted_stream = np.bitwise_xor(encrypted_stream, deskewed_uint8)
    decrypted_img = np.resize(decrypted_stream, (64, 64))
    decrypted_img = decrypted_img.astype(np.uint8)

    cv2.namedWindow("input_img", cv2.WINDOW_NORMAL)
    cv2.namedWindow("encrypted_img", cv2.WINDOW_NORMAL)
    cv2.namedWindow("decrypted_img", cv2.WINDOW_NORMAL)
    cv2.imshow("input_img", input_img)
    cv2.imshow("encrypted_img", encrypted_img)
    cv2.imshow("decrypted_img", decrypted_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.imwrite("encrypted_img.png", encrypted_img)
    cv2.imwrite("decrypted_img.png", decrypted_img)
    print("Done")


if __name__ == "__main__":
    main()
