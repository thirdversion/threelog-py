from abc import ABC, abstractmethod


class TracerImplementation(ABC):
    @abstractmethod
    def get_trace_id(self) -> str:
        raise NotImplementedError()
