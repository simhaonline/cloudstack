# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


"""Delete one or more alerts."""
from baseCmd import *
from baseResponse import *
class deleteAlertsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """end date range to delete alerts (including) this date (use format "yyyy-MM-dd" or the new format "yyyy-MM-ddThh:mm:ss")"""
        self.enddate = None
        """the IDs of the alerts"""
        self.ids = []
        """start date range to delete alerts (including) this date (use format "yyyy-MM-dd" or the new format "yyyy-MM-ddThh:mm:ss")"""
        self.startdate = None
        """delete by alert type"""
        self.type = None
        self.required = []

class deleteAlertsResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

