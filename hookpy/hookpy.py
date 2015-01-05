import pyxhook as hook
import time

class Hook:
    def __init__(self,onKbEvent=lambda x: True,onMouseEvent=lambda x: True,kill_on_esc=False):
        # self.ind = indicator
        self.hm = hook.HookManager()
        self.hm.HookKeyboard()
        self.hm.KeyDown = self.kbdown
        self.hm.KeyUp = self.kbup
        self.hm.start()
        self.active_modifiers=[]
        self.modifiers=['Control_L','Control_R','Shift_L','Shift_R']
        self.onKbEvent=onKbEvent
        self.onMouseEvent= onMouseEvent
        self.kill_on_esc=kill_on_esc

    def kbdown(self, event):
        # print event.Key,'down'
        if event.Key in self.modifiers:
            self.active_modifiers.append(event.Key)
        else:
            if self.active_modifiers:
                event.Key= '+'.join(self.active_modifiers)+'+'+event.Key
                self.onKbEvent(event)
            else:
                self.onKbEvent(event)

        if self.kill_on_esc and event.Key=='Escape':
            self.kill()

    def kbup(self,event):
        # print event.Key,'up'
        if event.Key in self.active_modifiers:
            self.active_modifiers.remove(event.Key)


    def kill(self):
        time.sleep(2)
        self.hm.cancel()


def handle(event):
    print event.Key


if __name__ == '__main__':
    h=Hook(kill_on_esc=True)
    h.onKbEvent= handle



