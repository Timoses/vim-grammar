from dragonfly import MappingRule, Key, Text

class CtrlPRule(MappingRule):
    mapping = {
        "switch file": Key("colon") + Text("CtrlPMixed") + Key("enter"),
        "switch fault": Key("c-v"),
        "switch tab": Key("c-t"),
    }
    extras = []
    defaults = {}
