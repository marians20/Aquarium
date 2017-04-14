"""Container for execution elements and sensors"""

import json

from .execution_element import ExecutionElement

class Context:
    """Container for execution elements and sensors"""

    def __init__(self):
        self.execution_elements = [
            ExecutionElement("ColdLight"),
            ExecutionElement("WarmLight")
        ]
        id=1
        for item in self.execution_elements:
            item.Id = id
            id = id + 1
        self.sensors = []

    def __getitem_by_name__(self, name):
        for index, item in enumerate(self.execution_elements):
            if item.Name == name:
                return item

    def __getitem__(self, key):
        return self.Get(key)

    def Get(self, key):
        for item in self.execution_elements:
            if item.Id == key:
                return item
        return "Pula"

    @property
    def ExecutionElements(self):
        return self.execution_elements

    def __str__(self):
        result = []
        for item in self.execution_elements:
            result.append(json.loads(str(item)))
        return json.dumps(result)
