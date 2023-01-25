# Industrial APIs

Implementing **Industrial APIs** for industrial devices. 

Follow [template.json](actors_api/device_descriptions/template.json) to generate the devices descriptions. The different aspects of the actor are represented as attributes and features. <em>Features</em> can either represent a state with properties (e.g., <code>status</code>, <code>voltage</code>) or a functionality of the actor (e.g., <code>converting</code>), while <em>attributes</em> (e.g., <code>type</code>) hold values that do not change or that change less frequently than the <em>feature</em> property values. Noticeably, for what concerns functionalities, effects can be different if something goes wrong during the execution. For example, if the <code>convert</code> fails, one or more effects could not be verified.

