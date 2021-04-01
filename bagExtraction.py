import bagpy 
from bagpy import bagreader
b=bagreader('file path')
b.topic_table
velmsgs=b.vel_data()
velmsgs
import pandas as pd
velf=pd.read_csv(velmsgs[0])
velf
newmsg=b.message_by_topic(topic='topic name')
newmsg
