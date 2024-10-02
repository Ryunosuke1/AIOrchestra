from typing import Dict

class WorkflowDesigner:
    def __init__(self):
        self.workflows: Dict[str, dict] = {}

    def create_workflow(self, workflow: dict) -> None:
        """
        Creates a new workflow.

        Args:
            workflow (dict): The workflow dictionary containing workflow details.
        """
        if not isinstance(workflow, dict):
            raise ValueError("Workflow must be a dictionary.")
        if 'id' not in workflow:
            raise ValueError("Workflow must contain an ID.")
        if workflow['id'] in self.workflows:
            raise ValueError("A workflow with the given ID already exists.")
        self.workflows[workflow['id']] = workflow

    def edit_workflow(self, workflow_id: str, workflow: dict) -> None:
        """
        Edits an existing workflow.

        Args:
            workflow_id (str): The ID of the workflow to edit.
            workflow (dict): The updated workflow dictionary containing workflow details.
        """
        if not isinstance(workflow, dict):
            raise ValueError("Workflow must be a dictionary.")
        if 'id' in workflow and workflow['id'] != workflow_id:
            raise ValueError("The ID in the workflow does not match the provided workflow ID.")
        if workflow_id not in self.workflows:
            raise ValueError("A workflow with the given ID does not exist.")
        self.workflows[workflow_id] = workflow

    def delete_workflow(self, workflow_id: str) -> None:
        """
        Deletes an existing workflow.

        Args:
            workflow_id (str): The ID of the workflow to delete.
        """
        if workflow_id not in self.workflows:
            raise ValueError("A workflow with the given ID does not exist.")
        del self.workflows[workflow_id]

    def get_workflow(self, workflow_id: str) -> dict:
        """
        Retrieves an existing workflow.

        Args:
            workflow_id (str): The ID of the workflow to retrieve.

        Returns:
            dict: The workflow dictionary.
        """
        if workflow_id not in self.workflows:
            raise ValueError("A workflow with the given ID does not exist.")
        return self.workflows[workflow_id]
