import qrcode
from PIL import Image
import io
import base64

import qrcode.constants

class QRCodeUtil:
    @staticmethod
    def generate_qr(data: str,
                    version: int = 1,
                    error_correction: int = qrcode.constants.ERROR_CORRECT_L,
                    box_size: int = 10,
                    border: int = 4) -> Image.Image:
        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img

    @staticmethod
    def save_qr(image: Image.Image, file_path: str) -> None:
        image.save(file_path)
        print(f"QR kod '{file_path}' ga saqlandi.")

    @staticmethod
    def show_qr(image: Image.Image) -> None:
        image.show()

    @staticmethod
    def generate_and_save(data: str,
                          file_path: str,
                          version: int = 1,
                          error_correction: int = qrcode.constants.ERROR_CORRECT_L,
                          box_size: int = 10,
                          border: int = 4) -> None:
        img = QRCodeUtil.generate_qr(data, version, error_correction, box_size, border)
        QRCodeUtil.save_qr(img, file_path)



if __name__ == "__main__":
    root_path = "qr_images/"
    # TG username uchun eng yuqori H darajali QR kod
    tg = "https://t.me/Samandar_Hamrayev"
    qr_img = QRCodeUtil.generate_qr(tg, 2, qrcode.constants.ERROR_CORRECT_H)
    # yaratilgan QR kodni ko'rsatish
    QRCodeUtil.show_qr(qr_img) 
    # yaratilgan QR kodni saqlash
    QRCodeUtil.save_qr(qr_img, f"{root_path}tg.png")


    # QR kodni yaratish va saqlash
    QRCodeUtil.generate_and_save(
        "https://leetcode.com/u/Samandar_Hamrayev/", 
        f"{root_path}leedcode.png", 
        3, 
        qrcode.constants.ERROR_CORRECT_H)


