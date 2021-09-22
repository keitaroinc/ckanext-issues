[![CI Actions Status](https://github.com/keitaroinc/ckanext-issues/workflows/CI/badge.svg)](https://github.com/keitaroinc/ckanext-issues/actions) [![Coverage Status](https://coveralls.io/repos/github/keitaroinc/ckanext-issues/badge.svg?branch=master)](https://coveralls.io/github/keitaroinc/ckanext-issues?branch=master) [![Python](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org) [![CKAN](https://img.shields.io/badge/ckan-2.9-red)](https://www.ckan.org)
# CKAN Issues Extension

This extension allows users to to report issues with datasets in a CKAN
instance.

## Requirements

This extension works with CKAN 2.9+.

## Installation

To install the plugin, enter your virtualenv and install from pip or source:

    pip install ckanext-isssues
   
    pip install -e git+http://github.com/keitaroinc/ckanext-issues

Create the necessary tables:

    ckan -c path-to/ckan.ini issuesdb

This will also register a plugin entry point, so you now should be
able to add the following to your CKAN .ini file::

    ckan.plugins = issues

After you clear your cache and restart the web server, the Issues extension
should be available.

## Upgrade from older versions

When upgrading ckanext-issues from older code versions, you should run the issues upgrade command, in case there are any model migrations (e.g. 11th Jan 2016):

    ckan -c path-to/ckan.ini issuesupdate

## What it does

Once installed and enabled, the issues extension will make available a per-
dataset issue tracker.

The issue tracker user interface can be found at:

    /dataset/{dataset-name-or-id}/issues

You can add an issue at:

    /dataset/{dataset-name-or-id}/issues/new

### Issues API

The issues extension also exposes its functionality as part of the standard [CKAN Action API][api]:

[api]: http://docs.ckan.org/en/latest/api/index.html

Specifically:

    /api/3/action/issue_show
    /api/3/action/issue_create
    /api/3/action/issue_update
    /api/3/action/issue_delete
    /api/3/action/issue_search
    /api/3/action/issue_count
    /api/3/action/issue_comment_create
    /api/3/action/issue_report
    /api/3/action/issue_report_clear
    /api/3/action/issue_comment_report
    /api/3/action/issue_comment_report_clear

## Configuration

To switch-on notifications, you should set the following option in your
configuration, and all users in the group will get the email.

    ckanext.issues.send_email_notifications = true

If you set max_strikes then users can 'report' a comment as spam/abuse. If the number of users reporting a particular comment hits the max_strikes number then it is hidden, pending moderation.

    ckanext.issues.max_strikes = 2

### Activation

By default, issues are enabled for all datasets. If you wish to restrict
issues to specific datasets or organizations, you can use these config options:
    
    ckanext.issues.enabled_for_datasets = mydataset1 mydataset2 ...
    ckanext.issues.enabled_for_organizations = department-of-transport health-regulator

Alternatively, you can switch issues on/off for particular datasets by using an extra field:

    'issues_enabled': True

and you can set the default for all the other datasets (without that extra field):

    ckanext.issues.enabled_without_extra = false

For the extra field to work you must not set `enabled_per_dataset` or `enabled_for_organizations` options.

## Feedback

Please open an issue in the github [issue tracker][issues].

[issues]: https://github.com/keitaroinc/ckanext-issues

## Developers

Normal requirements for CKAN Extensions (including an installation of CKAN and
its dev requirements). Contributions welcome.

### Testing with Postgres
To run full production tests on postgres run. These are the tests that the travis build will run

    pytest --ckan-ini=test.ini ckanext/issues/tests
    
