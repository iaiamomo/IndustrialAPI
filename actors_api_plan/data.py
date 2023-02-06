import dataclasses
from typing import Any, Dict

from actors_api_plan.actor import Actor, build_actor_from_json


@dataclasses.dataclass(eq=True)
class ServiceInstance:
    service_id: str
    service_spec: Actor
    current_state: Any
    actions: Dict[str, Any]
    attributes: Dict

    @classmethod
    def from_json(cls, data: Dict) -> "ServiceInstance":
        """Get the actor from JSON format."""
        service_id = data["id"]
        service_spec = build_actor_from_json(data)
        current_state = service_spec.current_state
        actions = service_spec.actions

        attributes = data["attributes"]

        return ServiceInstance(
            service_id,
            service_spec,
            current_state,
            actions,
            attributes
        )


    @property
    def json(self) -> Dict:
        """Get the service instance in JSON format."""
        result = dict()

        result["id"] = str(self.service_id)
        result["features"] = {
            "status": {
                "properties": {
                    "value": self.current_state
                }
            }
        }
        result["attributes"] = self.attributes
        return result

    
    def updateState(self, update):
        state = update["state"]
        value = update["value"]

        if state == self.current_state.keys()[0]:
            self.current_state[state]["properties"]["value"] = value
            self.service_spec.current_state[state]["properties"]["value"] = value
