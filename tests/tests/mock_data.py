""" mock kitsu api data for patching gazu """

projects = [
    {
        "name": "test_kitsu_project",
        "code": "TP1",
        "id": "kitsu-project-id-1",
        "type": "Project",
    },
    {
        "name": "another_test_kitsu_project",
        "code": "TP2",
        "id": "kitsu-project-id-2",
        "type": "Project",
    },
]

# /api/data/task-status
all_task_statuses = [
    {
        "name": "Todo",
        "archived": True,
        "short_name": "TODO",
        "color": "#f5f5f5",
        "priority": 18,
        "is_done": False,
        "is_artist_allowed": True,
        "is_client_allowed": True,
        "is_retake": False,
        "is_feedback_request": False,
        "is_default": False,
        "shotgun_id": None,
        "for_concept": False,
        "id": "task-status-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "TaskStatus",
    },
    {
        "name": "Approved",
        "archived": False,
        "short_name": "App",
        "color": "#22D160",
        "priority": 1,
        "is_done": False,
        "is_artist_allowed": False,
        "is_client_allowed": False,
        "is_retake": False,
        "is_feedback_request": False,
        "is_default": False,
        "shotgun_id": None,
        "for_concept": True,
        "id": "task-status-id-2",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "TaskStatus",
    },
]


# /api/data/projects/{kitsu_project_id}/asset-types
all_asset_types_for_project = [
    {"name": "Character", "archived": False, "id": "asset-type-id-1"},
    {"name": "Rig", "archived": False, "id": "asset-type-id-2"},
    {"name": "Location", "archived": False, "id": "asset-type-id-3"},
]
# /api/data/projects/{kitsu_project_id}/task-types
all_task_types = [
    {
        "name": "Animation",
        "short_name": "ANIM",
        "color": "#DDD",
        "priority": 5,
        "for_entity": "Shot",
        "allow_timelog": True,
        "archived": False,
        "shotgun_id": None,
        "department_id": "dept-id-1",
        "id": "task-type-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "TaskType",
    },
    {
        "name": "Compositing",
        "short_name": "COMP",
        "color": "#666",
        "priority": 5,
        "for_entity": "Shot",
        "allow_timelog": True,
        "archived": False,
        "shotgun_id": None,
        "department_id": "dept-id-1",
        "id": "task-type-id-2",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "TaskType",
    },
    {
        "name": "Concept",
        "short_name": "",
        "color": "#8D6E63",
        "priority": 1,
        "for_entity": "Concept",
        "allow_timelog": True,
        "archived": False,
        "shotgun_id": None,
        "department_id": None,
        "id": "task-type-id-3",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "TaskType",
    },
]

# /api/data/projects/{kitsu_project_id}/episodes
all_episodes_for_project = [
    {
        "id": "episode-id-1",
        "name": "Episode 01",
        "code": "EP001",
        "description": "The first episode",
        "shotgun_id": None,
        "canceled": False,
        "nb_frames": None,
        "nb_entities_out": 0,
        "is_casting_standby": False,
        "status": "running",
        "project_id": "project-id-1",
        "entity_type_id": "entity-type-id-ep",
        "parent_id": None,
        "source_id": None,
        "preview_file_id": None,
        "data": {},
        "ready_for": None,
        "created_by": "user-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "Episode",
    },
    {
        "id": "episode-id-2",
        "name": "Episode 02",
        "code": "EP002",
        "description": "The second episode",
        "shotgun_id": None,
        "canceled": False,
        "nb_frames": None,
        "nb_entities_out": 0,
        "is_casting_standby": False,
        "status": "running",
        "project_id": "project-id-1",
        "entity_type_id": "entity-type-id-ep",
        "parent_id": None,
        "source_id": None,
        "preview_file_id": None,
        "data": {},
        "ready_for": None,
        "created_by": "user-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "Episode",
    },
]

# /api/data/projects/{kitsu_project_id}/sequences
all_sequences_for_project = [
    {
        "id": "sequence-id-1",
        "name": "SEQ01",
        "code": None,
        "description": "A Sequence",
        "shotgun_id": None,
        "canceled": False,
        "nb_frames": None,
        "nb_entities_out": 0,
        "is_casting_standby": False,
        "status": "running",
        "project_id": "project-id-1",
        "entity_type_id": "entity-type-id-seq",
        "parent_id": "episode-id-2",
        "source_id": None,
        "preview_file_id": None,
        "data": {},
        "ready_for": None,
        "created_by": "user-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "Sequence",
    },
    {
        "id": "sequence-id-2",
        "name": "SEQ02",
        "code": None,
        "description": "Another Sequence",
        "shotgun_id": None,
        "canceled": False,
        "nb_frames": None,
        "nb_entities_out": 0,
        "is_casting_standby": False,
        "status": "running",
        "project_id": "project-id-1",
        "entity_type_id": "entity-type-id-seq",
        "parent_id": "episode-id-2",
        "source_id": None,
        "preview_file_id": None,
        "data": {},
        "ready_for": None,
        "created_by": "user-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "Sequence",
    },
]

# /api/data/projects/{kitsu_project_id}/shots
all_shots_for_project = [
    {
        "id": "shot-id-1",
        "name": "SH001",
        "code": None,
        "description": "",
        "shotgun_id": None,
        "canceled": False,
        "nb_frames": None,
        "nb_entities_out": 0,
        "is_casting_standby": False,
        "status": "running",
        "project_id": "project-id-1",
        "entity_type_id": "entity-type-id-shot",
        "parent_id": "sequence-id-1",
        "source_id": None,
        "preview_file_id": "preview-id-1",
        "data": {"fps": "25", "frame_in": "0", "frame_out": "100"},
        "ready_for": None,
        "created_by": "user-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "Shot",
    },
    {
        "id": "shot-id-2",
        "name": "SH002",
        "code": "sh2",
        "description": "description2",
        "shotgun_id": None,
        "canceled": False,
        "nb_frames": None,
        "nb_entities_out": 0,
        "is_casting_standby": False,
        "status": "running",
        "project_id": "project-id-1",
        "entity_type_id": "entity-type-id-shot",
        "parent_id": "sequence-id-1",
        "source_id": None,
        "preview_file_id": "preview-id-2",
        "data": {"fps": "25", "frame_in": "1", "frame_out": "150"},
        "ready_for": None,
        "created_by": "user-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "Shot",
    },
    {
        "id": "shot-id-3",
        "name": "SH003",
        "code": None,
        "description": "",
        "shotgun_id": None,
        "canceled": False,
        "nb_frames": None,
        "nb_entities_out": 0,
        "is_casting_standby": False,
        "status": "running",
        "project_id": "project-id-1",
        "entity_type_id": "entity-type-id-shot",
        "parent_id": "sequence-id-2",
        "source_id": None,
        "preview_file_id": "preview-id-3",
        "data": {"fps": "29.97", "frame_in": "0", "frame_out": "50"},
        "ready_for": None,
        "created_by": "user-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "Shot",
    },
]

# /api/data/projects/{kitsu_project_id}/assets
all_assets_for_project = [
    {
        "id": "asset-id-1",
        "name": "Main Character",
        "code": None,
        "description": "",
        "shotgun_id": None,
        "canceled": False,
        "nb_frames": None,
        "nb_entities_out": 0,
        "is_casting_standby": False,
        "status": "running",
        "project_id": "project-id-1",
        "entity_type_id": "asset-type-id-1",
        "parent_id": None,
        "source_id": None,
        "preview_file_id": None,
        "data": {},
        "ready_for": None,
        "created_by": "user-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "Asset",
    },
    {
        "id": "asset-id-2",
        "name": "Second Character",
        "code": None,
        "description": "",
        "shotgun_id": None,
        "canceled": False,
        "nb_frames": None,
        "nb_entities_out": 0,
        "is_casting_standby": False,
        "status": "running",
        "project_id": "project-id-1",
        "entity_type_id": "asset-type-id-2",
        "parent_id": None,
        "source_id": None,
        "preview_file_id": None,
        "data": {},
        "ready_for": None,
        "created_by": "user-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "Asset",
    },
]

# adds the preprocessing that fullsync does
all_assets_for_project_preprocessed = [
    {**all_assets_for_project[0], "asset_type_name": "Character"},
    {**all_assets_for_project[1], "asset_type_name": "Rig"},
]


all_tasks_for_project = [
    {
        "id": "task-id-1",
        "name": "main",
        "description": None,
        "priority": 0,
        "duration": 0,
        "estimation": 0,
        "completion_rate": 0,
        "retake_count": 0,
        "sort_order": 0,
        "start_date": None,
        "due_date": None,
        "real_start_date": None,
        "end_date": None,
        "last_comment_date": "2024-01-01T00:00:00",
        "nb_assets_ready": 0,
        "data": None,
        "shotgun_id": None,
        "assignees": [
            # assignees are given the ayon user name in processor/utils
            "testkitsu.user1",
            "testkitsu.user3",
        ],
        "project_id": "project-id-1",
        "task_type_id": "task-type-id-1",
        "task_status_id": "task-status-id-2",
        "entity_id": "shot-id-1",
        "assigner_id": "person-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "Task",
    },
    {
        "id": "task-id-2",
        "name": "main",
        "description": None,
        "priority": 0,
        "duration": 0,
        "estimation": 0,
        "completion_rate": 0,
        "retake_count": 0,
        "sort_order": 0,
        "start_date": None,
        "due_date": None,
        "real_start_date": None,
        "end_date": None,
        "last_comment_date": "2024-01-01T00:00:00",
        "nb_assets_ready": 0,
        "data": None,
        "shotgun_id": None,
        "assignees": [],
        "project_id": "project-id-1",
        "task_type_id": "task-type-id-2",
        "task_status_id": "task-status-id-1",
        "entity_id": "shot-id-1",
        "assigner_id": "user-id-1",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "type": "Task",
    },
]

# adds the preprocessing that fullsync does
all_tasks_for_project_preprocessed = [
    {
        **all_tasks_for_project[0],
        "name": "animation",
        "task_type_name": "Animation",
        "task_status_name": "Todo",
    },
    {
        **all_tasks_for_project[1],
        "name": "compositing",
        "task_type_name": "Compositing",
        "task_status_name": "Approved",
    },
]


all_persons = [
    {
        "active": True,
        "archived": False,
        "contract_type": "permanent",
        "created_at": "2023-04-13T11:33:34",
        "data": None,
        "desktop_login": "",
        "email": "user-id-1@temp.com",
        "email_otp_enabled": False,
        "fido_devices": [],
        "fido_enabled": False,
        "first_name": "Test Kitsu",
        "full_name": "Test kitsu User 1",
        "has_avatar": True,
        "id": "person-id-1",
        "is_generated_from_ldap": False,
        "last_login_failed": "2024-02-12T12:47:19",
        "last_name": "User 1",
        "last_presence": "2024-01-08",
        "ldap_uid": None,
        "locale": "en_US",
        "login_failed_attemps": 0,
        "notifications_discord_enabled": False,
        "notifications_discord_userid": "",
        "notifications_enabled": False,
        "notifications_mattermost_enabled": False,
        "notifications_mattermost_userid": "",
        "notifications_slack_enabled": False,
        "notifications_slack_userid": "",
        "phone": "",
        "preferred_two_factor_authentication": None,
        "role": "admin",
        "shotgun_id": None,
        "timezone": "Europe/Stockholm",
        "totp_enabled": False,
        "type": "Person",
        "updated_at": "2024-02-18T17:25:34",
    },
    {
        "active": True,
        "archived": False,
        "contract_type": "Permanent",
        "created_at": "2024-02-18T17:40:11",
        "data": None,
        "desktop_login": "",
        "email": "user-id-2@temp.com",
        "email_otp_enabled": False,
        "fido_devices": [],
        "fido_enabled": False,
        "first_name": "Test Kitsu",
        "full_name": "Test Kitsu User 2",
        "has_avatar": True,
        "id": "person-id-2",
        "is_generated_from_ldap": False,
        "last_login_failed": None,
        "last_name": "User 2",
        "last_presence": None,
        "ldap_uid": None,
        "locale": "en_US",
        "login_failed_attemps": 0,
        "notifications_discord_enabled": False,
        "notifications_discord_userid": "",
        "notifications_enabled": False,
        "notifications_mattermost_enabled": False,
        "notifications_mattermost_userid": "",
        "notifications_slack_enabled": False,
        "notifications_slack_userid": "",
        "phone": "",
        "preferred_two_factor_authentication": None,
        "role": "supervisor",
        "shotgun_id": None,
        "timezone": "Europe/Paris",
        "totp_enabled": False,
        "type": "Person",
        "updated_at": "2024-02-18T17:50:13",
    },
    {
        "active": True,
        "archived": False,
        "contract_type": "permanent",
        "created_at": "2023-05-24T14:57:30",
        "data": None,
        "desktop_login": "",
        "email": "user-id-3@temp.com",
        "email_otp_enabled": False,
        "fido_devices": [],
        "fido_enabled": False,
        "first_name": "Test Kitsu",
        "full_name": "Test Kitsu User 3",
        "has_avatar": False,
        "id": "person-id-3",
        "is_generated_from_ldap": False,
        "last_login_failed": None,
        "last_name": "User 3",
        "last_presence": None,
        "ldap_uid": None,
        "locale": "en_US",
        "login_failed_attemps": 0,
        "notifications_discord_enabled": False,
        "notifications_discord_userid": "",
        "notifications_enabled": False,
        "notifications_mattermost_enabled": False,
        "notifications_mattermost_userid": "",
        "notifications_slack_enabled": False,
        "notifications_slack_userid": "",
        "phone": "",
        "preferred_two_factor_authentication": None,
        "role": "user",
        "shotgun_id": None,
        "timezone": "Europe/Paris",
        "totp_enabled": False,
        "type": "Person",
        "updated_at": "2024-02-15T16:33:55",
    },
]

all_edits_for_project = [
    {
        "canceled": False,
        "code": None,
        "created_at": "2024-02-13T11:46:58",
        "created_by": "7910f71b-245b-4168-9c92-8bf38d0e403d",
        "data": None,
        "description": "",
        "entity_type_id": "1e1e03ea-3211-4a4c-a389-6bbedf9cd0e9",
        "id": "edit-id-1",
        "is_casting_standby": False,
        "name": "test_edit1",
        "nb_entities_out": 0,
        "nb_frames": None,
        "parent_id": None,
        "preview_file_id": None,
        "project_id": "67c8ad65-0350-4b38-93be-5d0a4653f465",
        "ready_for": None,
        "shotgun_id": None,
        "source_id": None,
        "status": "running",
        "type": "Edit",
        "updated_at": "2024-02-13T11:46:58",
    },
    {
        "canceled": False,
        "code": None,
        "created_at": "2024-02-13T11:46:53",
        "created_by": "7910f71b-245b-4168-9c92-8bf38d0e403d",
        "data": None,
        "description": "",
        "entity_type_id": "1e1e03ea-3211-4a4c-a389-6bbedf9cd0e9",
        "id": "edit-id-2",
        "is_casting_standby": False,
        "name": "test_edit2",
        "nb_entities_out": 0,
        "nb_frames": None,
        "parent_id": None,
        "preview_file_id": None,
        "project_id": "67c8ad65-0350-4b38-93be-5d0a4653f465",
        "ready_for": None,
        "shotgun_id": None,
        "source_id": None,
        "status": "running",
        "type": "Edit",
        "updated_at": "2024-02-13T11:46:53",
    },
]

all_concepts_for_project = [
    {
        "canceled": False,
        "code": None,
        "created_at": "2024-02-19T13:15:55",
        "created_by": "7910f71b-245b-4168-9c92-8bf38d0e403d",
        "data": None,
        "description": None,
        "entity_concept_links": [],
        "entity_type_id": "e6fd7768-c032-4b6f-a5b4-2b0b892b8540",
        "id": "concept-id-1",
        "is_casting_standby": False,
        "name": "temp1.png-5f893bd8-69eb-49d7-9093-fb4cc8327894",
        "nb_entities_out": 0,
        "nb_frames": None,
        "parent_id": None,
        "preview_file_id": "b99985a9-ef30-4951-8d6f-5a4c1a874057",
        "project_id": "67c8ad65-0350-4b38-93be-5d0a4653f465",
        "ready_for": None,
        "shotgun_id": None,
        "source_id": None,
        "status": "running",
        "type": "Concept",
        "updated_at": "2024-02-19T13:15:55",
    },
    {
        "canceled": False,
        "code": None,
        "created_by": "7910f71b-245b-4168-9c92-8bf38d0e403d",
        "data": None,
        "description": None,
        "entity_concept_links": [],
        "entity_type_id": "e6fd7768-c032-4b6f-a5b4-2b0b892b8540",
        "id": "concept-id-2",
        "is_casting_standby": False,
        "name": "temp2.jpg-a219866e-b637-4717-8490-b208a76a0d75",
        "nb_entities_out": 0,
        "nb_frames": None,
        "parent_id": None,
        "preview_file_id": "aa56ffb5-2875-420a-879e-4d23f2b40e28",
        "project_id": "project-id-1",
        "ready_for": None,
        "shotgun_id": None,
        "source_id": None,
        "status": "running",
        "type": "Concept",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
    },
    {
        "canceled": False,
        "code": None,
        "created_at": "2024-02-19T13:16:09",
        "created_by": "7910f71b-245b-4168-9c92-8bf38d0e403d",
        "data": None,
        "description": None,
        "entity_concept_links": [],
        "entity_type_id": "e6fd7768-c032-4b6f-a5b4-2b0b892b8540",
        "id": "concept-id-3",
        "is_casting_standby": False,
        "name": "temp3.jpg-d4e7d9af-5ccb-4192-b350-66b1049ee8f2",
        "nb_entities_out": 0,
        "nb_frames": None,
        "parent_id": None,
        "preview_file_id": "d54934b1-4842-46e9-b703-c93d9d652550",
        "project_id": "67c8ad65-0350-4b38-93be-5d0a4653f465",
        "ready_for": None,
        "shotgun_id": None,
        "source_id": None,
        "status": "running",
        "type": "Concept",
        "updated_at": "2024-02-19T13:16:09",
    },
]

all_concept_tasks = [
    {
        "assignees": [],
        "name": "main",
        "description": None,
        "priority": 0,
        "duration": 0.0,
        "estimation": 0.0,
        "completion_rate": 0,
        "retake_count": 0,
        "sort_order": 0,
        "start_date": None,
        "due_date": None,
        "real_start_date": None,
        "end_date": None,
        "last_comment_date": "2024-02-12T17:48:54",
        "nb_assets_ready": 0,
        "data": None,
        "shotgun_id": None,
        "project_id": "3bbf7eb9-32ad-48a3-ba7b-c26606909c37",
        "task_type_id": "task-type-id-3",
        "task_type_name": "Concept",
        "task_status_id": "status-id-1",
        "task_status_name": "Approved",
        "entity_id": "concept-id-1",
        "assigner_id": "cc27d066-07cb-45c8-8a1c-0ca84eba48b2",
        "id": "concept-task-id-1",
        "created_at": "2024-02-12T17:48:54",
        "updated_at": "2024-02-12T17:48:54",
        "type": "Task",
        "persons": [],
    },
    {
        "assignees": [],
        "name": "main",
        "description": None,
        "priority": 0,
        "duration": 0.0,
        "estimation": 0.0,
        "completion_rate": 0,
        "retake_count": 0,
        "sort_order": 0,
        "start_date": None,
        "due_date": None,
        "real_start_date": None,
        "end_date": None,
        "last_comment_date": "2024-02-12T17:48:54",
        "nb_assets_ready": 0,
        "data": None,
        "shotgun_id": None,
        "project_id": "project-id-1",
        "task_type_id": "task-type-id-3",
        "task_type_name": "Concept",
        "task_status_id": "status-id-1",
        "task_status_name": "Approved",
        "entity_id": "concept-id-2",
        "assigner_id": "user-id-1",
        "id": "concept-task-id-2",
        "created_at": "2024-02-12T17:48:54",
        "updated_at": "2024-02-12T17:48:54",
        "type": "Task",
        "persons": [],
    },
]
