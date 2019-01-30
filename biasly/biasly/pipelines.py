# -*- coding: utf-8 -*-

import csv

class BiaslyPipeline(object):

	def __init__(self):
		self.csvwriter = csv.writer(open("cosmopolitan_new.csv", "w"))
		self.csvwriter.writerow(["title", "body", "url"])

	def process_item(self, item, spider):
		row = []
		row.append(item["title"])
		row.append(item["body"])
		row.append(item["url"])
		self.csvwriter.writerow(row)
		return item
