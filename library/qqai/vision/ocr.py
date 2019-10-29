from qqai.base import *

class OCR(QQAIBase):

    def general_ocr(self,image):
        """通用OCR"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr'

        self.params = {'app_id': self.app_id,
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'image': self.get_base64(image)
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)

    def driverlicense_ocr(self,image,type):
        """行驶证驾驶证OCR"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_driverlicenseocr'

        self.params = {'app_id': self.app_id,
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'image': self.get_base64(image),
                  'type': type
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)

    def handwriting_ocr(self,image):
        """手写体OCR"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_handwritingocr'

        self.params = {'app_id': self.app_id,
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'image': self.get_base64(image),
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)

    def plate_ocr(self,image):
        """车牌OCR"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_plateocr'

        self.params = {'app_id': self.app_id,
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'image': self.get_base64(image),
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)

    def bc_ocr(self,image):
        """名片OCR"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_bcocr'

        self.params = {'app_id': self.app_id,
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'image': self.get_base64(image),
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)

    def creditcard_ocr(self,image):
        """银行卡OCR"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_creditcardocr'

        self.params = {'app_id': self.app_id,
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'image': self.get_base64(image),
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)


