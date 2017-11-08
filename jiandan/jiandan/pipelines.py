# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
class JiandanPipeline(object):
    def process_item(self, item, spider):
        dir_path = 'e:/nihao'#存储路径
        print('创建目录')
        
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['img_urls']:
            list_name = image_url.split('/')
            file_name = list_name[-1]#图片名称
            # print 'filename',file_name
            file_path = '%s/%s'%(dir_path,file_name)
            # print 'file_path',file_path
            if os.path.exists(file_name):
                continue
            with open(file_path,'wb') as file_writer:
                conn = requests.get("https:"+image_url)#下载图片
                file_writer.write(conn.content)
            file_writer.close()
        return item
