from datetime import datetime
from typing import Any, Dict, List

from github.GithubObject import CompletableGithubObject
from github.WorkflowStep import WorkflowStep

class WorkflowJob(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def check_run_url(self) -> str: ...
    @property
    def completed_at(self) -> datetime: ...
    @property
    def conclusion(self) -> str: ...
    @property
    def head_sha(self) -> str: ...
    @property
    def html_url(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def node_id(self) -> str: ...
    @property
    def run_id(self) -> int: ...
    @property
    def run_url(self) -> str : ...
    @property
    def started_at(self) -> datetime: ...
    @property
    def status(self) -> str: ...
    @property
    def steps(self) -> List[WorkflowStep]: ...
    @property
    def url(self) -> str: ...
    def logs_url(self) -> str: ...
