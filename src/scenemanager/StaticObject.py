from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *

from WorldObject import WorldObject

class StaticObject(WorldObject):
	def __init__(self,file = False):
		#calling parent method
		WorldObject.__init__(self)
		
		self.originalFilename = file
		self.placeholder = False
		self.locking = False
		
		if file != False:
			self.loadModel(file)
	
	def getPropertyList(self):
		properties = {}
		
		properties["name"] = self.getName()
		
		return properties
	
	def getFilename(self):
		return self.originalFilename
	
	def getName(self):
		return self.model.getName()
	
	def setX(self,factor):
		self.model.setX(self.model.getX()+factor)
		
		if self.placeholder != False:
			self.placeholder.setX(self.placeholder.getX()+factor)
	
	def setY(self,factor):
		self.model.setY(self.model.getY()+factor)
		
		if self.placeholder != False:
			self.placeholder.setY(self.placeholder.getY()+factor)
	
	def setZ(self,factor):
		self.model.setZ(self.model.getZ()+factor)
		
		if self.placeholder != False:
			self.placeholder.setZ(self.placeholder.getZ()+factor)
	
	def setH(self,factor):
		self.model.setH(self.model.getH()+factor)
		
		if self.placeholder != False:
			self.placeholder.setH(self.placeholder.getH()+factor)
	
	def setP(self,factor):
		self.model.setP(self.model.getP()+factor)
		
		if self.placeholder != False:
			self.placeholder.setP(self.placeholder.getP()+factor)
	
	def setR(self,factor):
		self.model.setR(self.model.getR()+factor)
		
		if self.placeholder != False:
			self.placeholder.setR(self.placeholder.getR()+factor)
	
	def setProperty(self, key, value):
		if key == "name":
			print "INFO: storing new name"
			self.setName(value)
	
	def setName(self,s):
		ext = s.split(".")[-1]
		
		#forcing egg extension
		if len(ext)>0:
			if ext != "egg":
				self.model.setName(s+".egg")
			else:
				self.model.setName(s)
	
	def loadPlaceHolder(self,file):
		#hiding real model
		if self.model != False:
			self.model.hide()
		#inserting placeholder
		self.placeholder = loader.loadModel("dataset/"+file)
		self.placeholder.reparentTo(self.model)
	
	def unloadPlaceHolder(self):
		if self.model != False:
			self.model.show()
		self.placeholder.remove()

	def loadModel(self,file):
		#loading model egg file
		self.model = loader.loadModel("dataset/"+file)
		self.model.reparentTo(myApp.getSceneNode())
		#storing type of object in scene
		self.type = "StaticObject"
		#storing options such as lightning
		self.lightning = True
		self.shaders = False
		self.wireframe = False
		self.hidden = False
	
	def getModel(self):
		return self.model
	
	def setLocking(self,v):
		self.locking = v
		#real control is done in InputHandler
	
	def getLocking(self):
		return self.locking
	
	def getWireframe(self):
		isWireframed = self.model.getRenderMode()
		if isWireframed == 0 or isWireframed == 1:
			isWireframed = False
		else:
			isWireframed = True
		return isWireframed
	
	def setLightning(self,v):
		self.lightning = v
		if v == True:
			#setting all lights on
			for l in myObjectManager.lightList:
				self.model.setLight(l.getNodePath())
		else:
			#set all lights off
			self.model.setLightOff()
	
	def getLightning(self):
		return self.lightning
	
	def setShaders(self,v):
		self.shaders = v
		if v == True:
			self.model.setShaderAuto()
		else:
			self.model.setShaderOff()

	def getShaders(self):
		return self.shaders
	
	def setHidden(self,v):
		self.hidden = v
		if v == True:
			pass #needed to be written with a placeholder or something
		else:
			pass #lululul
			
	def getHidden(self):
		return self.hidden

	#warn: not advised to directly set the type
	def setType(self,s):
		self.type = s

	def getType(self):
		return self.type
	
	def remove(self):
		#first remove it from camera
		myCamera.getSelectionTool().removeObject(self)
		#then release memory
		self.model.remove()
