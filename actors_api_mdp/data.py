import dataclasses
from enum import Enum
from typing import Any, Dict

from actors_api_mdp.helpers import ServiceId
from actors_api_mdp.services import Service, build_service_from_transitions
from actors_api_mdp.types import TransitionFunctionReward


class ServiceType(Enum):
    SERVICE = "service"
    TARGET = "target"


@dataclasses.dataclass(eq=True)
class ServiceInstance:
    service_id: ServiceId
    service_spec: Service
    current_state: Any
    transition_function: TransitionFunctionReward

    @classmethod
    def from_json(cls, obj: Dict) -> "ServiceInstance":
        """Get the service instance from JSON format."""
        service_id = ServiceId(obj["id"])
        service_type = ServiceType(obj["attributes"]["type"])
        assert service_type == ServiceType.SERVICE

        current_transition_function = obj["features"]["transition_function"]
        current_state = obj["features"]["current_state"]

        transitions = obj["attributes"]["transitions"]
        initial_state = obj["attributes"]["initial_state"]
        final_states = set(obj["attributes"]["final_states"])
        service = build_service_from_transitions(transitions, initial_state, final_states)
        return ServiceInstance(
            service_id,
            service,
            current_state,
            current_transition_function
        )

    @property
    def json(self) -> Dict:
        """Get the service instance in JSON format."""
        result = dict()

        result["id"] = str(self.service_id)
        result["features"] = dict(
            transition_function=self.transition_function,
            current_state=self.current_state
        )
        result["attributes"] = dict(
            type=ServiceType.SERVICE.value,
            transitions=self.service_spec.transition_function,
            initial_state=self.service_spec.initial_state,
            final_states=sorted(self.service_spec.final_states)
        )
        return result

    @property
    def current_service_spec(self):
        return Service(
            self.service_spec.states,
            self.service_spec.actions,
            self.service_spec.final_states,
            self.service_spec.initial_state,
            self.transition_function
        )


