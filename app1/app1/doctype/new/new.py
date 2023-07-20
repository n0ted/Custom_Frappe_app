# Copyright (c) 2023, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import today 
from frappe.model.document import Document
from datetime import datetime # from python std library

class new(Document):
	
	def validate(self):
		self.time = datetime.now().strftime("%H:%M")
		self.datee = datetime.now().strftime("%Y-%m-%d")
		if len(self.details):
			if self.stage != self.details[len(self.details)-1].status:
				
				if self.stage == "Lead":
					self.append(
						"details",
						{
							"status": "Lead",
							"date":self.datee,
							"end_time":self.time,
							"user":frappe.session.user
						}
					)
				else:
					self.append(
						"details",
						{
							"status":self.stage,
							"date":self.datee,
							"end_time":self.time,
							"user":frappe.session.user
						}
					)
				
		else:
			if self.stage == "Lead":
				self.append(
					"details",
					{
						"status" : "Lead",
						"date":self.datee,
						"end_time":self.time,
						"user":frappe.session.user
					}
				)
				
				
	# # pass
	
	# def validate(self):cd cd fra
	# 	a = self.age
	# 	# frappe.msgprint(a)
	# 	if self.age != a:
	# 		frappe.msgprint("bbfdv")
	# 		# return
	# 	else:
	# 		frappe.msgprint("HI")
	# 		# self.time = datetime.now().strftime("%H:%M")
