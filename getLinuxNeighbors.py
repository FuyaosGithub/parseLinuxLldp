import os
# json parse example
# 建議parse以下內容:
# 自己 : 可使用 getLldpInterfaces()
# 1.介面 位於lldp.interface
# 2.自己的ip  位於lldp.interface.chassis.mgmt-ip  (也可使用 getLldpSelfChassis())
# 鄰居 : 使用 getLldpNeighbors()
# 1.掃到的鄰居名稱 位於lldp.interface.chassic內
# 2.掃到的鄰居的ip 位於lldp.interface.chassic.mgmt-ip
# 3.鄰居裝置詳細描述 位於lldp.interface.chassic.descr

#getLldpInterfaces() example
# {
#   "lldp": {
#     "interface": [
#       {
#         "enp3s0": { //interface名稱
#           "via": "LLDP",
#           "age": "5 days, 16:26:49",
#           "chassis": {
#             "ricky-G3-3590": {
#               "id": {
#                 "type": "mac",
#                 "value": "e4:54:e8:15:ae:1e"
#               },
#               "descr": "Ubuntu 18.04.6 LTS Linux 5.4.0-107-generic #121~18.04.1-Ubuntu SMP Thu Mar 24 17:21:33 UTC 2022 x86_64",
#               "mgmt-ip": [
#                 "192.168.45.47", //自己的ip
#                 "fe80::3efe:405d:56e6:e8eb"
#               ],
#               "capability": [
#                 {
#                   "type": "Bridge",
#                   "enabled": false
#                 },
#                 {
#                   "type": "Router",
#                   "enabled": false
#                 },
#                 {
#                   "type": "Wlan",
#                   "enabled": true
#                 },
#                 {
#                   "type": "Station",
#                   "enabled": false
#                 }
#               ]
#             }
#           },
#           "port": {
#             "id": {
#               "type": "mac",
#               "value": "e4:54:e8:15:ae:1e"
#             },
#             "descr": "enp3s0"
#           },
#           "ttl": {
#             "ttl": "120"
#           }
#         }
#       },
#       {
#         "wlo1": { //interface名稱
#           "via": "LLDP",
#           "age": "3 days, 18:13:21",
#           "chassis": {
#             "ricky-G3-3590": {
#               "id": {
#                 "type": "mac",
#                 "value": "e4:54:e8:15:ae:1e"
#               },
#               "descr": "Ubuntu 18.04.6 LTS Linux 5.4.0-107-generic #121~18.04.1-Ubuntu SMP Thu Mar 24 17:21:33 UTC 2022 x86_64",
#               "mgmt-ip": [
#                 "192.168.45.47", //自己的ip
#                 "fe80::3efe:405d:56e6:e8eb"
#               ],
#               "capability": [
#                 {
#                   "type": "Bridge",
#                   "enabled": false
#                 },
#                 {
#                   "type": "Router",
#                   "enabled": false
#                 },
#                 {
#                   "type": "Wlan",
#                   "enabled": true
#                 },
#                 {
#                   "type": "Station",
#                   "enabled": false
#                 }
#               ]
#             }
#           },
#           "port": {
#             "id": {
#               "type": "mac",
#               "value": "90:78:41:1e:b6:26"
#             },
#             "descr": "wlo1"
#           },
#           "ttl": {
#             "ttl": "120"
#           }
#         }
#       }
#     ]
#   }
# }




#getLldpSelfChassis() example
# {
#   "local-chassis": { //固定key
#     "chassis": { //固定key
#       "ricky-G3-3590": { //自己裝置名稱
#         "id": {
#           "type": "mac",
#           "value": "e4:54:e8:15:ae:1e"
#         },
#         "descr": "Ubuntu 18.04.6 LTS Linux 5.4.0-107-generic #121~18.04.1-Ubuntu SMP Thu Mar 24 17:21:33 UTC 2022 x86_64",
#         "mgmt-ip": [
#           "192.168.45.47",
#           "fe80::3efe:405d:56e6:e8eb"
#         ],
#         "capability": [
#           {
#             "type": "Bridge",
#             "enabled": false
#           },
#           {
#             "type": "Router",
#             "enabled": false
#           },
#           {
#             "type": "Wlan",
#             "enabled": true
#           },
#           {
#             "type": "Station",
#             "enabled": false
#           }
#         ]
#       }
#     }
#   }
# }


#getLldpNeighbors() example
# {
#   "lldp": {  //固定key
#     "interface": {  //固定key
#       "wlo1": { //網卡名稱 可能parse到 eth0, ens160等
#         "via": "LLDP",
#         "rid": "172",
#         "age": "0 day, 00:24:38",
#         "chassis": {  //固定key，為主要主機
#           "U6-LR": { // 掃描到鄰居簡易名稱(建議1)
#             "id": {
#               "type": "mac", //該裝置網卡類型
#               "value": "d0:21:f9:82:c3:31" //該裝置網卡mac
#             },
#             "descr": "U6-LR, 6.0.19.13671", //掃描到的鄰居詳細資訊(建議3)
#             "mgmt-ip": [  //掃描到的鄰居ip(建議2)
#               "192.168.45.35", //ivp4 ip
#               "fe80::d221:f9ff:fe82:c331" //ivp6 ip
#             ],
#             "capability": [ //略
#               {
#                 "type": "Bridge",
#                 "enabled": true
#               },
#               {
#                 "type": "Router",
#                 "enabled": true
#               },
#               {
#                 "type": "Wlan",
#                 "enabled": true
#               },
#               {
#                 "type": "Station",
#                 "enabled": false
#               }
#             ]
#           }
#         },
#         "port": { //固定key值 列出該port資訊
#           "id": {
#             "type": "mac",
#             "value": "d0:21:f9:82:c3:33"
#           },
#           "descr": "rai0",
#           "ttl": "120"
#         }
#       }
#     }
#   }
# }

def getLldpSelfChassis():
    if os.name == 'nt':
        print('this is windows system, not support');
    if os.name == 'posix':
        result = os.popen("lldpcli show chassis -f json").read()
        print(result)
def getLldpNeighbors():
    if os.name == 'nt':
        print('this is windows system, not support');
    if os.name == 'posix':
        result = os.popen("lldpcli show neighbors -f json").read()
        print(result)
def getLldpInterfaces():
    if os.name == 'nt':
        print('this is windows system, not support');
    if os.name == 'posix':
        result = os.popen("lldpcli show interfaces -f json").read()
        print(result)

if __name__ == "__main__":
    getLldpNeighbors()
