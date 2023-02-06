from typing import Any, Dict, List
from actors_api_plan.helpers import get_type_service


class Actor:
    service_id: str
    service_type: str
    current_state: Any
    actions: Dict[str, List[Any]]

    def __init__(self, service_id: str, service_type: str, current_state: Any, actions: Dict[str, List[Any]]) -> None:
        self.service_id = service_id
        self.service_type = service_type
        self.current_state = current_state
        self.actions = actions


def build_actor_from_json(data: Dict) -> "Actor":
        """Get the actor from JSON format."""
        service_id = data["id"]
        service_type = data["attributes"]["type"]
        current_state = data["features"]
        if service_type == "service":
            actions_dict = data["attributes"]["actions"]
            actions = {}
            for act in actions_dict.keys():
                action_description = actions_dict[act]["properties"]
                action: Action = build_action_from_json(act, action_description)
                actions[act] = action
            
            return Actor(
                service_id,
                service_type,
                current_state,
                actions
            )
        else:
            return Actor(
                service_id,
                service_type,
                current_state,
                {}
            )



class Action:
    name: str
    type: str
    command: str
    cost: int
    parameters: List[str]
    requirements: Dict[str, List]
    effects: Dict[str, List]

    def __init__(self, name: str, type: str, command: str, cost: int, parameters: List[str], requirements: Dict[str, List], effects: Dict[str, List]) -> None:
        self.name = name
        self.type = type
        self.command = command
        self.cost = cost
        self.parameters = parameters
        self.requirements = requirements
        self.effects = effects


    def get_result_action(self, parameters: List[str]):
        """Check if the action is conform to the action."""
        name_param = ""
        for i in range(len(parameters)):
            serv_type = get_type_service(parameters[i])
            if serv_type in self.parameters[i]:
                name_param = self.parameters[i].split(" - ")[1]
                
                addedEffect = self.effects["added"]
                for effect in addedEffect:
                    effectTokens = effect.split(":")
                    paramEffect = effectTokens[0].split(":")
                    nameParamEffect = paramEffect[0]
                    if nameParamEffect == name_param:
                        stateParamEffect = paramEffect[1]
                        resultParamEffect = effectTokens[1]
                        update = {"service_id": parameters[i], "state": stateParamEffect, "result": resultParamEffect}
                        return update
        return None


def build_action_from_json(name, data) -> "Action":
    """Get the action from JSON format."""
    name = name
    type = data["type"]
    command = data["command"]
    cost = data["cost"]
    parameters = data["parameters"]
    requirements = data["requirements"]
    effects = data["effects"]
    
    return Action(
        name,
        type,
        command,
        cost,
        parameters,
        requirements,
        effects
    )
