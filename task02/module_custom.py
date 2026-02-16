#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

module = AnsibleModule(
    argument_spec=dict(
        port=dict(type='int', required=True)
    )
)

module.exit_json(msg="port is {{ port }}".replace("{{ port }}", str(module.params["port"])))
