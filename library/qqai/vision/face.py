from qqai.base import *

class Face(QQAIBase):

    def detect_face(self,image,mode=1):
        """人脸检测与分析"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/face/face_detectface'
        self.params = {'app_id': self.app_id,
                    'time_stamp': self._time_stamp(),
                    'nonce_str': self._time_stamp(),
                    'mode': mode,
                    'image': self.get_base64(image)
                    }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)
       