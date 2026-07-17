class LocatorMemory:


    def __init__(self):

        self.memory = {}



    def save_locator(
        self,
        element,
        locator
    ):

        self.memory[element] = locator



    def get_locator(
        self,
        element
    ):

        return self.memory.get(
            element
        )



locator_memory = LocatorMemory()