from urllib import parse
import hashlib
import ubinascii
import urequests
import usocket
import ussl
import gc
import time
import os
import sys
import time
import json
sys.path.append('../')


class QQAIBase:
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.params = {}

    def get_base64(self, media_path,save='.qqai_base64'):
        """获取媒体的Base64字符串

        :param media_param 媒体URL或文件路径
        """
        gc.collect()
        BLOCK_SZ = 1024 * 6
        with open(save, 'wb') as tmpfile:
            if type(media_path) == str:
                if 'https://' in media_path or 'http://' in media_path:
                    rsp = urequests.get(media_path)
                    while True:
                        chunk_data = rsp.raw.read(BLOCK_SZ)
                        if chunk_data:
                            chunk_data = ubinascii.b2a_base64(
                                chunk_data).strip()
                            # print(chunk_data.decode(),end='')
                            tmpfile.write(chunk_data)
                        else:
                            rsp.close()
                            break
                else:
                    with open(media_path, 'rb') as media_file:
                        while True:
                            chunk_data = media_file.read(BLOCK_SZ)
                            if chunk_data:
                                chunk_data = ubinascii.b2a_base64(
                                    chunk_data).strip()
                                # print(chunk_data.decode(),end='')
                                tmpfile.write(chunk_data)
                            else:
                                break
            else:
                raise TypeError('URL or file path must be str type')
        print("Base64 temporary files size: %0.3fKB" %
              (os.stat(save)[6]//1000))
        return tmpfile

    def get_sign(self, params):
        """获取签名"""
        gc.collect()
        uri_str = ''
        BLOCK_SZ = 1024*3
        # print("sign_str:  ",end='')
        hash_str = hashlib.md5()
        for key in sorted(params.keys()):
            if not hasattr(params[key], 'read'):
                uri_str = '{}={}&'.format(
                    key, parse.quote_plus(str(params[key]), safe=''))
                hash_str.update(uri_str)
                # print(uri_str,end='')
            else:
                uri_str = '{}=' .format(key)
                hash_str.update(uri_str)
                # print(uri_str,end='')
                with open('.qqai_base64', 'r') as file_base64:
                    while True:
                        chunk_data = file_base64.read(BLOCK_SZ)
                        if chunk_data:
                            uri_str = parse.quote_plus(chunk_data, safe='')
                            hash_str.update(uri_str)
                            # print(uri_str,end='')
                        else:
                            break
                    hash_str.update('&')
                    # print('&',end='')
        uri_str = 'app_key='+self.app_key
        hash_str.update(uri_str)
        # print(uri_str)
        return ubinascii.hexlify(hash_str.digest()).decode().upper()

    def call_api(self, params, api=None):
        gc.collect()
        if api is None:
            api = self.api
        rsp = self._qqai_post(api, params)
        gc.collect()
        return rsp

    def _time_stamp(self):
        return str(time.time() + 946656001)

    def _qqai_post(self, url, params):
        gc.collect()
        port = 443
        proto, dummy, host, path = url.split("/", 3)
        ai = usocket.getaddrinfo(host, port)
        # print(ai)
        addr = ai[0][4]
        s = usocket.socket()
        s.connect(addr)
        s = ussl.wrap_socket(s)
        s.write(b"%s /%s HTTP/1.0\r\n" % ('POST', path))
        s.write(b"Host: %s\r\n" % host)
        s.write(b"Connection: keep-alive\r\n")
        s.write(b"Content-Type: application/x-www-form-urlencoded\r\n")
        s.write(b"Transfer-Encoding: chunked\r\n")

        s.write(b"\r\n")
        temp_str = ''
        list_key = list(params.keys())
        for k in list_key:
            if not hasattr(params[k], 'read'):
                temp_str = k+'='+parse.quote_plus(str(params[k]), safe='')
                if k is not list_key[-1]:
                    temp_str = temp_str + '&'

                chunk_size = hex(len(temp_str))[2:]
                s.write(chunk_size.encode())
                # print(chunk_size,end='')
                s.write(b'\r\n')
                # print()
                s.write(temp_str.encode())
                # print(temp_str,end='')
                s.write(b'\r\n')
                # print()

            else:
                temp_str = k+'='
                chunk_size = hex(len(temp_str))[2:]
                s.write(chunk_size.encode())
                s.write(b'\r\n')
                # print(chunk_size)
                s.write(temp_str.encode())
                s.write(b'\r\n')
                # print(temp_str)
                with open('.qqai_base64', 'r') as file_base64:
                    while True:
                        temp_str = file_base64.read(1024*3)
                        if temp_str:
                            temp_str = parse.quote_plus(temp_str, safe='')
                            chunk_size = hex(len(temp_str))[2:]
                            s.write((chunk_size+'\r\n').encode())
                            # print(chunk_size)
                            s.write((temp_str+'\r\n').encode())
                            # print(temp_str)
                        else:
                            break
                if k is not list_key[-1]:
                    s.write(b'1\r\n')
                    # print('1')
                    s.write(b'&\r\n')
                    # print('&')
        # chunked end
        s.write(b'0\r\n')
        # print('0')
        s.write(b'\r\n')
        # print('')

        l = s.readline()
        protover, status, msg = l.split(None, 2)
        # print(protover, status, msg)
        status = int(status)
        while True:
            l = s.readline()
            # print(l)
            if not l or l == b"\r\n":
                break
        return s

    def response_base64_decode(self, socket, key_str, path):
        gc.collect()
        _socket = socket
        BlOCK_SZ = 512*4
        chunked = _socket.read(1024)
        if len(chunked) < 1024 and chunked[-1:] == b'\n':
            _socket.close()
            return json.loads(chunked.decode())
            # print(json.loads(chunked.decode()))
        else:
            with open(path, 'wb') as file_image:
                chunked = chunked.replace(b'\\', b'')
                index = chunked.find(key_str)
                if index != -1:
                    chunked = chunked[index+len(key_str):]
                    while (BlOCK_SZ-len(chunked)) != 0:
                        miss_len = BlOCK_SZ-len(chunked)
                        miss_str = _socket.read(miss_len).replace(b'\\', b'')
                        chunked = chunked+miss_str
                    # print(chunked.decode(),end='')
                    file_image.write(ubinascii.a2b_base64(chunked))
                while True:
                    chunked = _socket.read(BlOCK_SZ).replace(b'\\', b'')
                    while (BlOCK_SZ-len(chunked)) != 0:
                        miss_len = BlOCK_SZ-len(chunked)
                        miss_str = _socket.read(miss_len).replace(b'\\', b'')
                        chunked = chunked+miss_str
                        index_end = chunked.find(b"\"")
                        if index_end != -1:
                            chunked = chunked[:index_end]
                            # print(chunked.decode(),end='')
                            file_image.write(ubinascii.a2b_base64(chunked))
                            _socket.close()
                            return True
                    # print(chunked.decode(),end='')
                    file_image.write(ubinascii.a2b_base64(chunked))
