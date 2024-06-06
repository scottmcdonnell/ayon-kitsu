"""tests for endpoint 'api/addons/kitsu/{version}/push'
with entities of kitsu type: Project

$ poetry run pytest tests/test_push_project.py
"""

from pprint import pprint

import pytest

from . import mock_data
from .fixtures import (
    PAIR_PROJECT_CODE,
    PAIR_PROJECT_NAME,
    PROJECT_CODE,
    PROJECT_ID,
    PROJECT_NAME,
    api,
    kitsu_url,
    ensure_kitsu_server_setting,
    delete_projects_enabled,
    delete_projects_disabled,
)


def test_update_project(api, kitsu_url, ensure_kitsu_server_setting):
    """update project anatomy based on kitsu data

    we create a project with just 1 task type.
    Then when task types are added in Kitsu the project.update event is fired.
    The project meta then has more task types that need to be synced with Ayon.
    Same for statuses and folderTypes. We start with just status: Todo and then add more.
    """

    api.delete("/projects/test_project")
    assert not api.get_project("test_project")

    entity = {
        "name": "test_project",
        "code": "TP",
        "id": "test-project-id",
        "type": "Project",
    }

    project_meta = {
        "code": "TEST_P",
        "folderTypes": [{"name": "Folder"}],
        "taskTypes": [{"name": "Animation"}],
        "statuses": [{"name": "Todo"}],
        "data": {"kitsuProjectId": "kitsu-project-id-1"},
    }

    # create the test project
    res = api.put("/projects/test_project", **project_meta)

    project = api.get_project("test_project")
    assert project["folderTypes"] == [{"name": "Folder"}]
    assert project["taskTypes"] == [{"name": "Animation"}]
    assert project["statuses"] == [{"name": "Todo"}]

    res = api.post(
        f"{kitsu_url}/push",
        project_name=entity["name"],
        entities=[entity],
        mock=True,
    )
    print(res.data)
    assert res.status_code == 200
    project = api.get_project("test_project")

    assert project["folderTypes"] == [
        {"icon": "folder", "name": "Folder", "shortName": ""},
        {"icon": "library_books", "name": "Library", "shortName": "lib"},
        {"icon": "web_asset", "name": "Asset", "shortName": ""},
        {"icon": "live_tv", "name": "Episode", "shortName": "ep"},
        {"icon": "theaters", "name": "Sequence", "shortName": "sq"},
        {"icon": "screenshot_keyboard", "name": "Shot", "shortName": "sh"},
    ]

    assert project["statuses"] == [
        {
            "color": "#f5f5f5",
            "icon": "task_alt",
            "name": "Todo",
            "shortName": "TODO",
            "state": "in_progress",
        },
        {
            "color": "#22D160",
            "icon": "task_alt",
            "name": "Approved",
            "shortName": "App",
            "state": "in_progress",
        },
    ]
    assert project["taskTypes"] == [
        {"icon": "directions_run", "name": "Animation", "shortName": "anim"},
        {"icon": "layers", "name": "Compositing", "shortName": "comp"},
        {"icon": "task_alt", "name": "Grading", "shortName": "Grad"},
    ]
    api.delete("/projects/test_project")


def test_push_unsynced_project(api, kitsu_url):
    entity = mock_data.projects[1]

    project_meta = {
        "code": "ATK",
        "folderTypes": [
            {"name": "Folder"},
            {"name": "Library"},
            {"name": "Asset"},
            {"name": "Episode"},
            {"name": "Sequence"},
            {"name": "Shot"},
        ],
        "taskTypes": [{"name": "Animation"}],
        "statuses": [{"name": "Todo"}],
    }

    # create the 2nd test project
    api.put(f"/projects/{entity['name']}", **project_meta)

    project = api.get_project(entity["name"])
    assert project

    res = api.post(
        f"{kitsu_url}/push",
        project_name=entity["name"],
        entities=[entity],
        mock=True,
    )
    assert res.status_code == 200

    # no project changes as project is not synced
    target_project = api.get_project(entity["name"])
    assert project == target_project


def test_delete_project_disabled(api, kitsu_url, delete_projects_disabled):
    """testing attempting to remove a project
    when delete_projects is False in the kitsu settings"""
    entity = mock_data.projects[0]

    res = api.post(
        f"{kitsu_url}/remove", project_name=entity["name"], entities=[entity]
    )
    assert res.status_code == 200

    # project should still exist
    assert api.get_project(entity["name"])


def test_delete_project_enabled(api, kitsu_url, delete_projects_enabled):
    """testing attempting to remove a project
    when delete_projects is True in the kitsu settings"""
    entity = mock_data.projects[0]

    res = api.post(
        f"{kitsu_url}/remove", project_name=entity["name"], entities=[entity]
    )
    assert res.status_code == 200

    # project should be deleted
    assert not api.get_project(entity["name"])
