from qqai.base import *

class Nlp(QQAIBase):
    """自然语言"""

    def text_translate_ailab(self,text,type=0):
        """文本翻译（AI Lab）"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_texttrans'

        self.params = {'app_id': self.app_id,
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'type': type,
                  'text': text,
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)


    def text_translate_fanyi(self,text,source='auto', target='en'):
        """文本翻译（翻译君）"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_texttranslate'
        self.params = {'app_id': self.app_id,
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'text': text,
                  'source': source,
                  'target': target,
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)

    def text_detect(self, text,candidate_langs=None, force=0):
        """语种识别"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textdetect'
        if candidate_langs is None:
            candidate_langs = ['zh', 'en', 'jp', 'kr']
        if type(candidate_langs) == str:
            candidate_langs_param = candidate_langs
        else:
            candidate_langs_param = '|'.join(candidate_langs)
        self.params = {'app_id': self.app_id,
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'text': text,
                  'candidate_langs': candidate_langs_param,
                  'force': force
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)



    def image_translate(self,image_path, scene='doc', source='auto', target='auto'):
        """图片翻译"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_imagetranslate'
        self.params = {'app_id': self.app_id,
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'image': self.get_base64(image_path),
                  'session_id': self._time_stamp(),
                  'scene': scene,
                  'source': source,
                  'target': target,
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)

    def text_chat(self,question):
        """图片翻译"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'
        self.params = {'app_id': self.app_id,
                  'time_stamp': self._time_stamp(),
                  'nonce_str': self._time_stamp(),
                  'session': self._time_stamp(),
                  'question': question
                  }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)  

# class Text(QQAIBase):
#     """基础文本分析"""

#     def word_seg(self, text):
#         """"分词"""
#         self.api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordseg'
#         self.params = {'app_id': self.app_id,
#                        'time_stamp': self._time_stamp(),
#                        'nonce_str': self._time_stamp(),
#                        'text': text
#                        }
#         self.params['sign'] = self.get_sign(self.params)
#       s = self.call_api(self.params)
        # contants = s.read()
        # s.close()
        # return json.loads(contants)

#     def word_pos(self, text):
#         """"词性标注"""
#         self.api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordpos'
#         self.params = {'app_id': self.app_id,
#                        'time_stamp': self._time_stamp(),
#                        'nonce_str': self._time_stamp(),
#                        'text': text
#                        }
#         self.params['sign'] = self.get_sign(self.params)
#       s = self.call_api(self.params)
        # contants = s.read()
        # s.close()
        # return json.loads(contants)

#     def word_ner(self, text):
#         """"专有名词识别"""
#         self.api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordner'
#         self.params = {'app_id': self.app_id,
#                        'time_stamp': self._time_stamp(),
#                        'nonce_str': self._time_stamp(),
#                        'text': text
#                        }
#         self.params['sign'] = self.get_sign(self.params)
#         s = self.call_api(self.params)
        # contants = s.read()
        # s.close()
        # return json.loads(contants)

#     def word_syn(self, text):
#         """"同义词识别"""
#         self.api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordsyn'
#         self.params = {'app_id': self.app_id,
#                        'time_stamp': self._time_stamp(),
#                        'nonce_str': self._time_stamp(),
#                        'text': text
#                        }
#         self.params['sign'] = self.get_sign(self.params)
#                 s = self.call_api(self.params)
        # contants = s.read()
        # s.close()
        # return json.loads(contants)

#     def word_com(self, text):
#         """"意图成分识别"""
#         self.api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordcom'
#         self.params = {'app_id': self.app_id,
#                        'time_stamp': self._time_stamp(),
#                        'nonce_str': self._time_stamp(),
#                        'text': text
#                        }
#         self.params['sign'] = self.get_sign(self.params)
#                 s = self.call_api(self.params)
        # contants = s.read()
        # s.close()
        # return json.loads(contants)

#     def text_polar(self, text):
#         """"情感分析识别"""
#         self.api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar'
#         self.params = {'app_id': self.app_id,
#                        'time_stamp': self._time_stamp(),
#                        'nonce_str': self._time_stamp(),
#                        'text': text
#                        }
#         self.params['sign'] = self.get_sign(self.params)
#                 s = self.call_api(self.params)
        # contants = s.read()
        # s.close()
        # return json.loads(contants)


