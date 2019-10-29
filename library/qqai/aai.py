from qqai.base import *


class AAI(QQAIBase):

    def aai_asr(self, speech, format=2, rate=16000):
        """语音识别-echo版"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/aai/aai_asr'
        self.params = {'app_id': self.app_id,
                       'time_stamp': self._time_stamp(),
                       'nonce_str': self._time_stamp(),
                       'format': format,
                       'rate': rate,
                       'speech': self.get_base64(speech)
                       }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        contants = s.read()
        s.close()
        return json.loads(contants)

    def aai_tts(self, text, save_path ,speaker =1, format=3, volume=10, speed=100, aht=0, apc=58):
        """语音合成（AI Lab）"""
        self.api = 'https://api.ai.qq.com/fcgi-bin/aai/aai_tts'
        self.params = {'app_id': self.app_id,
                       'time_stamp': self._time_stamp(),
                       'nonce_str': self._time_stamp(),
                       'text': text,
                       'speaker': speaker,
                       'format': format,
                       'volume': volume,
                       'speed': speed,
                       'aht': aht,
                       'apc': apc
                       }
        self.params['sign'] = self.get_sign(self.params)
        s = self.call_api(self.params)
        resp = self.response_base64_decode(s,b"\"speech\": \"",save_path)
        return resp
