import json
from channels import Group, Channel
from channels.auth import channel_session_user, channel_session_user_from_http
from .models import User_main
from django.core import serializers

@channel_session_user_from_http
def ws_connect(message):
    pass
    # print(4)
    # message.reply_channel.send({"accept": True})
    # message.channel_session['rooms'] = []
    # # print(dict(message))


# @channel_session_user
def ws_disconnect(message):
    pass
    # print(5)
    # for room_id in message.channel_session.get("rooms", set()):
    #     try:
    #         room = Room.objects.get(pk=room_id)
    #         room.websocket_group.discard(message.reply_channel)
    #     except Room.DoesNotExist:
    #         pass

def ws_receive(message):
    pass
    # print(6)
    # payload = json.loads(message['text'])
    # payload['reply_channel'] = message.content['reply_channel']
    # Channel("chat.receive").send(payload)


# @catch_client_error
# @channel_session_user
# def chat_join(message):
#     print(7)
#     l1=[]
#     l2=[]
#     room = get_room_or_error(message["room"], message.user)
#     if NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
#         room.send_message(None, message.user, MSG_TYPE_ENTER)
#     log = Comments.objects.filter(room=message["room"])
#     for l in log:
#         l1.append(l.comment)
#         l1.append(str(l.user))
#         l2.extend([l1])
#         l1=[]
#     # log1 = serializers.serialize('json', log)
#     # print("----",log1)
#     # for i in log1:
#     #     print(i)
#     # print("=========",log1)
#     room.websocket_group.add(message.reply_channel)
#     message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([room.id]))
#     message.reply_channel.send({
#         "text": json.dumps({
#             "join": str(room.id),
#             "title": room.title,
#             "d":l2,
#         }),
#     })


# @channel_session_user
# @catch_client_error
# def chat_leave(message):
#     print(9)
#     room = get_room_or_error(message["room"], message.user)
#     if NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
#         room.send_message(None, message.user, MSG_TYPE_LEAVE)

#     room.websocket_group.discard(message.reply_channel)
#     message.channel_session['rooms'] = list(set(message.channel_session['rooms']).difference([room.id]))
#     message.reply_channel.send({
#         "text": json.dumps({
#             "leave": str(room.id),
#         }),
#     })


# @catch_client_error
# @channel_session_user
# def chat_send(message):
#     print(10)
#     if int(message['room']) not in message.channel_session['rooms']:
#         raise ClientError("ROOM_ACCESS_DENIED")
#     room = get_room_or_error(message["room"], message.user)
#     Comments.objects.create(room = message["room"],user=message.user, comment=message["message"])
#     room.send_message(message["message"], message.user)