from lib import Leap

class LeapListener(Leap.Listener): 
    def __init__(self,callback): 
        self.callback = callback
        super(LeapListener, self).__init__()

    def onFrame(self, controller): 
        callback(controller.frame())