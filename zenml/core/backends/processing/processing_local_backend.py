#  Copyright (c) maiot GmbH 2020. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""Definition of the data Processing Backend"""

from zenml.core.backends.base_backend import BaseBackend


class ProcessingLocalBackend(BaseBackend):
    """
    Use this class to run a ZenML pipeline locally.

    Every ZenML pipeline runs in backends.

    A dedicated processing backend can be used to efficiently process large
    amounts of incoming data in parallel, potentially distributed across
    multiple machines. This can happen on local processing backends as well
    as cloud-based variants like Google Cloud Dataflow. More powerful machines
    with higher core counts and clock speeds can be leveraged to increase
    processing throughput significantly.
    """
    BACKEND_TYPE = 'local'
    BACKEND_KEY = 'processing'
