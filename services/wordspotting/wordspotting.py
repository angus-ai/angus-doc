#!/usr/bin/env python
# -*- coding: utf-8 -*-

import angus.cloud

conn = angus.connect()

service = conn.services.get_service('word_spotting', version=1)

w1_s1 = conn.blobs.create(open("/path/to/word1/sample1.wav"))
w1_s2 = conn.blobs.create(open("/path/to/word1/sample2.wav"))
w1_s3 = conn.blobs.create(open("/path/to/word1/sample3.wav"))

w2_s1 = conn.blobs.create(open("/path/to/word2/sample1.wav"))
w2_s2 = conn.blobs.create(open("/path/to/word2/sample2.wav"))
w2_s3 = conn.blobs.create(open("/path/to/word2/sample3.wav"))

vocabulary = {'turn wifi on': [w1_s1, w1_s2, w1_s3], 'turn wifi off': [w2_s1, w2_s2, w2_s3]}

service.enable_session({'vocabulary': vocabulary})

job = service.process({'sound': open("./sound.wav"), 'sensitivity': 0.7, 'lang': "en-US"})

service.disable_session()

print job.result
