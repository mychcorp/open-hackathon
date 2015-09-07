# -*- coding: utf-8 -*-
"""
Copyright (c) Microsoft Open Technologies (Shanghai) Co. Ltd.  All rights reserved.
 
The MIT License (MIT)
 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import sys

sys.path.append("..")

from hackathon import api

from resources import *

__all__ = ["init_routes"]


def init_routes():
    """Register RESTFul API routes"""
    # health page API
    api.add_resource(HealthResource, "/", "/health")

    # system time API
    api.add_resource(CurrentTimeResource, "/api/currenttime")

    # APIs for template library
    api.add_resource(TemplateResource, "/api/template")  # query, create or delete template
    api.add_resource(TemplateCreateByFileResource, "/api/template/file")  # create template from file
    api.add_resource(TemplateListResource, "/api/template/list")  # list templates

    # APIs for hackathon query that not related to user or admin
    api.add_resource(HackathonResource, "/api/hackathon")  # query hackathon
    api.add_resource(HackathonListResource, "/api/hackathon/list")  # list hackathons
    api.add_resource(HackathonStatResource, "/api/hackathon/stat")  # get statistics of hackathon
    api.add_resource(HackathonTeamListResource, "/api/hackathon/team/list")  # list teams of hackathon
    api.add_resource(HackathonRegistrationListResource, "/api/hackathon/registration/list")  # list registered users

    # APIs for user(participant) to join hackathon
    api.add_resource(GuacamoleResource, "/api/user/guacamoleconfig")  # get remote paras for guacamole
    api.add_resource(CurrentUserResource, "/api/user")  # get current login user
    api.add_resource(UserProfileResource, "/api/user/profile")  # update user profile
    api.add_resource(UserTemplateListResource, "/api/hackathon/template")  # list templates for specific user
    api.add_resource(UserRegistrationResource, "/api/user/registration")  # register hackathon
    api.add_resource(UserHackathonListResource, "/api/user/registration/list")  # participated hackathon list of user
    api.add_resource(UserExperimentResource, "/api/user/experiment")  # start or stop experiment
    api.add_resource(UserExperimentListResource, "/api/user/experiment/list")  # expr list of user
    api.add_resource(UserTeamsResource, "/api/user/team/list")  # list all teams of user

    # team APIs
    api.add_resource(TeamResource, "/api/team")  # create, update, dismiss and query team
    api.add_resource(TeamListResource, "/api/team/list")  # list teams of hackathon
    api.add_resource(TeamMemberResource, "/api/team/member")  # join or leave team, approve member
    api.add_resource(TeamMemberListResource, "/api/team/member/list")  # list team members
    api.add_resource(TeamLeaderResource, "/api/team/leader")  # promote team leader
    api.add_resource(TeamTemplateResource, "/api/team/template")  # select or unselect template for team

    # APIs for admin to manage hackathon and hackathon resources, features and users
    api.add_resource(AdminHackathonResource, "/api/admin/hackathon")  # create/update hackathon
    api.add_resource(HackathonCheckNameResource, "/api/admin/hackathon/checkname")  # check hackathon name exists
    api.add_resource(AdminHackathonListResource, "/api/admin/hackathon/list")  # get entitled hackathon list
    api.add_resource(AdminAzureResource, '/api/admin/azure')  # manage azure subscription and certs
    api.add_resource(AdminRegisterListResource, "/api/admin/registration/list")  # get registered users
    api.add_resource(AdminRegisterResource, "/api/admin/registration")  # create, delete or query registration
    api.add_resource(AdminHackathonTemplateListResource, "/api/admin/template/list")  # get templates of hackathon
    api.add_resource(AdminHackathonTemplateResource, "/api/admin/template")  # select template for hackathon
    api.add_resource(AdminExperimentResource, "/api/admin/experiment")  # start expr by admin
    api.add_resource(AdminExperimentListResource, "/api/admin/experiment/list")  # get expr list of hackathon
    api.add_resource(AdminHackathonFileResource, "/api/admin/file")  # upload hackathon image
    api.add_resource(HackathonAdminListResource, "/api/admin/hackathon/administrator/list")  # list admin/judges
    api.add_resource(HackathonAdminResource, "/api/admin/hackathon/administrator")  # add or delete admin/judge