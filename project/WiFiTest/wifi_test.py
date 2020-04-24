import socket
import threading
from random import randrange
from time import sleep

DEFAULT_HOST = '0.0.0.0'
DEFAULT_PORT = 8899


class WiFiData:
  """ WIFI 协议数据 """

  def __init__(self):
    self.device = 0
    self.station_horizontal = 0.0
    self.station_vertical = 0.0
    self.rainshed_horizontal = 0
    self.rainshed_vertical = 0
    self.rail_distance = 0.0
    self.exceed_height = 0.0
    self.km = 0.0
    self.temperature = 0.0

  def _toDevice(self):
    return format(self.device, '0>8d')

  def _toStationHorizontal(self):
    return format(self.station_horizontal, '0>6.1f')

  def _toStationVertical(self):
    return format(self.station_vertical, '0>6.1f')

  def _toRainshedHorizontal(self):
    return format(self.rainshed_horizontal, '0>4.0f')

  def _toRainshedVertical(self):
    return format(self.rainshed_vertical, '0>4.0f')

  def _toRailDistance(self):
    return format(self.rail_distance, '0>6.1f')

  def _toExceedHeight(self):
    v = format(abs(self.exceed_height), '0>5.1f')
    if self.exceed_height < 0:
      return '-' + v
    else:
      return '+' + v

  def _toKM(self):
    v = format(self.km, '0>11.3f')
    if self.km < 0:
      return v
    else:
      return '+' + v

  def _toTemperature(self):
    v = format(self.temperature, '0>4.1f')
    if self.temperature < 0:
      return v
    else:
      return '+' + v

  def toBytes(self):
    data = 'AR{0}ZL{1}ZH{2}YL{3}YH{4}GJ{5}CG{6}LS{7}TW{8}'.format(
        self._toDevice(), 
        self._toStationHorizontal(), self._toStationVertical(),
        self._toRainshedHorizontal(), self._toRainshedVertical(),
        self._toRailDistance(), self._toExceedHeight(),
        self._toKM(), self._toTemperature()
    )
    code = 0
    for s in data:
      if s.isnumeric():
        code = code + int(s)

    # 补位或截断
    code = format(code, '0>2d')[-2:]
    return 'S{0}U{1}P'.format(data, code).encode()

  def generate(self):
    self.km = self.km + 10
    self.station_horizontal = randrange(1800, 1900)
    self.station_vertical = randrange(1200, 1300)
    self.rainshed_horizontal = randrange(1700, 1800)
    self.rainshed_vertical = randrange(6400, 6600)
    self.rail_distance = randrange(1400, 1500)
    self.exceed_height = randrange(-10, 20)
    self.temperature = randrange(20, 30)


def start_service():
  """ 启动服务端 """
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((DEFAULT_HOST, DEFAULT_PORT))
    s.listen(10)
  except socket.error as msg:
    print(msg)

  print(f'服务端已启动:{DEFAULT_PORT}...')
  while True:
    client, addr = s.accept()
    t = threading.Thread(target=client_proc, args=(client, addr))
    t.start()


def client_proc(client, addr):
  """ 客户端连接数据处理 """

  print(f'新连接进入：{addr}')

  data = WiFiData()
  data.device = randrange(10000000, 99999999)

  while True:
    # 生成并发送数据
    data.generate()
    client.sendall(data.toBytes())

    # client.sendall(b'SAR36058886ZL1802.0ZH1220.0YL1767YH6513GJ1429.0CG0-9.0LS+0000010.000TW+28.0U32P')

    # 等待并回复
    recv = client.recv(1024)
    if not recv:
      print(f'对方已断开:{addr}')
      break

    try:
      str = recv.decode()
      if str != 'SOKP':
        print(f'返回内容异常:{str}')    
    except Exception as e:
      print(f'解析返回数据异常：{e}')

    sleep(1)
    

  client.close()
  print(f'连接已断开：{addr}')


if __name__ == "__main__":
  start_service()
