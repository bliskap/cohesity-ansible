#
# cohesity_authentication
#
# Copyright (c) 2022 Cohesity Inc

#

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import env_fallback

__metaclass__ = type

DOCUMENTATION = """
module_utils: cohesity_utilities
short_description: The **CohesityUtilities** utils module provides the authentication token manage
for Cohesity Platforms.
version_added: 1.1.4
description:
    - The **CohesityUtilities** utils module provides the authentication token manage
for Cohesity Platforms.
"""


def cohesity_common_argument_spec():
    return dict(
        cluster=dict(
            type="str", 
            aliases=["cohesity_server"], 
            fallback=(env_fallback, ['COHESITY_CLUSTER'])
        ),
        username=dict(
            type="str", 
            aliases=["cohesity_user", "admin_name", "cohesity_admin"], 
            fallback=(env_fallback, ['COHESITY_USERNAME'])
        ),
        password=dict(
            type="str", 
            aliases=["cohesity_password", "admin_pass"], 
            fallback=(env_fallback, ['COHESITY_PASSWORD']),
            no_log=True
        ),
        validate_certs=dict(
            default=True, 
            type="bool", 
            aliases=["cohesity_validate_certs"], 
            fallback=(env_fallback, ['COHESITY_VALIDATE_CERTS'])
        ),
        state=dict(choices=["present", "absent"], default="present"),
    )


def raise__cohesity_exception__handler(error, module, message=""):
    if not message:
        message = "Unexpected error caused while managing the Cohesity Module."

    module.fail_json(
        msg=message, error_details=str(error), error_class=type(error).__name__
    )


# constants
REQUEST_TIMEOUT = 120
