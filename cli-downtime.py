import logging

import click

from datadog_api_client.v2.model.downtime_create_request import DowntimeCreateRequest
from datadog_api_client.v2.model.downtime_create_request import DowntimeCreateRequest
from datadog_api_client.v2.model.downtime_create_request_attributes import DowntimeCreateRequestAttributes
from datadog_api_client.v2.model.downtime_create_request_data import DowntimeCreateRequestData
from datadog_api_client.v2.model.downtime_monitor_identifier_tags import DowntimeMonitorIdentifierTags
from datadog_api_client.v2.model.downtime_resource_type import DowntimeResourceType
from datadog_api_client.v2.model.downtime_schedule_one_time_create_update_request import (
    DowntimeScheduleOneTimeCreateUpdateRequest,
)

@click.command()
@click.option('--appname', help='application name.')

def create_downtime(body: DowntimeCreateRequest):
        """ doc string"""
        return f"The application {body.data.attributes.scope} downtime started"

def get_all_downtimes():
    """ doc string"""
    return


def post_sync_app_argocd(request_url: str):
    """ doc string"""
    return request_url

def syn_app_argocd(appname: str):
    """ doc string"""
    request_url = f"https://cd.apps.argoproj.io/api/v1/applications/{appname}/sync"
    return f"app sync done {appname}"


def sync_command(appname: str):
    """Simple program that greets NAME for a total of COUNT times."""
    body = DowntimeCreateRequest(
        data=DowntimeCreateRequestData(
            attributes=DowntimeCreateRequestAttributes(
                message="dark forest",
                monitor_identifier=DowntimeMonitorIdentifierTags(
                    monitor_tags=[
                        "cat:hat",
                    ],
                ),
                scope=appname,
                schedule=DowntimeScheduleOneTimeCreateUpdateRequest(
                    start=None,
                ),
            ),
            type=DowntimeResourceType.DOWNTIME,
        ),
    )

    try:
        list_downtimes = get_all_downtimes()
        if appname in list_downtimes:
            logging.info(f"The app {appname} is already set to downtime")
            # try sync directly
            try:
                sync_res = syn_app_argocd()
            except Exception as e:
                raise e
        else:
            try:
                create_downtime(body)
            except Exception as e:
                raise e
            try:
                sync_res = syn_app_argocd()
            except Exception as e:
                raise e
            
            if sync_res.status_code==200:
                logging.info(f"The app {appname} is sync")
            else:
                print('retry logic')
            # can also use requests Session with Retry configuration
    except Exception as e:
        raise e 


    
    
if __name__ == '__main__':
    sync_command()