###
# Copyright (c) 2009, Patrik Bjornfot
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


import xml.dom.minidom as minidom

class Osumu(callbacks.Plugin):
    """Add the help for "@plugin help Osumu" here
    This should describe *how* to use this plugin."""
  
   
    def event(self, irc, msg, args):

      doc = self.getXmlFile()
     
      for eventElement in doc.childNodes[0].childNodes:
	if eventElement.nodeType == eventElement.ELEMENT_NODE:
	   irc.reply("---------------------------------")
	   irc.reply(eventElement.childNodes[0].childNodes[0].nodeValue)
	   irc.reply(eventElement.childNodes[1].childNodes[0].nodeValue)
	   irc.reply(eventElement.childNodes[2].childNodes[0].nodeValue)
	   
     
      pass
      
          
    def getXmlFile(self):
      doc = minidom.parse("/var/lib/python-support/python2.5/supybot/plugins/Osumu/xmlEvents/test.xml")
      return doc  
      
    def writeXmlFile(self, doc):
      file_object = open("/var/lib/python-support/python2.5/supybot/plugins/Osumu/xmlEvents/test.xml", "w")
      doc = doc2
      doc2.writexml(file_object)
      
    
      
    def write(self, irc, msg, args):
      file_object = open("/var/lib/python-support/python2.5/supybot/plugins/Osumu/xmlEvents/test.xml", "w")
      
      doc = minidom.Document()
      
      eventsElement = doc.createElementNS("epp","evens")
      eventElement = doc.createElementNS("epp","event")
      
      nameElement = doc.createElementNS("epp","name")
      nameText = doc.createTextNode(args[0])
      nameElement.appendChild(nameText)
      eventElement.appendChild(nameElement)
      
      dateElement = doc.createElementNS("epp","date")
      dateText = doc.createTextNode(args[1])
      dateElement.appendChild(dateText)
      eventElement.appendChild(dateElement)
      
      descElement = doc.createElementNS("epp","desc")
      descText = doc.createTextNode(args[2])
      descElement.appendChild(descText)
      eventElement.appendChild(descElement)
     
      eventsElement.appendChild(eventElement)
      doc.appendChild(eventsElement)
      doc2 = doc
      doc2.writexml(file_object)
      
      file_object.close()
      pass
    
    def oneevent(self, irc, msg, args):

      doc = self.getXmlFile()
      i = int(args[0])
      irc.reply("---------------------------------")
      irc.reply(doc.childNodes[0].childNodes[i].childNodes[0].childNodes[0].nodeValue)
      irc.reply(doc.childNodes[0].childNodes[i].childNodes[1].childNodes[0].nodeValue)
      irc.reply(doc.childNodes[0].childNodes[i].childNodes[2].childNodes[0].nodeValue)
      
     
      pass
    def delevent(self, irc, msg, args):

      doc = self.getXmlFile()
      i = int(args[0])
      aNode = doc.childNodes[0]
      bNode = aNode.childNodes[i]
      aNode.removeChild(bNode)
      
      self.writeXmlFile(doc)
      irc.reply("Event deleted")
      
      
      pass
      
    def newevent(self, irc, msg, args):
      
      
      doc = self.getXmlFile()
      
      eventsElement = doc.childNodes[0]
      eventElement = doc.createElementNS("epp","event")
      nameElement = doc.createElementNS("epp","name")
      nameText = doc.createTextNode(args[0])      
      nameElement.appendChild(nameText)
      eventElement.appendChild(nameElement)
      
      dateElement = doc.createElementNS("epp","date")
      dateText = doc.createTextNode(args[1])
      dateElement.appendChild(dateText)
      eventElement.appendChild(dateElement)
      
      descElement = doc.createElementNS("epp","desc")
      descText = doc.createTextNode(args[2])
      descElement.appendChild(descText)
      eventElement.appendChild(descElement)
      
      eventsElement.appendChild(eventElement)
      
      
      self.writeXmlFile(doc)
      file_object.close()
      pass

Class = Osumu

      
      
    
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
