import json
from enum import Enum

UNKNOWN_ID = 'FFFF'

class MessageType(Enum):
  GET = 'get'
  PUT = 'put'

class Message:
  def __init__(self, t: MessageType, src: str, dest: str, leader: str = UNKNOWN_ID):
    self.src = src
    self.dest = dest
    self.leader = leader
    self.type = t

  @staticmethod
  def from_str(s: str):
    fields = json.loads(s)
    return Message(fields['type'], fields['src'], fields['dest'], fields['leader'])

  def to_str(self):
    return json.dumps({
      self.src, self.dest, self.leader, self.type
    })