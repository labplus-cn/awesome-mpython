from qqai.base import *

class Picture(QQAIBase):

    def imagetotext(self,image):
        """看图说话"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_imgtotext'

        self.params = {'app_id': self.app_id,
                  'session_id': self._time_stamp(),
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'image': self.get_base64(image)
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)

    def image_tag(self,image):
        """多标签识别"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/image/image_tag'

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

    def isfuzzy(self,image):
        """模糊图片检测"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/image/image_fuzzy'

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
    def isfood(self,image):
        """美食图片识别"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/image/image_food'

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

    # def scener_recog(self,image,topk=5,farmat=1):
    #     """场景识别 (调试不能使用)"""
    #     self.api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_scener'

    #     self.params = {'app_id': self.app_id,
    #               'time_stamp': self._time_stamp(),
    #               'nonce_str': self._time_stamp(),
    #               'format': farmat ,
    #               'topk': topk ,
    #               'image': self.get_base64(image)
    #               }
    #     self.params['sign'] = self.get_sign(self.params)
    #     s = self.call_api(self.params)
    #     contants = s.read()
    #     s.close()
    #     return json.loads(contants)

    # def object_recog(self,image,topk=5,farmat=1):
    #     """物体识别 (调试不能使用)"""
    #     self.api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_objectr'

    #     self.params = {'app_id': self.app_id,
    #               'time_stamp': self._time_stamp(),
    #               'nonce_str': self._time_stamp(),
    #               'format': farmat ,
    #               'topk': topk ,
    #               'image': self.get_base64(image)
    #               }
    #     self.params['sign'] = self.get_sign(self.params)
    #     s = self.call_api(self.params)
    #     contants = s.read()
    #     s.close()
    #     return json.loads(contants)

    def terrorism(self,image):
        """暴恐图片识别"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/image/image_terrorism'

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

    def porn(self,image):
        """智能鉴黄"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_porn'
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

    def image_filter_ptu(self,image, save_path,filter=1):
        """图片滤镜（天天P图）"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_imgfilter'
        self.params = {'app_id': self.app_id,
                    'time_stamp': self._time_stamp(),
                    'nonce_str': self._time_stamp(),
                    'filter': filter,
                    'image': self.get_base64(image)
                    }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        resp = self.response_base64_decode(s,b"\"image\": \"", save_path)
        return resp
       
    def image_filter_ailab(self,image, save_path,filter=1):
        """图片滤镜（AI Lab）"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_imgfilter'
        self.params = {'app_id': self.app_id,
                    'time_stamp': self._time_stamp(),
                    'nonce_str': self._time_stamp(),
                    'session_id': self._time_stamp(),
                    'filter': filter,
                    'image': self.get_base64(image)
                    }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        resp = self.response_base64_decode(s,b"\"image\": \"", save_path)
        return resp
       
    def face_cosmetic(self,image, save_path,cosmetic=1):
        """人脸美妆"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_facecosmetic'
        self.params = {'app_id': self.app_id,
                    'time_stamp': self._time_stamp(),
                    'nonce_str': self._time_stamp(),
                    'cosmetic': cosmetic,
                    'image': self.get_base64(image)
                    }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        resp = self.response_base64_decode(s,b"\"image\": \"", save_path)
        return resp

    def face_decoration(self,image, save_path,decoration=1):
        """人脸变妆"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_facedecoration'
        self.params = {'app_id': self.app_id,
                    'time_stamp': self._time_stamp(),
                    'nonce_str': self._time_stamp(),
                    'decoration': decoration,
                    'image': self.get_base64(image)
                    }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        resp = self.response_base64_decode(s,b"\"image\": \"", save_path)
        return resp

    def face_sticker(self,image, save_path,sticker=1):
        """大头贴"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_facesticker'
        self.params = {'app_id': self.app_id,
                    'time_stamp': self._time_stamp(),
                    'nonce_str': self._time_stamp(),
                    'sticker': sticker,
                    'image': self.get_base64(image)
                    }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        resp = self.response_base64_decode(s,b"\"image\": \"", save_path)
        return resp

  