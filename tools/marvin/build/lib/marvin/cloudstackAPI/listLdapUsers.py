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


"""Lists all LDAP Users"""
from baseCmd import *
from baseResponse import *
class listLdapUsersCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        """Determines whether all ldap users are returned or just non-cloudstack users"""
        self.listtype = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = []

class listLdapUsersResponse (baseResponse):
    def __init__(self):
        """The user's email"""
        self.email = None
        """The user's firstname"""
        self.firstname = None
        """The user's lastname"""
        self.lastname = None
        """The user's principle"""
        self.principal = None
        """The user's username"""
        self.username = None

