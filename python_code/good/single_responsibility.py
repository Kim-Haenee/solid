#!/usr/bin/env python
# -*- coding: utf-8 -*-
# In this implementation, it provide the same functionality as `python_code.bad.single_responsibility`.
# There is only one reason to modify the code of `Email` if you want to support different protocol. For
# different content, you only need to define a new subtype of `IContent`. It's not the same in the
# implementation of `python_code.bad.single_responsibility` since there are 2 senario which you have to
# modify the code for `Email`: different content types and different protocols.

from abc import ABCMeta, abstractmethod

class IEmail(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def SetSender(self, sender):
        pass

    @abstractmethod
    def SetReceiver(self, receiver):
        pass

    @abstractmethod
    def SetContent(self, content):
        pass

class IContent(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getString(self):
        pass

class MyContent(IContent):

    def __init__(self, content):
        self.content = content

    def getString(self):
        return "<MyML>{}</MyML>".format(self.content)

class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def SetSender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def SetReceiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def SetContent(self, content):
        self.__content = content.getString()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)

def main():
    email = Email('IM')
    email.SetSender('qmal')
    email.SetReceiver('james')
    content = MyContent('Hello, there!')
    email.SetContent(content)
    print(email)

if __name__ == '__main__':
    main()
